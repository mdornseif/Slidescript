# $ANTLR 3.2 Sep 23, 2009 12:02:23 Slidescript.g 2010-03-05 07:40:49

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FOURSPACES=13
T__16=16
T__15=15
NEWLINE=6
VARIABLE=7
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


class SlidescriptLexer(Lexer):

    grammarFileName = "Slidescript.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SlidescriptLexer, self).__init__(input, state)


        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "T__15"
    def mT__15(self, ):

        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:7:7: ( '=' )
            # Slidescript.g:7:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__15"



    # $ANTLR start "T__16"
    def mT__16(self, ):

        try:
            _type = T__16
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:8:7: ( '(' )
            # Slidescript.g:8:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__16"



    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:9:7: ( ')' )
            # Slidescript.g:9:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



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



    # $ANTLR start "FOURSPACES"
    def mFOURSPACES(self, ):

        try:
            _type = FOURSPACES
            _channel = DEFAULT_CHANNEL

            # Slidescript.g:55:11: ( ' ' )
            # Slidescript.g:55:13: ' '
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

            # Slidescript.g:58:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # Slidescript.g:58:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # Slidescript.g:58:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((9 <= LA6_0 <= 10) or (12 <= LA6_0 <= 13) or LA6_0 == 32) :
                    alt6 = 1


                if alt6 == 1:
                    # Slidescript.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # Slidescript.g:1:8: ( T__15 | T__16 | T__17 | CONSTANT | VARIABLE | PLUS | MINUS | MAL | DURCH | NEWLINE | FOURSPACES | WHITESPACE )
        alt7 = 12
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # Slidescript.g:1:10: T__15
            pass 
            self.mT__15()


        elif alt7 == 2:
            # Slidescript.g:1:16: T__16
            pass 
            self.mT__16()


        elif alt7 == 3:
            # Slidescript.g:1:22: T__17
            pass 
            self.mT__17()


        elif alt7 == 4:
            # Slidescript.g:1:28: CONSTANT
            pass 
            self.mCONSTANT()


        elif alt7 == 5:
            # Slidescript.g:1:37: VARIABLE
            pass 
            self.mVARIABLE()


        elif alt7 == 6:
            # Slidescript.g:1:46: PLUS
            pass 
            self.mPLUS()


        elif alt7 == 7:
            # Slidescript.g:1:51: MINUS
            pass 
            self.mMINUS()


        elif alt7 == 8:
            # Slidescript.g:1:57: MAL
            pass 
            self.mMAL()


        elif alt7 == 9:
            # Slidescript.g:1:61: DURCH
            pass 
            self.mDURCH()


        elif alt7 == 10:
            # Slidescript.g:1:67: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt7 == 11:
            # Slidescript.g:1:75: FOURSPACES
            pass 
            self.mFOURSPACES()


        elif alt7 == 12:
            # Slidescript.g:1:86: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\12\uffff\1\15\1\16\1\15\2\uffff\2\15\1\22\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\11\uffff\1\12\1\11\1\40\2\uffff\2\40\1\11\1\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\132\11\uffff\1\12\2\40\2\uffff\3\40\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\3\uffff\1\14\1\12"
        u"\3\uffff\1\13"
        )

    DFA7_special = DFA.unpack(
        u"\23\uffff"
        )

            
    DFA7_transition = [
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
        DFA.unpack(u""),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\2\15\1\uffff\2\15\22\uffff\1\15"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\2\15\1\uffff\2\15\22\uffff\1\15"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
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
