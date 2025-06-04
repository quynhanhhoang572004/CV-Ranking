# Generated from grammars/Hire.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HireParser import HireParser
else:
    from HireParser import HireParser

# This class defines a complete listener for a parse tree produced by HireParser.
class HireListener(ParseTreeListener):

    # Enter a parse tree produced by HireParser#program.
    def enterProgram(self, ctx:HireParser.ProgramContext):
        pass

    # Exit a parse tree produced by HireParser#program.
    def exitProgram(self, ctx:HireParser.ProgramContext):
        pass


    # Enter a parse tree produced by HireParser#showTop.
    def enterShowTop(self, ctx:HireParser.ShowTopContext):
        pass

    # Exit a parse tree produced by HireParser#showTop.
    def exitShowTop(self, ctx:HireParser.ShowTopContext):
        pass


    # Enter a parse tree produced by HireParser#showConditional.
    def enterShowConditional(self, ctx:HireParser.ShowConditionalContext):
        pass

    # Exit a parse tree produced by HireParser#showConditional.
    def exitShowConditional(self, ctx:HireParser.ShowConditionalContext):
        pass


    # Enter a parse tree produced by HireParser#condition.
    def enterCondition(self, ctx:HireParser.ConditionContext):
        pass

    # Exit a parse tree produced by HireParser#condition.
    def exitCondition(self, ctx:HireParser.ConditionContext):
        pass


    # Enter a parse tree produced by HireParser#jd.
    def enterJd(self, ctx:HireParser.JdContext):
        pass

    # Exit a parse tree produced by HireParser#jd.
    def exitJd(self, ctx:HireParser.JdContext):
        pass


    # Enter a parse tree produced by HireParser#requirements.
    def enterRequirements(self, ctx:HireParser.RequirementsContext):
        pass

    # Exit a parse tree produced by HireParser#requirements.
    def exitRequirements(self, ctx:HireParser.RequirementsContext):
        pass


    # Enter a parse tree produced by HireParser#preferences.
    def enterPreferences(self, ctx:HireParser.PreferencesContext):
        pass

    # Exit a parse tree produced by HireParser#preferences.
    def exitPreferences(self, ctx:HireParser.PreferencesContext):
        pass


    # Enter a parse tree produced by HireParser#requirePosition.
    def enterRequirePosition(self, ctx:HireParser.RequirePositionContext):
        pass

    # Exit a parse tree produced by HireParser#requirePosition.
    def exitRequirePosition(self, ctx:HireParser.RequirePositionContext):
        pass


    # Enter a parse tree produced by HireParser#requireLevel.
    def enterRequireLevel(self, ctx:HireParser.RequireLevelContext):
        pass

    # Exit a parse tree produced by HireParser#requireLevel.
    def exitRequireLevel(self, ctx:HireParser.RequireLevelContext):
        pass


    # Enter a parse tree produced by HireParser#requireTechnicalSkills.
    def enterRequireTechnicalSkills(self, ctx:HireParser.RequireTechnicalSkillsContext):
        pass

    # Exit a parse tree produced by HireParser#requireTechnicalSkills.
    def exitRequireTechnicalSkills(self, ctx:HireParser.RequireTechnicalSkillsContext):
        pass


    # Enter a parse tree produced by HireParser#requireTools.
    def enterRequireTools(self, ctx:HireParser.RequireToolsContext):
        pass

    # Exit a parse tree produced by HireParser#requireTools.
    def exitRequireTools(self, ctx:HireParser.RequireToolsContext):
        pass


    # Enter a parse tree produced by HireParser#requireProLang.
    def enterRequireProLang(self, ctx:HireParser.RequireProLangContext):
        pass

    # Exit a parse tree produced by HireParser#requireProLang.
    def exitRequireProLang(self, ctx:HireParser.RequireProLangContext):
        pass


    # Enter a parse tree produced by HireParser#requireFrameworks.
    def enterRequireFrameworks(self, ctx:HireParser.RequireFrameworksContext):
        pass

    # Exit a parse tree produced by HireParser#requireFrameworks.
    def exitRequireFrameworks(self, ctx:HireParser.RequireFrameworksContext):
        pass


    # Enter a parse tree produced by HireParser#requireDB.
    def enterRequireDB(self, ctx:HireParser.RequireDBContext):
        pass

    # Exit a parse tree produced by HireParser#requireDB.
    def exitRequireDB(self, ctx:HireParser.RequireDBContext):
        pass


    # Enter a parse tree produced by HireParser#requireEducation.
    def enterRequireEducation(self, ctx:HireParser.RequireEducationContext):
        pass

    # Exit a parse tree produced by HireParser#requireEducation.
    def exitRequireEducation(self, ctx:HireParser.RequireEducationContext):
        pass


    # Enter a parse tree produced by HireParser#requireMajor.
    def enterRequireMajor(self, ctx:HireParser.RequireMajorContext):
        pass

    # Exit a parse tree produced by HireParser#requireMajor.
    def exitRequireMajor(self, ctx:HireParser.RequireMajorContext):
        pass


    # Enter a parse tree produced by HireParser#requireDegree.
    def enterRequireDegree(self, ctx:HireParser.RequireDegreeContext):
        pass

    # Exit a parse tree produced by HireParser#requireDegree.
    def exitRequireDegree(self, ctx:HireParser.RequireDegreeContext):
        pass


    # Enter a parse tree produced by HireParser#requireGPA.
    def enterRequireGPA(self, ctx:HireParser.RequireGPAContext):
        pass

    # Exit a parse tree produced by HireParser#requireGPA.
    def exitRequireGPA(self, ctx:HireParser.RequireGPAContext):
        pass


    # Enter a parse tree produced by HireParser#requireLanguage.
    def enterRequireLanguage(self, ctx:HireParser.RequireLanguageContext):
        pass

    # Exit a parse tree produced by HireParser#requireLanguage.
    def exitRequireLanguage(self, ctx:HireParser.RequireLanguageContext):
        pass


    # Enter a parse tree produced by HireParser#requireExperience.
    def enterRequireExperience(self, ctx:HireParser.RequireExperienceContext):
        pass

    # Exit a parse tree produced by HireParser#requireExperience.
    def exitRequireExperience(self, ctx:HireParser.RequireExperienceContext):
        pass


    # Enter a parse tree produced by HireParser#requireActivites.
    def enterRequireActivites(self, ctx:HireParser.RequireActivitesContext):
        pass

    # Exit a parse tree produced by HireParser#requireActivites.
    def exitRequireActivites(self, ctx:HireParser.RequireActivitesContext):
        pass


    # Enter a parse tree produced by HireParser#position.
    def enterPosition(self, ctx:HireParser.PositionContext):
        pass

    # Exit a parse tree produced by HireParser#position.
    def exitPosition(self, ctx:HireParser.PositionContext):
        pass


    # Enter a parse tree produced by HireParser#level.
    def enterLevel(self, ctx:HireParser.LevelContext):
        pass

    # Exit a parse tree produced by HireParser#level.
    def exitLevel(self, ctx:HireParser.LevelContext):
        pass


    # Enter a parse tree produced by HireParser#degree.
    def enterDegree(self, ctx:HireParser.DegreeContext):
        pass

    # Exit a parse tree produced by HireParser#degree.
    def exitDegree(self, ctx:HireParser.DegreeContext):
        pass


    # Enter a parse tree produced by HireParser#major.
    def enterMajor(self, ctx:HireParser.MajorContext):
        pass

    # Exit a parse tree produced by HireParser#major.
    def exitMajor(self, ctx:HireParser.MajorContext):
        pass


    # Enter a parse tree produced by HireParser#tool.
    def enterTool(self, ctx:HireParser.ToolContext):
        pass

    # Exit a parse tree produced by HireParser#tool.
    def exitTool(self, ctx:HireParser.ToolContext):
        pass


    # Enter a parse tree produced by HireParser#pro_lang.
    def enterPro_lang(self, ctx:HireParser.Pro_langContext):
        pass

    # Exit a parse tree produced by HireParser#pro_lang.
    def exitPro_lang(self, ctx:HireParser.Pro_langContext):
        pass


    # Enter a parse tree produced by HireParser#framework.
    def enterFramework(self, ctx:HireParser.FrameworkContext):
        pass

    # Exit a parse tree produced by HireParser#framework.
    def exitFramework(self, ctx:HireParser.FrameworkContext):
        pass


    # Enter a parse tree produced by HireParser#db.
    def enterDb(self, ctx:HireParser.DbContext):
        pass

    # Exit a parse tree produced by HireParser#db.
    def exitDb(self, ctx:HireParser.DbContext):
        pass


    # Enter a parse tree produced by HireParser#lang.
    def enterLang(self, ctx:HireParser.LangContext):
        pass

    # Exit a parse tree produced by HireParser#lang.
    def exitLang(self, ctx:HireParser.LangContext):
        pass



del HireParser