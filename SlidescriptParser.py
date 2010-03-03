# $ANTLR 3.2 Sep 23, 2009 12:02:23 Slidescript.g 2010-03-03 12:24:49

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FOURSPACES=13
T__16=16
T__15=15
VARIABLE=7
NEWLINE=6
T__17=17
MAL=10
CONSTANT=12
WHITESPACE=14
PLUS=8
ASSIGNMENT=4
MINUS=9
EOF=-1
DURCH=11
CODE=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ASSIGNMENT", "CODE", "NEWLINE", "VARIABLE", "PLUS", "MINUS", "MAL", 
    "DURCH", "CONSTANT", "FOURSPACES", "WHITESPACE", "'='", "'('", "')'"
]




class SlidescriptParser(Parser):
    grammarFileName = "Slidescript.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SlidescriptParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.program_return, self).__init__()

            self.tree = None




    # $ANTLR start "program"
    # Slidescript.g:14:1: program : ( code ) ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)

        root_0 = None

        code1 = None



        try:
            try:
                # Slidescript.g:14:8: ( ( code ) )
                # Slidescript.g:14:12: ( code )
                pass 
                root_0 = self._adaptor.nil()

                # Slidescript.g:14:12: ( code )
                # Slidescript.g:14:14: code
                pass 
                self._state.following.append(self.FOLLOW_code_in_program65)
                code1 = self.code()

                self._state.following.pop()
                self._adaptor.addChild(root_0, code1.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "program"

    class code_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.code_return, self).__init__()

            self.tree = None




    # $ANTLR start "code"
    # Slidescript.g:15:1: code : ( stat )+ EOF -> ^( CODE ( stat )+ ) ;
    def code(self, ):

        retval = self.code_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF3 = None
        stat2 = None


        EOF3_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_stat = RewriteRuleSubtreeStream(self._adaptor, "rule stat")
        try:
            try:
                # Slidescript.g:15:5: ( ( stat )+ EOF -> ^( CODE ( stat )+ ) )
                # Slidescript.g:15:7: ( stat )+ EOF
                pass 
                # Slidescript.g:15:7: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((NEWLINE <= LA1_0 <= VARIABLE) or LA1_0 == CONSTANT or LA1_0 == 16) :
                        alt1 = 1


                    if alt1 == 1:
                        # Slidescript.g:15:9: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_code76)
                        stat2 = self.stat()

                        self._state.following.pop()
                        stream_stat.add(stat2.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1
                EOF3=self.match(self.input, EOF, self.FOLLOW_EOF_in_code81) 
                stream_EOF.add(EOF3)

                # AST Rewrite
                # elements: stat
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 15:21: -> ^( CODE ( stat )+ )
                # Slidescript.g:15:24: ^( CODE ( stat )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CODE, "CODE"), root_1)

                # Slidescript.g:15:31: ( stat )+
                if not (stream_stat.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_stat.hasNext():
                    self._adaptor.addChild(root_1, stream_stat.nextTree())


                stream_stat.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "code"

    class stat_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.stat_return, self).__init__()

            self.tree = None




    # $ANTLR start "stat"
    # Slidescript.g:17:1: stat : ( additionExp NEWLINE -> additionExp | VARIABLE '=' additionExp NEWLINE -> ^( ASSIGNMENT VARIABLE additionExp ) | NEWLINE ->);
    def stat(self, ):

        retval = self.stat_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE5 = None
        VARIABLE6 = None
        char_literal7 = None
        NEWLINE9 = None
        NEWLINE10 = None
        additionExp4 = None

        additionExp8 = None


        NEWLINE5_tree = None
        VARIABLE6_tree = None
        char_literal7_tree = None
        NEWLINE9_tree = None
        NEWLINE10_tree = None
        stream_VARIABLE = RewriteRuleTokenStream(self._adaptor, "token VARIABLE")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_15 = RewriteRuleTokenStream(self._adaptor, "token 15")
        stream_additionExp = RewriteRuleSubtreeStream(self._adaptor, "rule additionExp")
        try:
            try:
                # Slidescript.g:17:5: ( additionExp NEWLINE -> additionExp | VARIABLE '=' additionExp NEWLINE -> ^( ASSIGNMENT VARIABLE additionExp ) | NEWLINE ->)
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == CONSTANT or LA2 == 16:
                    alt2 = 1
                elif LA2 == VARIABLE:
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == 15) :
                        alt2 = 2
                    elif (LA2_2 == NEWLINE or (PLUS <= LA2_2 <= DURCH)) :
                        alt2 = 1
                    else:
                        nvae = NoViableAltException("", 2, 2, self.input)

                        raise nvae

                elif LA2 == NEWLINE:
                    alt2 = 3
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # Slidescript.g:17:9: additionExp NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_additionExp_in_stat100)
                    additionExp4 = self.additionExp()

                    self._state.following.pop()
                    stream_additionExp.add(additionExp4.tree)
                    NEWLINE5=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat102) 
                    stream_NEWLINE.add(NEWLINE5)

                    # AST Rewrite
                    # elements: additionExp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 17:29: -> additionExp
                    self._adaptor.addChild(root_0, stream_additionExp.nextTree())



                    retval.tree = root_0


                elif alt2 == 2:
                    # Slidescript.g:18:9: VARIABLE '=' additionExp NEWLINE
                    pass 
                    VARIABLE6=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_stat116) 
                    stream_VARIABLE.add(VARIABLE6)
                    char_literal7=self.match(self.input, 15, self.FOLLOW_15_in_stat118) 
                    stream_15.add(char_literal7)
                    self._state.following.append(self.FOLLOW_additionExp_in_stat120)
                    additionExp8 = self.additionExp()

                    self._state.following.pop()
                    stream_additionExp.add(additionExp8.tree)
                    NEWLINE9=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat122) 
                    stream_NEWLINE.add(NEWLINE9)

                    # AST Rewrite
                    # elements: VARIABLE, additionExp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 18:42: -> ^( ASSIGNMENT VARIABLE additionExp )
                    # Slidescript.g:18:45: ^( ASSIGNMENT VARIABLE additionExp )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGNMENT, "ASSIGNMENT"), root_1)

                    self._adaptor.addChild(root_1, stream_VARIABLE.nextNode())
                    self._adaptor.addChild(root_1, stream_additionExp.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 3:
                    # Slidescript.g:19:9: NEWLINE
                    pass 
                    NEWLINE10=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat142) 
                    stream_NEWLINE.add(NEWLINE10)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 19:17: ->
                    root_0 = None


                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "stat"

    class additionExp_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.additionExp_return, self).__init__()

            self.tree = None




    # $ANTLR start "additionExp"
    # Slidescript.g:25:1: additionExp : multiplyExp ( ( PLUS | MINUS ) multiplyExp )* ;
    def additionExp(self, ):

        retval = self.additionExp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS12 = None
        MINUS13 = None
        multiplyExp11 = None

        multiplyExp14 = None


        PLUS12_tree = None
        MINUS13_tree = None

        try:
            try:
                # Slidescript.g:26:5: ( multiplyExp ( ( PLUS | MINUS ) multiplyExp )* )
                # Slidescript.g:26:10: multiplyExp ( ( PLUS | MINUS ) multiplyExp )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multiplyExp_in_additionExp168)
                multiplyExp11 = self.multiplyExp()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multiplyExp11.tree)
                # Slidescript.g:26:22: ( ( PLUS | MINUS ) multiplyExp )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((PLUS <= LA4_0 <= MINUS)) :
                        alt4 = 1


                    if alt4 == 1:
                        # Slidescript.g:26:23: ( PLUS | MINUS ) multiplyExp
                        pass 
                        # Slidescript.g:26:23: ( PLUS | MINUS )
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == PLUS) :
                            alt3 = 1
                        elif (LA3_0 == MINUS) :
                            alt3 = 2
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            raise nvae

                        if alt3 == 1:
                            # Slidescript.g:26:24: PLUS
                            pass 
                            PLUS12=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_additionExp172)

                            PLUS12_tree = self._adaptor.createWithPayload(PLUS12)
                            root_0 = self._adaptor.becomeRoot(PLUS12_tree, root_0)



                        elif alt3 == 2:
                            # Slidescript.g:26:30: MINUS
                            pass 
                            MINUS13=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_additionExp175)

                            MINUS13_tree = self._adaptor.createWithPayload(MINUS13)
                            root_0 = self._adaptor.becomeRoot(MINUS13_tree, root_0)




                        self._state.following.append(self.FOLLOW_multiplyExp_in_additionExp179)
                        multiplyExp14 = self.multiplyExp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multiplyExp14.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "additionExp"

    class multiplyExp_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.multiplyExp_return, self).__init__()

            self.tree = None




    # $ANTLR start "multiplyExp"
    # Slidescript.g:30:1: multiplyExp : atomExp ( ( MAL | DURCH ) atomExp )* ;
    def multiplyExp(self, ):

        retval = self.multiplyExp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MAL16 = None
        DURCH17 = None
        atomExp15 = None

        atomExp18 = None


        MAL16_tree = None
        DURCH17_tree = None

        try:
            try:
                # Slidescript.g:31:5: ( atomExp ( ( MAL | DURCH ) atomExp )* )
                # Slidescript.g:31:9: atomExp ( ( MAL | DURCH ) atomExp )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atomExp_in_multiplyExp202)
                atomExp15 = self.atomExp()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atomExp15.tree)
                # Slidescript.g:31:17: ( ( MAL | DURCH ) atomExp )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((MAL <= LA6_0 <= DURCH)) :
                        alt6 = 1


                    if alt6 == 1:
                        # Slidescript.g:31:18: ( MAL | DURCH ) atomExp
                        pass 
                        # Slidescript.g:31:18: ( MAL | DURCH )
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == MAL) :
                            alt5 = 1
                        elif (LA5_0 == DURCH) :
                            alt5 = 2
                        else:
                            nvae = NoViableAltException("", 5, 0, self.input)

                            raise nvae

                        if alt5 == 1:
                            # Slidescript.g:31:19: MAL
                            pass 
                            MAL16=self.match(self.input, MAL, self.FOLLOW_MAL_in_multiplyExp206)

                            MAL16_tree = self._adaptor.createWithPayload(MAL16)
                            root_0 = self._adaptor.becomeRoot(MAL16_tree, root_0)



                        elif alt5 == 2:
                            # Slidescript.g:31:24: DURCH
                            pass 
                            DURCH17=self.match(self.input, DURCH, self.FOLLOW_DURCH_in_multiplyExp209)

                            DURCH17_tree = self._adaptor.createWithPayload(DURCH17)
                            root_0 = self._adaptor.becomeRoot(DURCH17_tree, root_0)




                        self._state.following.append(self.FOLLOW_atomExp_in_multiplyExp213)
                        atomExp18 = self.atomExp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atomExp18.tree)


                    else:
                        break #loop6



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "multiplyExp"

    class atomExp_return(ParserRuleReturnScope):
        def __init__(self):
            super(SlidescriptParser.atomExp_return, self).__init__()

            self.tree = None




    # $ANTLR start "atomExp"
    # Slidescript.g:37:1: atomExp : ( CONSTANT | VARIABLE | '(' additionExp ')' );
    def atomExp(self, ):

        retval = self.atomExp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONSTANT19 = None
        VARIABLE20 = None
        char_literal21 = None
        char_literal23 = None
        additionExp22 = None


        CONSTANT19_tree = None
        VARIABLE20_tree = None
        char_literal21_tree = None
        char_literal23_tree = None

        try:
            try:
                # Slidescript.g:38:5: ( CONSTANT | VARIABLE | '(' additionExp ')' )
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == CONSTANT:
                    alt7 = 1
                elif LA7 == VARIABLE:
                    alt7 = 2
                elif LA7 == 16:
                    alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # Slidescript.g:38:9: CONSTANT
                    pass 
                    root_0 = self._adaptor.nil()

                    CONSTANT19=self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_atomExp236)

                    CONSTANT19_tree = self._adaptor.createWithPayload(CONSTANT19)
                    self._adaptor.addChild(root_0, CONSTANT19_tree)



                elif alt7 == 2:
                    # Slidescript.g:39:9: VARIABLE
                    pass 
                    root_0 = self._adaptor.nil()

                    VARIABLE20=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_atomExp246)

                    VARIABLE20_tree = self._adaptor.createWithPayload(VARIABLE20)
                    self._adaptor.addChild(root_0, VARIABLE20_tree)



                elif alt7 == 3:
                    # Slidescript.g:40:9: '(' additionExp ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal21=self.match(self.input, 16, self.FOLLOW_16_in_atomExp256)
                    self._state.following.append(self.FOLLOW_additionExp_in_atomExp259)
                    additionExp22 = self.additionExp()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, additionExp22.tree)
                    char_literal23=self.match(self.input, 17, self.FOLLOW_17_in_atomExp261)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atomExp"


    # Delegated rules


 

    FOLLOW_code_in_program65 = frozenset([1])
    FOLLOW_stat_in_code76 = frozenset([6, 7, 12, 16])
    FOLLOW_EOF_in_code81 = frozenset([1])
    FOLLOW_additionExp_in_stat100 = frozenset([6])
    FOLLOW_NEWLINE_in_stat102 = frozenset([1])
    FOLLOW_VARIABLE_in_stat116 = frozenset([15])
    FOLLOW_15_in_stat118 = frozenset([7, 12, 16])
    FOLLOW_additionExp_in_stat120 = frozenset([6])
    FOLLOW_NEWLINE_in_stat122 = frozenset([1])
    FOLLOW_NEWLINE_in_stat142 = frozenset([1])
    FOLLOW_multiplyExp_in_additionExp168 = frozenset([1, 8, 9])
    FOLLOW_PLUS_in_additionExp172 = frozenset([7, 12, 16])
    FOLLOW_MINUS_in_additionExp175 = frozenset([7, 12, 16])
    FOLLOW_multiplyExp_in_additionExp179 = frozenset([1, 8, 9])
    FOLLOW_atomExp_in_multiplyExp202 = frozenset([1, 10, 11])
    FOLLOW_MAL_in_multiplyExp206 = frozenset([7, 12, 16])
    FOLLOW_DURCH_in_multiplyExp209 = frozenset([7, 12, 16])
    FOLLOW_atomExp_in_multiplyExp213 = frozenset([1, 10, 11])
    FOLLOW_CONSTANT_in_atomExp236 = frozenset([1])
    FOLLOW_VARIABLE_in_atomExp246 = frozenset([1])
    FOLLOW_16_in_atomExp256 = frozenset([7, 12, 16])
    FOLLOW_additionExp_in_atomExp259 = frozenset([17])
    FOLLOW_17_in_atomExp261 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SlidescriptLexer", SlidescriptParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
