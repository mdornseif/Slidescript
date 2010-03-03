#!/usr/bin/env python
# encoding: utf-8
"""
slidescript.py - Slidescript paser and Converter

Created by Maximillian Dornseif on 2010-02-28.
Copyright (c) 2010 HUDORA. All rights reserved.
"""

from SlidescriptParser import *
from antlr3 import *
from antlr3.tree import *
from pprint import pprint
import SlidescriptLexer
import argparse
import sys
import xlwt


# The internal code representation is the "namespace". Namespace is a dict
# where the key are variable names and the value is a node.
#
# A node can be one of the following:
#
# * `Variable` being a symbolic representation of something else. A 
#   Variable points into the namespace. A Variable is always represented
#   as a string with a length greater than 1
# * `Operator` representing a mathematical operation. A Operator is always
#   represented as a string of length 1.
# * `Value` representing a numeric value. A Float is always represented
#   by a float value
# * `subtree` collecting other nodes. A subtreee usually starts with a
#   operater and is vollowed by Values or Variables. A Subtree is represented
#   by a tuple


def is_variable(node):
    return (isinstance(node, basestring) and len(node) > 1)


def is_unknown(node):
    return (isinstance(node, basestring) and node.startswith('?'))


def is_operator(node):
    return (isinstance(node, basestring) and len(node) == 1)


def is_value(node):
    return isinstance(node, float)


def is_subtree(node):
    return isinstance(node, tuple)



def resolve_antlr_node(node, namespace):
    if node.getType() == VARIABLE:
        if node.getText() not in namespace:
            namespace[node.getText()] = '?Unknown'
        return node.getText()
    if node.getType() == CONSTANT:
        return float(node.getText())
    else:
        operation = node
        operand1 = node.getChild(0)
        operand2 = node.getChild(1)
        return (str(operation.getText()), resolve_antlr_node(operand1, namespace), resolve_antlr_node(operand2, namespace))


def node_to_string(node, var2loc={}):
    """Convert a node and it's subnodes to a string."""
    if is_variable(node):
        return var2loc.get(node, node)
    elif is_value(node):
        return node
    elif is_subtree(node) and len(node) == 3 and is_operator(node[0]):
        return "(%s %s %s)" % (node_to_string(node[1], var2loc), node[0], node_to_string(node[2], var2loc))
    else:
        raise ValueError("unknown node type %r" % node)


def parse(value, debug=False):
    namespace = {}
    char_stream = ANTLRStringStream(value+'\n')
    lexer = SlidescriptLexer.SlidescriptLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = SlidescriptParser(tokens)
    result = parser.program()
    # unser Root-Node heisst code und da haengen die enzelnen statements dran
    if result.tree.getType() != CODE:
        print result.tree.toStringTree()
        raise ValueError('invalid type %s' % result.tree.getType())
    statements = [result.tree.getChild(x) for x in range(result.tree.getChildCount())]
    for statement in statements:
        if debug:
            print statement.toStringTree()
        if statement.getChildCount() != 2:
            if not statement.token:
                continue
            raise ValueError(statement.toStringTree())
        var = statement.getChild(0)
        assert var.getType() == VARIABLE
        varname = var.getText()
        val = statement.getChild(1)
        assert var.getType() == VARIABLE
        namespace[varname] = resolve_antlr_node(val, namespace)
    return namespace


def calculate_dependencies_helper(node):
    ret = []
    if is_variable(node):
        ret.append(node)
    if is_subtree(node):
        for subnode in node:
            ret.extend(calculate_dependencies_helper(subnode))
    return ret


def calculate_dependencies(namespace):
    ret = {}
    for varname in namespace:
        ret[varname] = calculate_dependencies_helper(namespace[varname])
    return ret


def ersetzen_helper(node, myvars):
    ret = []
    if is_variable(node) and is_value(myvars.get(node)):
        ret.append(myvars[node])
    elif is_subtree(node):
        for subnode in node:
            ret.append(ersetzen_helper(subnode, myvars))
    else:
        ret.append(node)
    if len(ret) > 1:
        return tuple(ret)
    return ret[0]


def ersetzen(namespace):
    """Ersetzt Variablen durch ihre Werte - wo möglich"""
    newnamespace = {}
    for varname in namespace:
        newnamespace[varname] = ersetzen_helper(namespace[varname], namespace)
    if newnamespace != namespace:
        return ersetzen(newnamespace)
    return newnamespace


