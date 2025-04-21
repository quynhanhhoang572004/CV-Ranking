# Generated from grammars/cv_scan.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cv_scanParser import cv_scanParser
else:
    from cv_scanParser import cv_scanParser

# This class defines a complete listener for a parse tree produced by cv_scanParser.
class cv_scanListener(ParseTreeListener):

    # Enter a parse tree produced by cv_scanParser#document.
    def enterDocument(self, ctx:cv_scanParser.DocumentContext):
        pass

    # Exit a parse tree produced by cv_scanParser#document.
    def exitDocument(self, ctx:cv_scanParser.DocumentContext):
        pass


    # Enter a parse tree produced by cv_scanParser#section.
    def enterSection(self, ctx:cv_scanParser.SectionContext):
        pass

    # Exit a parse tree produced by cv_scanParser#section.
    def exitSection(self, ctx:cv_scanParser.SectionContext):
        pass


    # Enter a parse tree produced by cv_scanParser#heading.
    def enterHeading(self, ctx:cv_scanParser.HeadingContext):
        pass

    # Exit a parse tree produced by cv_scanParser#heading.
    def exitHeading(self, ctx:cv_scanParser.HeadingContext):
        pass


    # Enter a parse tree produced by cv_scanParser#paragraph.
    def enterParagraph(self, ctx:cv_scanParser.ParagraphContext):
        pass

    # Exit a parse tree produced by cv_scanParser#paragraph.
    def exitParagraph(self, ctx:cv_scanParser.ParagraphContext):
        pass



del cv_scanParser