# $ANTLR 3.2 Sep 23, 2009 12:02:23 Slidescript.g 2010-03-10 07:52:57

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class SlidescriptLexer(Lexer):

    grammarFileName = "Slidescript.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SlidescriptLexer, self).__init__(input, state)


        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )






    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:7:7: ( '=' )
            # Slidescript.g:7:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):

        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:8:7: ( '(' )
            # Slidescript.g:8:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):

        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:9:7: ( ')' )
            # Slidescript.g:9:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__19"



    # $ANTLR start "CONSTANT"
    def mCONSTANT(self, ):

        try:
            _type = CONSTANT
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:44:9: ( ( '0' .. '9' )+ ( '.' ( '0' .. '9' )+ )? )
            # Slidescript.g:44:11: ( '0' .. '9' )+ ( '.' ( '0' .. '9' )+ )?
            pass 
            # Slidescript.g:44:11: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # Slidescript.g:44:12: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1
            # Slidescript.g:44:23: ( '.' ( '0' .. '9' )+ )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 46) :
                alt3 = 1
            if alt3 == 1:
                # Slidescript.g:44:24: '.' ( '0' .. '9' )+
                pass 
                self.match(46)
                # Slidescript.g:44:28: ( '0' .. '9' )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((48 <= LA2_0 <= 57)) :
                        alt2 = 1


                    if alt2 == 1:
                        # Slidescript.g:44:29: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONSTANT"



    # $ANTLR start "VARIABLE"
    def mVARIABLE(self, ):

        try:
            _type = VARIABLE
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:46:9: ( ( 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )+ )
            # Slidescript.g:46:11: ( 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )+
            pass 
            # Slidescript.g:46:11: ( 'A' .. 'Z' )
            # Slidescript.g:46:12: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)



            # Slidescript.g:46:22: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57) or (65 <= LA4_0 <= 90) or LA4_0 == 95 or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # Slidescript.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VARIABLE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:48:5: ( '+' )
            # Slidescript.g:48:7: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:49:6: ( '-' )
            # Slidescript.g:49:8: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MAL"
    def mMAL(self, ):

        try:
            _type = MAL
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:50:4: ( '*' )
            # Slidescript.g:50:6: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAL"



    # $ANTLR start "DURCH"
    def mDURCH(self, ):

        try:
            _type = DURCH
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:51:6: ( '/' )
            # Slidescript.g:51:8: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DURCH"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:53:8: ( ( '\\r' )? '\\n' )
            # Slidescript.g:53:10: ( '\\r' )? '\\n'
            pass 
            # Slidescript.g:53:10: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # Slidescript.g:53:10: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "ML_COMMENT"
    def mML_COMMENT(self, ):

        try:
            _type = ML_COMMENT
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:56:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # Slidescript.g:56:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")
            # Slidescript.g:56:14: ( options {greedy=false; } : . )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 42) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 47) :
                        alt6 = 2
                    elif ((0 <= LA6_1 <= 46) or (48 <= LA6_1 <= 65535)) :
                        alt6 = 1


                elif ((0 <= LA6_0 <= 41) or (43 <= LA6_0 <= 65535)) :
                    alt6 = 1


                if alt6 == 1:
                    # Slidescript.g:56:41: .
                    pass 
                    self.matchAny()


                else:
                    break #loop6
            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ML_COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:60:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # Slidescript.g:60:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")
            # Slidescript.g:60:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 12) or (14 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # Slidescript.g:60:12: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7
            # Slidescript.g:60:26: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # Slidescript.g:60:26: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "FOURSPACES"
    def mFOURSPACES(self, ):

        try:
            _type = FOURSPACES
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:63:11: ( ' ' )
            # Slidescript.g:63:13: ' '
            pass 
            self.match("    ")
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOURSPACES"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:66:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # Slidescript.g:66:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # Slidescript.g:66:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((9 <= LA9_0 <= 10) or (12 <= LA9_0 <= 13) or LA9_0 == 32) :
                    alt9 = 1


                if alt9 == 1:
                    # Slidescript.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # Slidescript.g:1:8: ( T__17 | T__18 | T__19 | CONSTANT | VARIABLE | PLUS | MINUS | MAL | DURCH | NEWLINE | ML_COMMENT | LINE_COMMENT | FOURSPACES | WHITESPACE )
        alt10 = 14
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # Slidescript.g:1:10: T__17
            pass 
            self.mT__17()


        elif alt10 == 2:
            # Slidescript.g:1:16: T__18
            pass 
            self.mT__18()


        elif alt10 == 3:
            # Slidescript.g:1:22: T__19
            pass 
            self.mT__19()


        elif alt10 == 4:
            # Slidescript.g:1:28: CONSTANT
            pass 
            self.mCONSTANT()


        elif alt10 == 5:
            # Slidescript.g:1:37: VARIABLE
            pass 
            self.mVARIABLE()


        elif alt10 == 6:
            # Slidescript.g:1:46: PLUS
            pass 
            self.mPLUS()


        elif alt10 == 7:
            # Slidescript.g:1:51: MINUS
            pass 
            self.mMINUS()


        elif alt10 == 8:
            # Slidescript.g:1:57: MAL
            pass 
            self.mMAL()


        elif alt10 == 9:
            # Slidescript.g:1:61: DURCH
            pass 
            self.mDURCH()


        elif alt10 == 10:
            # Slidescript.g:1:67: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt10 == 11:
            # Slidescript.g:1:75: ML_COMMENT
            pass 
            self.mML_COMMENT()


        elif alt10 == 12:
            # Slidescript.g:1:86: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt10 == 13:
            # Slidescript.g:1:99: FOURSPACES
            pass 
            self.mFOURSPACES()


        elif alt10 == 14:
            # Slidescript.g:1:110: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\11\uffff\1\20\1\15\1\21\1\15\5\uffff\2\15\1\25\1\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\26\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\11\10\uffff\1\52\1\12\1\11\1\40\5\uffff\2\40\1\11\1\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\132\10\uffff\1\57\1\12\2\40\5\uffff\3\40\1\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\4\uffff\1\16\1\13\1\14"
        u"\1\11\1\12\3\uffff\1\15"
        )

    DFA10_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\15\1\13\1\uffff\1\15\1\12\22\uffff\1\14\7\uffff\1"
        u"\2\1\3\1\10\1\6\1\uffff\1\7\1\uffff\1\11\12\4\3\uffff\1\1\3\uffff"
        u"\32\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\4\uffff\1\17"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\2\15\1\uffff\2\15\22\uffff\1\15"),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\2\15\1\uffff\2\15\22\uffff\1\15"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SlidescriptLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
