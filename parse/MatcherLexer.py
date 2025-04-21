# Generated from grammars/Matcher.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u008a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\7\22")
        buf.write("q\n\22\f\22\16\22t\13\22\3\22\3\22\3\23\3\23\7\23z\n\23")
        buf.write("\f\23\16\23}\13\23\3\24\6\24\u0080\n\24\r\24\16\24\u0081")
        buf.write("\3\25\6\25\u0085\n\25\r\25\16\25\u0086\3\25\3\25\3r\2")
        buf.write("\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26\3\2\6\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2")
        buf.write("\u008d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5\61\3")
        buf.write("\2\2\2\7\63\3\2\2\2\t\65\3\2\2\2\13=\3\2\2\2\rC\3\2\2")
        buf.write("\2\17J\3\2\2\2\21Q\3\2\2\2\23T\3\2\2\2\25Y\3\2\2\2\27")
        buf.write("[\3\2\2\2\31a\3\2\2\2\33c\3\2\2\2\35e\3\2\2\2\37h\3\2")
        buf.write("\2\2!k\3\2\2\2#n\3\2\2\2%w\3\2\2\2\'\177\3\2\2\2)\u0084")
        buf.write("\3\2\2\2+,\7o\2\2,-\7c\2\2-.\7v\2\2./\7e\2\2/\60\7j\2")
        buf.write("\2\60\4\3\2\2\2\61\62\7}\2\2\62\6\3\2\2\2\63\64\7\177")
        buf.write("\2\2\64\b\3\2\2\2\65\66\7t\2\2\66\67\7g\2\2\678\7s\2\2")
        buf.write("89\7w\2\29:\7k\2\2:;\7t\2\2;<\7g\2\2<\n\3\2\2\2=>\7u\2")
        buf.write("\2>?\7m\2\2?@\7k\2\2@A\7n\2\2AB\7n\2\2B\f\3\2\2\2CD\7")
        buf.write("r\2\2DE\7t\2\2EF\7g\2\2FG\7h\2\2GH\7g\2\2HI\7t\2\2I\16")
        buf.write("\3\2\2\2JK\7y\2\2KL\7g\2\2LM\7k\2\2MN\7i\2\2NO\7j\2\2")
        buf.write("OP\7v\2\2P\20\3\2\2\2QR\7k\2\2RS\7h\2\2S\22\3\2\2\2TU")
        buf.write("\7v\2\2UV\7j\2\2VW\7g\2\2WX\7p\2\2X\24\3\2\2\2YZ\7\60")
        buf.write("\2\2Z\26\3\2\2\2[\\\7u\2\2\\]\7e\2\2]^\7q\2\2^_\7t\2\2")
        buf.write("_`\7g\2\2`\30\3\2\2\2ab\7-\2\2b\32\3\2\2\2cd\7/\2\2d\34")
        buf.write("\3\2\2\2ef\7?\2\2fg\7?\2\2g\36\3\2\2\2hi\7@\2\2ij\7?\2")
        buf.write("\2j \3\2\2\2kl\7>\2\2lm\7?\2\2m\"\3\2\2\2nr\7$\2\2oq\13")
        buf.write("\2\2\2po\3\2\2\2qt\3\2\2\2rs\3\2\2\2rp\3\2\2\2su\3\2\2")
        buf.write("\2tr\3\2\2\2uv\7$\2\2v$\3\2\2\2w{\t\2\2\2xz\t\3\2\2yx")
        buf.write("\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|&\3\2\2\2}{\3\2")
        buf.write("\2\2~\u0080\t\4\2\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082(\3\2\2\2\u0083")
        buf.write("\u0085\t\5\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u0089\b\25\2\2\u0089*\3\2\2\2\7\2r{\u0081")
        buf.write("\u0086\3\b\2\2")
        return buf.getvalue()


class MatcherLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    STRING = 17
    IDENTIFIER = 18
    INT = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'match'", "'{'", "'}'", "'require'", "'skill'", "'prefer'", 
            "'weight'", "'if'", "'then'", "'.'", "'score'", "'+'", "'-'", 
            "'=='", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "IDENTIFIER", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "STRING", "IDENTIFIER", "INT", "WS" ]

    grammarFileName = "Matcher.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


