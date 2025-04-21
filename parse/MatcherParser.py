# Generated from grammars/Matcher.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\6\2\30\n\2\r\2\16\2\31")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\2\2\13\2\4")
        buf.write("\6\b\n\f\16\20\22\2\5\3\2\16\17\3\2\20\22\4\2\23\23\25")
        buf.write("\25\29\2\24\3\2\2\2\4 \3\2\2\2\6\"\3\2\2\2\b&\3\2\2\2")
        buf.write("\n,\3\2\2\2\f\61\3\2\2\2\16\67\3\2\2\2\20;\3\2\2\2\22")
        buf.write("=\3\2\2\2\24\25\7\3\2\2\25\27\7\4\2\2\26\30\5\4\3\2\27")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\34\7\5\2\2\34\3\3\2\2\2\35!\5\6\4\2")
        buf.write("\36!\5\b\5\2\37!\5\n\6\2 \35\3\2\2\2 \36\3\2\2\2 \37\3")
        buf.write("\2\2\2!\5\3\2\2\2\"#\7\6\2\2#$\7\7\2\2$%\7\23\2\2%\7\3")
        buf.write("\2\2\2&\'\7\b\2\2\'(\7\7\2\2()\7\23\2\2)*\7\t\2\2*+\7")
        buf.write("\25\2\2+\t\3\2\2\2,-\7\n\2\2-.\5\f\7\2./\7\13\2\2/\60")
        buf.write("\5\16\b\2\60\13\3\2\2\2\61\62\7\24\2\2\62\63\7\f\2\2\63")
        buf.write("\64\7\24\2\2\64\65\5\20\t\2\65\66\5\22\n\2\66\r\3\2\2")
        buf.write("\2\678\7\r\2\289\t\2\2\29:\7\25\2\2:\17\3\2\2\2;<\t\3")
        buf.write("\2\2<\21\3\2\2\2=>\t\4\2\2>\23\3\2\2\2\4\31 ")
        return buf.getvalue()


