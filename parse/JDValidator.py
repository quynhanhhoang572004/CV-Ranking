from parse.JDVisitor import JDVisitor
from parse.JDParser import JDParser

class JDValidator(JDVisitor):
    def visitProgram(self, ctx: JDParser.ProgramContext):
        return {
            "requirements": self.visit(ctx.requirements()),
            "preferences": self.visit(ctx.preferences()) if ctx.preferences() else None,
        }

    def visitRequirements(self, ctx: JDParser.RequirementsContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    def visitPreferences(self, ctx: JDParser.PreferencesContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    

    def visitRequirePosition(self, ctx):
        return self._build_simple_kv("position", ctx)

    def visitRequireLevel(self, ctx):
        return self._build_simple_kv("level", ctx)

    def visitRequireTechnicalSkills(self, ctx):
        return (
        "technical skills",
        dict(
            filter(
                lambda pair: isinstance(pair, tuple),
                map(lambda child: self.visit(child), ctx.children)
            )
        )
        )
    

    def visitRequireTools(self, ctx):
        return self._build_list_kv("tools", ctx)

    def visitRequireProLang(self, ctx):
        return self._build_list_kv("programmingLanguages", ctx)

    def visitRequireFrameworks(self, ctx):
        return self._build_list_kv("frameworksLibraries", ctx)

    def visitRequireDB(self, ctx):
        return self._build_list_kv("databasescloudServices", ctx)

    def visitRequireEducation(self, ctx):
        return ("education", (dict(filter(lambda pair: isinstance(pair,tuple), map(lambda child: self.visit(child), ctx.children)))))

    def visitRequireMajor(self, ctx):
        return self._build_simple_kv("major", ctx)

    def visitRequireDegree(self, ctx):
        return self._build_simple_kv("degree", ctx)

    def visitRequireGPA(self, ctx):
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return ("gpa", " ".join(tokens))

    def visitRequireExperience(self, ctx):
        return self._build_simple_kv("experience", ctx)

    def visitRequireLanguage(self, ctx):
        return self._build_simple_kv("language", ctx)

    def visitRequireActivites(self, ctx):
        return self._build_simple_kv("activities", ctx)

    def visitRequireReferences(self, ctx):
        return self._build_simple_kv("references", ctx)

    # === Utility functions ===

    def _build_simple_kv(self, key, ctx):
        """Skip first child rồi collects mấy tokens qua getText() cho nên in range(1, ...)"""
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return (key, " ".join(tokens)) # Trả về tuple

    def _build_list_kv(self, key, ctx):
        """Nên trả về tuple vì khi final result là dict mà mình nest dict[dict] nó sẽ error"""
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return (key, tokens)