def berechnenen_helper(node, namespace):
    if is_subtree(node):
        if len(node) == 3 and is_operator(node[0]) and is_value(node[1]) and is_value(node[2]):
            operator = node[0]
            operand1 = node[1]
            operand2 = node[2]
            if operator == '+':
                return operand1 + operand2
            if operator == '-':
                return operand1 - operand2
            if operator == '*':
                return operand1 * operand2
            if operator == '/':
                return operand1 / operand2
        else:
            ret = []
            for subnode in node:
                ret.append(berechnenen_helper(subnode, namespace))
            return tuple(ret)
    return node


def berechnenen(namespace):
    newnamespace = {}
    for varname in namespace:
        newnamespace[varname] = berechnenen_helper(namespace[varname], namespace)
    return newnamespace


def iterieren(namespace):
    """Werte auflösen, bis alles klärbare geklärt ist."""
    newnamespace = berechnenen(ersetzen(namespace))
    if namespace == newnamespace:
        return namespace
    return iterieren(newnamespace)


def generate_dotfile(namespace, outfd):
    """Generate a graphviz DOT file displaying the Variable dependencies."""
    outfd.write('digraph graphname {\n')
    # see http://www.graphviz.org/cvs/doc/info/attrs.html#d:ratio
    # and http://www.graphviz.org/cvs/doc/info/attrs.html#d:size
    outfd.write('    graph [ratio="compress", size="8.25,11.75"]\n')
    #outfd.write('    graph [ratio="0.7", size="8.25,11.75"]\n')
    for varname, dependencies in calculate_dependencies(namespace).items():
        for dependenciy in dependencies:
            outfd.write('    "%s" -> "%s";\n' % (dependenciy, varname))
    outfd.write('}\n')


def generate_resolvedfile(namespace, outfd):
    """Generates a file conainin resolved variables."""
    for varname, value in iterieren(namespace).items():
        outfd.write('    %s = %s\n' % (varname, value))


def generate_xlsfile(namespace, outfd):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Slidescript %s" % outfd.name)
    # Set to landscape
    ws.portrait = 0
    style_unknown = xlwt.XFStyle()
    style_unknown.pattern = xlwt.Pattern()
    style_unknown.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    style_unknown.pattern.pattern_fore_colour = 5 # (YELLOW)
    var2loc = {} # wo schreiben wir die Variablen hin
    row = 1
    ws.write(0, 0, 'Variable')
    ws.write(0, 1, 'Wert')
    ws.write(0, 2, 'Beschreibung')
    
    for varname, value in sorted(namespace.items()):
        ws.write(row, 0, varname)
        # Note where the Value of the Variable will be ($A$1)
        if is_subtree(value):
            # Beschreibung der Formel
            ws.write(row, 2, node_to_string(value))
        row += 1
        # My understanding o Excel seems to have a off by one Error.
        var2loc[varname] = "$B$%s" % (row)
        
    # Formeln schreiben mit ersetzten Variablen
    row = 1
    for varname, value in sorted(namespace.items()):
        if is_unknown(value):
            # unknown var
            ws.write(row, 1, '', style_unknown)
        else:
            ws.write(row, 1, xlwt.Formula("%s" % node_to_string(value, var2loc)))
        row += 1
    
    # Save the workbook
    wb.save(outfd)



# create the parser
parser = argparse.ArgumentParser(
    description='Parse and convert Slidescript')
#parser.add_argument('infile', nargs='?', help='y help', default=sys.stdout)
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), const=sys.stdin,
    help='Programmcode zum einlesen, wenn nicht angegeben, wird von stdin gelesen.')
#parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('-dP', '--debug-parser', action='store_true', help='debug input parsing')
parser.add_argument(
    '--dot', nargs='?', type=argparse.FileType('w'), const=sys.stdout,
    help='write a Graphviz/dot file displaying the Variable-dependencies')
parser.add_argument(
    '--resolved', nargs='?', type=argparse.FileType('w'), const=sys.stdout,
    help='write a text file with the resolved Variables')
parser.add_argument(
    '--xls', nargs='?', type=argparse.FileType('w'), const=sys.stdout,
    help='write a XLS file containing all the formulas')

# parse the command line
args = parser.parse_args()

sourcelines = []
for line in  args.infile.readlines():
    line = line.decode('utf-8')
    if line.startswith('    '):
        sourcelines.append(line.strip())
        
sourcecode = ('\n'.join(sourcelines)) + '\n'
namespace = parse(sourcecode, args.debug_parser)

if args.dot:
    generate_dotfile(namespace, args.dot)
if args.resolved:
    generate_resolvedfile(namespace, args.resolved)
if args.xls:
    generate_xlsfile(namespace, args.xls)
