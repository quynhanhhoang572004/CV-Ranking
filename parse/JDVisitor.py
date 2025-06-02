# Generated from JD.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JDParser import JDParser
else:
    from JDParser import JDParser

# This class defines a complete generic visitor for a parse tree produced by JDParser.

class JDVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JDParser#program.
    def visitProgram(self, ctx:JDParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requirements.
    def visitRequirements(self, ctx:JDParser.RequirementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#preferences.
    def visitPreferences(self, ctx:JDParser.PreferencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requirePosition.
    def visitRequirePosition(self, ctx:JDParser.RequirePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireLevel.
    def visitRequireLevel(self, ctx:JDParser.RequireLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireTechnicalSkills.
    def visitRequireTechnicalSkills(self, ctx:JDParser.RequireTechnicalSkillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireTools.
    def visitRequireTools(self, ctx:JDParser.RequireToolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireProLang.
    def visitRequireProLang(self, ctx:JDParser.RequireProLangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireFrameworks.
    def visitRequireFrameworks(self, ctx:JDParser.RequireFrameworksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireDB.
    def visitRequireDB(self, ctx:JDParser.RequireDBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireEducation.
    def visitRequireEducation(self, ctx:JDParser.RequireEducationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireMajor.
    def visitRequireMajor(self, ctx:JDParser.RequireMajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireDegree.
    def visitRequireDegree(self, ctx:JDParser.RequireDegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireGPA.
    def visitRequireGPA(self, ctx:JDParser.RequireGPAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireLanguage.
    def visitRequireLanguage(self, ctx:JDParser.RequireLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireExperience.
    def visitRequireExperience(self, ctx:JDParser.RequireExperienceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireActivites.
    def visitRequireActivites(self, ctx:JDParser.RequireActivitesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JDParser#requireReferences.
    def visitRequireReferences(self, ctx:JDParser.RequireReferencesContext):
        return self.visitChildren(ctx)



del JDParser