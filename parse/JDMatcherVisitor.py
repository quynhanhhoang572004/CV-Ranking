# Generated from JDMatcher.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JDMatcherParser import JDMatcherParser
else:
    from JDMatcherParser import JDMatcherParser

# This class defines a complete generic visitor for a parse tree produced by JDMatcherParser.

class JDMatcherVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JDMatcherParser#program.
    def visitProgram(self, ctx:JDMatcherParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#listCV.
    def visitListCV(self, ctx:JDMatcherParser.ListCVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#showConditional.
    def visitShowConditional(self, ctx:JDMatcherParser.ShowConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#show_X_best.
    def visitShow_X_best(self, ctx:JDMatcherParser.Show_X_bestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#jd.
    def visitJd(self, ctx:JDMatcherParser.JdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requirements.
    def visitRequirements(self, ctx:JDMatcherParser.RequirementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#preferences.
    def visitPreferences(self, ctx:JDMatcherParser.PreferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requirePosition.
    def visitRequirePosition(self, ctx:JDMatcherParser.RequirePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireLevel.
    def visitRequireLevel(self, ctx:JDMatcherParser.RequireLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireTechnicalSkills.
    def visitRequireTechnicalSkills(self, ctx:JDMatcherParser.RequireTechnicalSkillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireTools.
    def visitRequireTools(self, ctx:JDMatcherParser.RequireToolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireProLang.
    def visitRequireProLang(self, ctx:JDMatcherParser.RequireProLangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireFrameworks.
    def visitRequireFrameworks(self, ctx:JDMatcherParser.RequireFrameworksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireDB.
    def visitRequireDB(self, ctx:JDMatcherParser.RequireDBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireEducation.
    def visitRequireEducation(self, ctx:JDMatcherParser.RequireEducationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireMajor.
    def visitRequireMajor(self, ctx:JDMatcherParser.RequireMajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireDegree.
    def visitRequireDegree(self, ctx:JDMatcherParser.RequireDegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireGPA.
    def visitRequireGPA(self, ctx:JDMatcherParser.RequireGPAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireExperience.
    def visitRequireExperience(self, ctx:JDMatcherParser.RequireExperienceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireLanguage.
    def visitRequireLanguage(self, ctx:JDMatcherParser.RequireLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireActivites.
    def visitRequireActivites(self, ctx:JDMatcherParser.RequireActivitesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDMatcherParser#requireReferences.
    def visitRequireReferences(self, ctx:JDMatcherParser.RequireReferencesContext):
        return self.visitChildren(ctx)



del JDMatcherParser