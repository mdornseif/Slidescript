# $ANTLR 3.2 Sep 23, 2009 12:02:23 Slidescript.g 2010-03-10 07:52:57

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LINE_COMMENT=14
WHITESPACE=16
MINUS=9
EOF=-1
DURCH=11
CODE=5
T__19=19
ML_COMMENT=13
FOURSPACES=15
T__18=18
VARIABLE=6
NEWLINE=7
T__17=17
MAL=10
CONSTANT=12
PLUS=8
ASSIGNMENT=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ASSIGNMENT", "CODE", "VARIABLE", "NEWLINE", "PLUS", "MINUS", "MAL", 
    "DURCH", "CONSTANT", "ML_COMMENT", "LINE_COMMENT", "FOURSPACES", "WHITESPACE", 
    "'='", "'('", "')'"
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
    # Slidescript.g:16:1: code : ( stat )+ -> ^( CODE ( stat )+ ) ;
    def code(self, ):

        retval = self.code_return()
        retval.start = self.input.LT(1)

        root_0 = None

        stat2 = None


        stream_stat = RewriteRuleSubtreeStream(self._adaptor, "rule stat")
        try:
            try:
                # Slidescript.g:16:5: ( ( stat )+ -> ^( CODE ( stat )+ ) )
                # Slidescript.g:16:7: ( stat )+
                pass 
                # Slidescript.g:16:7: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((VARIABLE <= LA1_0 <= NEWLINE)) :
                        alt1 = 1


                    if alt1 == 1:
                        # Slidescript.g:16:9: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_code77)
                        stat2 = self.stat()

                        self._state.following.pop()
                        stream_stat.add(stat2.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1

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
                # 16:17: -> ^( CODE ( stat )+ )
                # Slidescript.g:16:20: ^( CODE ( stat )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CODE, "CODE"), root_1)

                # Slidescript.g:16:27: ( stat )+
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
    # Slidescript.g:18:1: stat : ( VARIABLE '=' additionExp ( NEWLINE | EOF ) -> ^( ASSIGNMENT VARIABLE additionExp ) | NEWLINE ->);
    def stat(self, ):

        retval = self.stat_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VARIABLE3 = None
        char_literal4 = None
        NEWLINE6 = None
        EOF7 = None
        NEWLINE8 = None
        additionExp5 = None


        VARIABLE3_tree = None
        char_literal4_tree = None
        NEWLINE6_tree = None
        EOF7_tree = None
        NEWLINE8_tree = None
        stream_VARIABLE = RewriteRuleTokenStream(self._adaptor, "token VARIABLE")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_17 = RewriteRuleTokenStream(self._adaptor, "token 17")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_additionExp = RewriteRuleSubtreeStream(self._adaptor, "rule additionExp")
        try:
            try:
                # Slidescript.g:18:5: ( VARIABLE '=' additionExp ( NEWLINE | EOF ) -> ^( ASSIGNMENT VARIABLE additionExp ) | NEWLINE ->)
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == VARIABLE) :
                    alt3 = 1
                elif (LA3_0 == NEWLINE) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Slidescript.g:18:9: VARIABLE '=' additionExp ( NEWLINE | EOF )
                    pass 
                    VARIABLE3=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_stat99) 
                    stream_VARIABLE.add(VARIABLE3)
                    char_literal4=self.match(self.input, 17, self.FOLLOW_17_in_stat101) 
                    stream_17.add(char_literal4)
                    self._state.following.append(self.FOLLOW_additionExp_in_stat103)
                    additionExp5 = self.additionExp()

                    self._state.following.pop()
                    stream_additionExp.add(additionExp5.tree)
                    # Slidescript.g:18:34: ( NEWLINE | EOF )
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == NEWLINE) :
                        alt2 = 1
                    elif (LA2_0 == EOF) :
                        alt2 = 2
                    else:
                        nvae = NoViableAltException("", 2, 0, self.input)

                        raise nvae

                    if alt2 == 1:
                        # Slidescript.g:18:35: NEWLINE
                        pass 
                        NEWLINE6=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat106) 
                        stream_NEWLINE.add(NEWLINE6)


                    elif alt2 == 2:
                        # Slidescript.g:18:43: EOF
                        pass 
                        EOF7=self.match(self.input, EOF, self.FOLLOW_EOF_in_stat108) 
                        stream_EOF.add(EOF7)




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
                    # 18:48: -> ^( ASSIGNMENT VARIABLE additionExp )
                    # Slidescript.g:18:51: ^( ASSIGNMENT VARIABLE additionExp )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGNMENT, "ASSIGNMENT"), root_1)

                    self._adaptor.addChild(root_1, stream_VARIABLE.nextNode())
                    self._adaptor.addChild(root_1, stream_additionExp.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 2:
                    # Slidescript.g:19:9: NEWLINE
                    pass 
                    NEWLINE8=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat129) 
                    stream_NEWLINE.add(NEWLINE8)

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

        PLUS10 = None
        MINUS11 = None
        multiplyExp9 = None

        multiplyExp12 = None


        PLUS10_tree = None
        MINUS11_tree = None

        try:
            try:
                # Slidescript.g:26:5: ( multiplyExp ( ( PLUS | MINUS ) multiplyExp )* )
                # Slidescript.g:26:10: multiplyExp ( ( PLUS | MINUS ) multiplyExp )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multiplyExp_in_additionExp155)
                multiplyExp9 = self.multiplyExp()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multiplyExp9.tree)
                # Slidescript.g:26:22: ( ( PLUS | MINUS ) multiplyExp )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((PLUS <= LA5_0 <= MINUS)) :
                        alt5 = 1


                    if alt5 == 1:
                        # Slidescript.g:26:23: ( PLUS | MINUS ) multiplyExp
                        pass 
                        # Slidescript.g:26:23: ( PLUS | MINUS )
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == PLUS) :
                            alt4 = 1
                        elif (LA4_0 == MINUS) :
                            alt4 = 2
                        else:
                            nvae = NoViableAltException("", 4, 0, self.input)

                            raise nvae

                        if alt4 == 1:
                            # Slidescript.g:26:24: PLUS
                            pass 
                            PLUS10=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_additionExp159)

                            PLUS10_tree = self._adaptor.createWithPayload(PLUS10)
                            root_0 = self._adaptor.becomeRoot(PLUS10_tree, root_0)



                        elif alt4 == 2:
                            # Slidescript.g:26:30: MINUS
                            pass 
                            MINUS11=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_additionExp162)

                            MINUS11_tree = self._adaptor.createWithPayload(MINUS11)
                            root_0 = self._adaptor.becomeRoot(MINUS11_tree, root_0)




                        self._state.following.append(self.FOLLOW_multiplyExp_in_additionExp166)
                        multiplyExp12 = self.multiplyExp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multiplyExp12.tree)


                    else:
                        break #loop5



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

        MAL14 = None
        DURCH15 = None
        atomExp13 = None

        atomExp16 = None


        MAL14_tree = None
        DURCH15_tree = None

        try:
            try:
                # Slidescript.g:31:5: ( atomExp ( ( MAL | DURCH ) atomExp )* )
                # Slidescript.g:31:9: atomExp ( ( MAL | DURCH ) atomExp )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atomExp_in_multiplyExp189)
                atomExp13 = self.atomExp()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atomExp13.tree)
                # Slidescript.g:31:17: ( ( MAL | DURCH ) atomExp )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((MAL <= LA7_0 <= DURCH)) :
                        alt7 = 1


                    if alt7 == 1:
                        # Slidescript.g:31:18: ( MAL | DURCH ) atomExp
                        pass 
                        # Slidescript.g:31:18: ( MAL | DURCH )
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == MAL) :
                            alt6 = 1
                        elif (LA6_0 == DURCH) :
                            alt6 = 2
                        else:
                            nvae = NoViableAltException("", 6, 0, self.input)

                            raise nvae

                        if alt6 == 1:
                            # Slidescript.g:31:19: MAL
                            pass 
                            MAL14=self.match(self.input, MAL, self.FOLLOW_MAL_in_multiplyExp193)

                            MAL14_tree = self._adaptor.createWithPayload(MAL14)
                            root_0 = self._adaptor.becomeRoot(MAL14_tree, root_0)



                        elif alt6 == 2:
                            # Slidescript.g:31:24: DURCH
                            pass 
                            DURCH15=self.match(self.input, DURCH, self.FOLLOW_DURCH_in_multiplyExp196)

                            DURCH15_tree = self._adaptor.createWithPayload(DURCH15)
                            root_0 = self._adaptor.becomeRoot(DURCH15_tree, root_0)




                        self._state.following.append(self.FOLLOW_atomExp_in_multiplyExp200)
                        atomExp16 = self.atomExp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atomExp16.tree)


                    else:
                        break #loop7



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

        CONSTANT17 = None
        VARIABLE18 = None
        char_literal19 = None
        char_literal21 = None
        additionExp20 = None


        CONSTANT17_tree = None
        VARIABLE18_tree = None
        char_literal19_tree = None
        char_literal21_tree = None

        try:
            try:
                # Slidescript.g:38:5: ( CONSTANT | VARIABLE | '(' additionExp ')' )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == CONSTANT:
                    alt8 = 1
                elif LA8 == VARIABLE:
                    alt8 = 2
                elif LA8 == 18:
                    alt8 = 3
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # Slidescript.g:38:9: CONSTANT
                    pass 
                    root_0 = self._adaptor.nil()

                    CONSTANT17=self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_atomExp223)

                    CONSTANT17_tree = self._adaptor.createWithPayload(CONSTANT17)
                    self._adaptor.addChild(root_0, CONSTANT17_tree)



                elif alt8 == 2:
                    # Slidescript.g:39:9: VARIABLE
                    pass 
                    root_0 = self._adaptor.nil()

                    VARIABLE18=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_atomExp233)

                    VARIABLE18_tree = self._adaptor.createWithPayload(VARIABLE18)
                    self._adaptor.addChild(root_0, VARIABLE18_tree)



                elif alt8 == 3:
                    # Slidescript.g:40:9: '(' additionExp ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal19=self.match(self.input, 18, self.FOLLOW_18_in_atomExp243)
                    self._state.following.append(self.FOLLOW_additionExp_in_atomExp246)
                    additionExp20 = self.additionExp()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, additionExp20.tree)
                    char_literal21=self.match(self.input, 19, self.FOLLOW_19_in_atomExp248)


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
    FOLLOW_stat_in_code77 = frozenset([1, 6, 7])
    FOLLOW_VARIABLE_in_stat99 = frozenset([17])
    FOLLOW_17_in_stat101 = frozenset([6, 12, 18])
    FOLLOW_additionExp_in_stat103 = frozenset([7])
    FOLLOW_NEWLINE_in_stat106 = frozenset([1])
    FOLLOW_EOF_in_stat108 = frozenset([1])
    FOLLOW_NEWLINE_in_stat129 = frozenset([1])
    FOLLOW_multiplyExp_in_additionExp155 = frozenset([1, 8, 9])
    FOLLOW_PLUS_in_additionExp159 = frozenset([6, 12, 18])
    FOLLOW_MINUS_in_additionExp162 = frozenset([6, 12, 18])
    FOLLOW_multiplyExp_in_additionExp166 = frozenset([1, 8, 9])
    FOLLOW_atomExp_in_multiplyExp189 = frozenset([1, 10, 11])
    FOLLOW_MAL_in_multiplyExp193 = frozenset([6, 12, 18])
    FOLLOW_DURCH_in_multiplyExp196 = frozenset([6, 12, 18])
    FOLLOW_atomExp_in_multiplyExp200 = frozenset([1, 10, 11])
    FOLLOW_CONSTANT_in_atomExp223 = frozenset([1])
    FOLLOW_VARIABLE_in_atomExp233 = frozenset([1])
    FOLLOW_18_in_atomExp243 = frozenset([6, 12, 18])
    FOLLOW_additionExp_in_atomExp246 = frozenset([19])
    FOLLOW_19_in_atomExp248 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SlidescriptLexer", SlidescriptParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
