# Generated from grammars/cv_scan.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cv_scanParser import cv_scanParser
else:
    from cv_scanParser import cv_scanParser

# This class defines a complete generic visitor for a parse tree produced by cv_scanParser.

class cv_scanVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cv_scanParser#document.
    def visitDocument(self, ctx:cv_scanParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cv_scanParser#section.
    def visitSection(self, ctx:cv_scanParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cv_scanParser#heading.
    def visitHeading(self, ctx:cv_scanParser.HeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cv_scanParser#paragraph.
    def visitParagraph(self, ctx:cv_scanParser.ParagraphContext):
        return self.visitChildren(ctx)



del cv_scanParser