class MatcherParser ( Parser ):

    grammarFileName = "Matcher.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'match'", "'{'", "'}'", "'require'", 
                     "'skill'", "'prefer'", "'weight'", "'if'", "'then'", 
                     "'.'", "'score'", "'+'", "'-'", "'=='", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "IDENTIFIER", "INT", "WS" ]

    RULE_matchBlock = 0
    RULE_matchRule = 1
    RULE_requireRule = 2
    RULE_preferRule = 3
    RULE_scoreRule = 4
    RULE_condition = 5
    RULE_scoreAction = 6
    RULE_comparator = 7
    RULE_value = 8

    ruleNames =  [ "matchBlock", "matchRule", "requireRule", "preferRule", 
                   "scoreRule", "condition", "scoreAction", "comparator", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    STRING=17
    IDENTIFIER=18
    INT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MatchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matchRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatcherParser.MatchRuleContext)
            else:
                return self.getTypedRuleContext(MatcherParser.MatchRuleContext,i)


        def getRuleIndex(self):
            return MatcherParser.RULE_matchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchBlock" ):
                listener.enterMatchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchBlock" ):
                listener.exitMatchBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchBlock" ):
                return visitor.visitMatchBlock(self)
            else:
                return visitor.visitChildren(self)




    def matchBlock(self):

        localctx = MatcherParser.MatchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_matchBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(MatcherParser.T__0)
            self.state = 19
            self.match(MatcherParser.T__1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.matchRule()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatcherParser.T__3) | (1 << MatcherParser.T__5) | (1 << MatcherParser.T__7))) != 0)):
                    break

            self.state = 25
            self.match(MatcherParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requireRule(self):
            return self.getTypedRuleContext(MatcherParser.RequireRuleContext,0)


        def preferRule(self):
            return self.getTypedRuleContext(MatcherParser.PreferRuleContext,0)


        def scoreRule(self):
            return self.getTypedRuleContext(MatcherParser.ScoreRuleContext,0)


        def getRuleIndex(self):
            return MatcherParser.RULE_matchRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchRule" ):
                listener.enterMatchRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchRule" ):
                listener.exitMatchRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchRule" ):
                return visitor.visitMatchRule(self)
            else:
                return visitor.visitChildren(self)




    def matchRule(self):

        localctx = MatcherParser.MatchRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_matchRule)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatcherParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.requireRule()
                pass
            elif token in [MatcherParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.preferRule()
                pass
            elif token in [MatcherParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.scoreRule()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MatcherParser.STRING, 0)

        def getRuleIndex(self):
            return MatcherParser.RULE_requireRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireRule" ):
                listener.enterRequireRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireRule" ):
                listener.exitRequireRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireRule" ):
                return visitor.visitRequireRule(self)
            else:
                return visitor.visitChildren(self)




    def requireRule(self):

        localctx = MatcherParser.RequireRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_requireRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MatcherParser.T__3)
            self.state = 33
            self.match(MatcherParser.T__4)
            self.state = 34
            self.match(MatcherParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreferRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MatcherParser.STRING, 0)

        def INT(self):
            return self.getToken(MatcherParser.INT, 0)

        def getRuleIndex(self):
            return MatcherParser.RULE_preferRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreferRule" ):
                listener.enterPreferRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreferRule" ):
                listener.exitPreferRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreferRule" ):
                return visitor.visitPreferRule(self)
            else:
                return visitor.visitChildren(self)




    def preferRule(self):

        localctx = MatcherParser.PreferRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_preferRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MatcherParser.T__5)
            self.state = 37
            self.match(MatcherParser.T__4)
            self.state = 38
            self.match(MatcherParser.STRING)
            self.state = 39
            self.match(MatcherParser.T__6)
            self.state = 40
            self.match(MatcherParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScoreRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MatcherParser.ConditionContext,0)


        def scoreAction(self):
            return self.getTypedRuleContext(MatcherParser.ScoreActionContext,0)


        def getRuleIndex(self):
            return MatcherParser.RULE_scoreRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScoreRule" ):
                listener.enterScoreRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScoreRule" ):
                listener.exitScoreRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScoreRule" ):
                return visitor.visitScoreRule(self)
            else:
                return visitor.visitChildren(self)




    def scoreRule(self):

        localctx = MatcherParser.ScoreRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scoreRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MatcherParser.T__7)
            self.state = 43
            self.condition()
            self.state = 44
            self.match(MatcherParser.T__8)
            self.state = 45
            self.scoreAction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MatcherParser.IDENTIFIER)
            else:
                return self.getToken(MatcherParser.IDENTIFIER, i)

        def comparator(self):
            return self.getTypedRuleContext(MatcherParser.ComparatorContext,0)


        def value(self):
            return self.getTypedRuleContext(MatcherParser.ValueContext,0)


        def getRuleIndex(self):
            return MatcherParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MatcherParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MatcherParser.IDENTIFIER)
            self.state = 48
            self.match(MatcherParser.T__9)
            self.state = 49
            self.match(MatcherParser.IDENTIFIER)
            self.state = 50
            self.comparator()
            self.state = 51
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScoreActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MatcherParser.INT, 0)

        def getRuleIndex(self):
            return MatcherParser.RULE_scoreAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScoreAction" ):
                listener.enterScoreAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScoreAction" ):
                listener.exitScoreAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScoreAction" ):
                return visitor.visitScoreAction(self)
            else:
                return visitor.visitChildren(self)




    def scoreAction(self):

        localctx = MatcherParser.ScoreActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scoreAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MatcherParser.T__10)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==MatcherParser.T__11 or _la==MatcherParser.T__12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(MatcherParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatcherParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = MatcherParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatcherParser.T__13) | (1 << MatcherParser.T__14) | (1 << MatcherParser.T__15))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MatcherParser.STRING, 0)

        def INT(self):
            return self.getToken(MatcherParser.INT, 0)

        def getRuleIndex(self):
            return MatcherParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MatcherParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==MatcherParser.STRING or _la==MatcherParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





