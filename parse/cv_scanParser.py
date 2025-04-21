# Generated from grammars/cv_scan.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\3\3\3\6\3\22\n\3\r\3\16\3\23\3\4\3\4\3\4\3\4")
        buf.write("\3\5\6\5\33\n\5\r\5\16\5\34\3\5\2\2\6\2\4\6\b\2\2\2\35")
        buf.write("\2\13\3\2\2\2\4\17\3\2\2\2\6\25\3\2\2\2\b\32\3\2\2\2\n")
        buf.write("\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16")
        buf.write("\3\2\2\2\16\3\3\2\2\2\17\21\5\6\4\2\20\22\5\b\5\2\21\20")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\5\3\2\2\2\25\26\7\3\2\2\26\27\7\4\2\2\27\30\7\5\2\2\30")
        buf.write("\7\3\2\2\2\31\33\7\4\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35\t\3\2\2\2\5\r\23\34")
        return buf.getvalue()


class cv_scanParser ( Parser ):

    grammarFileName = "cv_scan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TEXT", "NEWLINE", "WS" ]

    RULE_document = 0
    RULE_section = 1
    RULE_heading = 2
    RULE_paragraph = 3

    ruleNames =  [ "document", "section", "heading", "paragraph" ]

    EOF = Token.EOF
    T__0=1
    TEXT=2
    NEWLINE=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cv_scanParser.SectionContext)
            else:
                return self.getTypedRuleContext(cv_scanParser.SectionContext,i)


        def getRuleIndex(self):
            return cv_scanParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = cv_scanParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.section()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cv_scanParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def heading(self):
            return self.getTypedRuleContext(cv_scanParser.HeadingContext,0)


        def paragraph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cv_scanParser.ParagraphContext)
            else:
                return self.getTypedRuleContext(cv_scanParser.ParagraphContext,i)


        def getRuleIndex(self):
            return cv_scanParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = cv_scanParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.heading()
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.paragraph()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cv_scanParser.TEXT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(cv_scanParser.TEXT, 0)

        def NEWLINE(self):
            return self.getToken(cv_scanParser.NEWLINE, 0)

        def getRuleIndex(self):
            return cv_scanParser.RULE_heading

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading" ):
                listener.enterHeading(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading" ):
                listener.exitHeading(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading" ):
                return visitor.visitHeading(self)
            else:
                return visitor.visitChildren(self)




    def heading(self):

        localctx = cv_scanParser.HeadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_heading)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(cv_scanParser.T__0)
            self.state = 20
            self.match(cv_scanParser.TEXT)
            self.state = 21
            self.match(cv_scanParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(cv_scanParser.TEXT)
            else:
                return self.getToken(cv_scanParser.TEXT, i)

        def getRuleIndex(self):
            return cv_scanParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagraph" ):
                return visitor.visitParagraph(self)
            else:
                return visitor.visitChildren(self)




    def paragraph(self):

        localctx = cv_scanParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paragraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 23
                    self.match(cv_scanParser.TEXT)

                else:
                    raise NoViableAltException(self)
                self.state = 26 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





