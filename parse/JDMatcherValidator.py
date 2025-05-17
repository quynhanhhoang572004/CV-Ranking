from parse.JDMatcherVisitor import JDMatcherVisitor
from parse.JDMatcherParser import JDMatcherParser

class JDMatcherValidator(JDMatcherVisitor):
    def visitProgram(self, ctx: JDMatcherParser.ProgramContext):
        if ctx.listCV():
            return self.visitListCV(ctx.listCV())
        elif ctx.jd():
            return self.visitJD(ctx.jd())
        elif ctx.show_X_best():
            return self.visitShow_X_best(ctx.show_X_best())
        elif ctx.showConditional():
            return self.visitShowConditional(ctx.showConditional())
        else:
            return {"error": "Unknown command"}
        

    def visitListCV(self, ctx: JDMatcherParser.ListCVContext):
        return {
            "command": "list_cvs",
            "position": ctx.POSITION().getText()
        }

    def visitShow_X_best(self, ctx: JDMatcherParser.Show_X_bestContext):
        return {
            "command": "show_top",
            "count": int(ctx.INT().getText()),
            "position": ctx.POSITION().getText()
        }
    
    def visitShowConditional(self, ctx: JDMatcherParser.ShowConditionalContext):
        conditions = None
        position = ctx.requirePosition().POSITION().getText()

        for child in ctx.children:
            if  hasattr(child, 'accept'):
                conditions = self.visit(child)
        
        return {
            "command": "show_cv_with",
            "position": position,
            "conditions": conditions
        }
    
    def visitJD(self, ctx: JDMatcherParser.JdContext):
        return {
            "command": "jd",
            "requirements": self.visit(ctx.requirements()),
            "preferences": self.visit(ctx.preferences()) if ctx.preferences() else None,
        }
    def visitRequirements(self, ctx: JDMatcherParser.RequirementsContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    def visitPreferences(self, ctx: JDMatcherParser.PreferencesContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    def visitRequirePosition(self, ctx):
        return self._build_simple_kv("Position", ctx)

    def visitRequireLevel(self, ctx):
        return self._build_simple_kv("Level", ctx)

    def visitRequireTechnicalSkills(self, ctx):
        return self.visitChildren(ctx)

    def visitRequireTools(self, ctx):
        return self._build_list_kv("Tools", ctx)

    def visitRequireProLang(self, ctx):
        return self._build_list_kv("ProgrammingLanguages", ctx)

    def visitRequireFrameworks(self, ctx):
        return self._build_list_kv("Frameworks", ctx)

    def visitRequireDB(self, ctx):
        return self._build_list_kv("DatabasesAndCloud", ctx)

    def visitRequireEducation(self, ctx):
        return self.visitChildren(ctx)

    def visitRequireMajor(self, ctx):
        return self._build_simple_kv("Major", ctx)

    def visitRequireDegree(self, ctx):
        return self._build_simple_kv("Degree", ctx)

    def visitRequireGPA(self, ctx):
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return ("GPA", " ".join(tokens))

    def visitRequireExperience(self, ctx):
        return self._build_simple_kv("Experience", ctx)

    def visitRequireLanguage(self, ctx):
        return self._build_simple_kv("Language", ctx)

    def visitRequireActivites(self, ctx):
        return self._build_simple_kv("Activities", ctx)

    def visitRequireReferences(self, ctx):
        return self._build_simple_kv("References", ctx)

    # === Utility functions ===

    

    def _build_simple_kv(self, key, ctx):
        """Skip first child rồi collects mấy tokens qua getText() cho nên in range(1, ...)"""
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return (key, " ".join(tokens)) # Trả về tuple

    def _build_list_kv(self, key, ctx):
        """Nên trả về tuple vì khi final result là dict mà mình nest dict[dict] nó sẽ error"""
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return (key, tokens)
