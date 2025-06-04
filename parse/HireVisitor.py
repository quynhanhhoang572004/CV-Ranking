<<<<<<< HEAD
# Generated from grammars/Hire.g4 by ANTLR 4.9.2
=======
# Generated from Hire.g4 by ANTLR 4.9.2
>>>>>>> 87c567f62372deea8f99ccea0a616120727943e7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HireParser import HireParser
else:
    from HireParser import HireParser

# This class defines a complete generic visitor for a parse tree produced by HireParser.

class HireVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HireParser#program.
    def visitProgram(self, ctx:HireParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#showTop.
    def visitShowTop(self, ctx:HireParser.ShowTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#showConditional.
    def visitShowConditional(self, ctx:HireParser.ShowConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#condition.
    def visitCondition(self, ctx:HireParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#jd.
    def visitJd(self, ctx:HireParser.JdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requirements.
    def visitRequirements(self, ctx:HireParser.RequirementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#preferences.
    def visitPreferences(self, ctx:HireParser.PreferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requirePosition.
    def visitRequirePosition(self, ctx:HireParser.RequirePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireLevel.
    def visitRequireLevel(self, ctx:HireParser.RequireLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireTechnicalSkills.
    def visitRequireTechnicalSkills(self, ctx:HireParser.RequireTechnicalSkillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireTools.
    def visitRequireTools(self, ctx:HireParser.RequireToolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireProLang.
    def visitRequireProLang(self, ctx:HireParser.RequireProLangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireFrameworks.
    def visitRequireFrameworks(self, ctx:HireParser.RequireFrameworksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireDB.
    def visitRequireDB(self, ctx:HireParser.RequireDBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireEducation.
    def visitRequireEducation(self, ctx:HireParser.RequireEducationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireMajor.
    def visitRequireMajor(self, ctx:HireParser.RequireMajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireDegree.
    def visitRequireDegree(self, ctx:HireParser.RequireDegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireGPA.
    def visitRequireGPA(self, ctx:HireParser.RequireGPAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireLanguage.
    def visitRequireLanguage(self, ctx:HireParser.RequireLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireExperience.
    def visitRequireExperience(self, ctx:HireParser.RequireExperienceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#requireActivites.
    def visitRequireActivites(self, ctx:HireParser.RequireActivitesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#position.
    def visitPosition(self, ctx:HireParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#level.
    def visitLevel(self, ctx:HireParser.LevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#degree.
    def visitDegree(self, ctx:HireParser.DegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#major.
    def visitMajor(self, ctx:HireParser.MajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#tool.
    def visitTool(self, ctx:HireParser.ToolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#pro_lang.
    def visitPro_lang(self, ctx:HireParser.Pro_langContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#framework.
    def visitFramework(self, ctx:HireParser.FrameworkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#db.
    def visitDb(self, ctx:HireParser.DbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HireParser#lang.
    def visitLang(self, ctx:HireParser.LangContext):
        return self.visitChildren(ctx)



del HireParser