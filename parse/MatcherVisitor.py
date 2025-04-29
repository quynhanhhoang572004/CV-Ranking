# Generated from grammars/Matcher.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MatcherParser import MatcherParser
else:
    from MatcherParser import MatcherParser

# This class defines a complete generic visitor for a parse tree produced by MatcherParser.

class MatcherVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatcherParser#matchBlock.
    def visitMatchBlock(self, ctx:MatcherParser.MatchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#matchRule.
    def visitMatchRule(self, ctx:MatcherParser.MatchRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#requireRule.
    def visitRequireRule(self, ctx:MatcherParser.RequireRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#preferRule.
    def visitPreferRule(self, ctx:MatcherParser.PreferRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#scoreRule.
    def visitScoreRule(self, ctx:MatcherParser.ScoreRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#condition.
    def visitCondition(self, ctx:MatcherParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#scoreAction.
    def visitScoreAction(self, ctx:MatcherParser.ScoreActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#comparator.
    def visitComparator(self, ctx:MatcherParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatcherParser#value.
    def visitValue(self, ctx:MatcherParser.ValueContext):
        return self.visitChildren(ctx)



del MatcherParser