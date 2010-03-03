// This is a ANTLR3 Grammar for slidescript
grammar Slidescript;

options {
    language=Python;
    output=AST;
    //ASTLabelType=CommonTree; // type of $stat.tree ref etc...
}

tokens { ASSIGNMENT; 
         CODE; }

/* This will be the entry point of our parser. */
program:   ( code ) ;
code: ( stat )+ EOF -> ^(CODE stat+) ;

stat:   additionExp NEWLINE -> additionExp
    |   VARIABLE '=' additionExp NEWLINE -> ^(ASSIGNMENT VARIABLE additionExp)
    |   NEWLINE ->
    ;

//assignment: VARIABLE '=' additionExp -> ^(ASSIGNMENT VARIABLE additionExp);

/* Addition and subtraction have the lowest precedence. */
additionExp
    :    multiplyExp ((PLUS^|MINUS^) multiplyExp)*
    ;

/* Multiplication and addition have a higher precedence. */
multiplyExp
    :   atomExp ((MAL^|DURCH^) atomExp)*
    ;

/* An expression atom is the smallest part of an expression: a number. Or 
   when we encounter parenthesis, we're making a recursive call back to the
   rule 'additionExp'. As you can see, an 'atomExp' has the highest precedence. */
atomExp
    :   CONSTANT
    |   VARIABLE
    |   '('! additionExp ')'!
    ;

/* A number: can be an integer value, or a decimal value */
CONSTANT: ('0'..'9')+ ('.' ('0'..'9')+)? ;

VARIABLE: ('A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')+ ;

PLUS: '+';
MINUS: '-';
MAL: '*';
DURCH: '/';

NEWLINE: '\r'? '\n';

FOURSPACES: '    ' { $channel = HIDDEN; };

/* We're going to ignore all white space characters */
WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ { $channel = HIDDEN; };
