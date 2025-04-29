# Generated from grammars/Matcher.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MatcherParser import MatcherParser
else:
    from MatcherParser import MatcherParser

# This class defines a complete listener for a parse tree produced by MatcherParser.
class MatcherListener(ParseTreeListener):

    # Enter a parse tree produced by MatcherParser#matchBlock.
    def enterMatchBlock(self, ctx:MatcherParser.MatchBlockContext):
        pass

    # Exit a parse tree produced by MatcherParser#matchBlock.
    def exitMatchBlock(self, ctx:MatcherParser.MatchBlockContext):
        pass


    # Enter a parse tree produced by MatcherParser#matchRule.
    def enterMatchRule(self, ctx:MatcherParser.MatchRuleContext):
        pass

    # Exit a parse tree produced by MatcherParser#matchRule.
    def exitMatchRule(self, ctx:MatcherParser.MatchRuleContext):
        pass


    # Enter a parse tree produced by MatcherParser#requireRule.
    def enterRequireRule(self, ctx:MatcherParser.RequireRuleContext):
        pass

    # Exit a parse tree produced by MatcherParser#requireRule.
    def exitRequireRule(self, ctx:MatcherParser.RequireRuleContext):
        pass


    # Enter a parse tree produced by MatcherParser#preferRule.
    def enterPreferRule(self, ctx:MatcherParser.PreferRuleContext):
        pass

    # Exit a parse tree produced by MatcherParser#preferRule.
    def exitPreferRule(self, ctx:MatcherParser.PreferRuleContext):
        pass


    # Enter a parse tree produced by MatcherParser#scoreRule.
    def enterScoreRule(self, ctx:MatcherParser.ScoreRuleContext):
        pass

    # Exit a parse tree produced by MatcherParser#scoreRule.
    def exitScoreRule(self, ctx:MatcherParser.ScoreRuleContext):
        pass


    # Enter a parse tree produced by MatcherParser#condition.
    def enterCondition(self, ctx:MatcherParser.ConditionContext):
        pass

    # Exit a parse tree produced by MatcherParser#condition.
    def exitCondition(self, ctx:MatcherParser.ConditionContext):
        pass


    # Enter a parse tree produced by MatcherParser#scoreAction.
    def enterScoreAction(self, ctx:MatcherParser.ScoreActionContext):
        pass

    # Exit a parse tree produced by MatcherParser#scoreAction.
    def exitScoreAction(self, ctx:MatcherParser.ScoreActionContext):
        pass


    # Enter a parse tree produced by MatcherParser#comparator.
    def enterComparator(self, ctx:MatcherParser.ComparatorContext):
        pass

    # Exit a parse tree produced by MatcherParser#comparator.
    def exitComparator(self, ctx:MatcherParser.ComparatorContext):
        pass


    # Enter a parse tree produced by MatcherParser#value.
    def enterValue(self, ctx:MatcherParser.ValueContext):
        pass

    # Exit a parse tree produced by MatcherParser#value.
    def exitValue(self, ctx:MatcherParser.ValueContext):
        pass



del MatcherParser