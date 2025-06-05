# Generated from HireX.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HireXParser import HireXParser
else:
    from HireXParser import HireXParser

# This class defines a complete generic visitor for a parse tree produced by HireXParser.

class HireXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HireXParser#program.
    def visitProgram(self, ctx:HireXParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#showConditional.
    def visitShowConditional(self, ctx:HireXParser.ShowConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#condition.
    def visitCondition(self, ctx:HireXParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#jd.
    def visitJd(self, ctx:HireXParser.JdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requirements.
    def visitRequirements(self, ctx:HireXParser.RequirementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#preferences.
    def visitPreferences(self, ctx:HireXParser.PreferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requirePosition.
    def visitRequirePosition(self, ctx:HireXParser.RequirePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireLevel.
    def visitRequireLevel(self, ctx:HireXParser.RequireLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireTechnicalSkills.
    def visitRequireTechnicalSkills(self, ctx:HireXParser.RequireTechnicalSkillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireTools.
    def visitRequireTools(self, ctx:HireXParser.RequireToolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireProLang.
    def visitRequireProLang(self, ctx:HireXParser.RequireProLangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireFrameworks.
    def visitRequireFrameworks(self, ctx:HireXParser.RequireFrameworksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireDB.
    def visitRequireDB(self, ctx:HireXParser.RequireDBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireEducation.
    def visitRequireEducation(self, ctx:HireXParser.RequireEducationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireMajor.
    def visitRequireMajor(self, ctx:HireXParser.RequireMajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireDegree.
    def visitRequireDegree(self, ctx:HireXParser.RequireDegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireGPA.
    def visitRequireGPA(self, ctx:HireXParser.RequireGPAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireLanguage.
    def visitRequireLanguage(self, ctx:HireXParser.RequireLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireExperience.
    def visitRequireExperience(self, ctx:HireXParser.RequireExperienceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireActivites.
    def visitRequireActivites(self, ctx:HireXParser.RequireActivitesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#requireName.
    def visitRequireName(self, ctx:HireXParser.RequireNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#position.
    def visitPosition(self, ctx:HireXParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#level.
    def visitLevel(self, ctx:HireXParser.LevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#degree.
    def visitDegree(self, ctx:HireXParser.DegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#major.
    def visitMajor(self, ctx:HireXParser.MajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#tool.
    def visitTool(self, ctx:HireXParser.ToolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#proLang.
    def visitProLang(self, ctx:HireXParser.ProLangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#framework.
    def visitFramework(self, ctx:HireXParser.FrameworkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#db.
    def visitDb(self, ctx:HireXParser.DbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireXParser#lang.
    def visitLang(self, ctx:HireXParser.LangContext):
        return self.visitChildren(ctx)



del HireXParser