from parse.HireVisitor import HireVisitor
from parse.HireParser import HireParser

class HireProcessor(HireVisitor):
    def visitProgram(self, ctx:HireParser.ProgramContext):
        return self.visitChildren(ctx)
    def visitShowTop(self, ctx:HireParser.ShowTopContext):
        return {
            "command": "show_top",
            "number": int(ctx.INT().getText())  
        }

    
    def visitShowConditional(self, ctx:HireParser.ShowConditionalContext):
        return {
            "command": "show_cv_with",
            "condition": self.visit(ctx.condition())  # e.g., {"level": "senior"}
        }
    
    def visitCondition(self, ctx:HireParser.ConditionContext):
        return self.visitChildren(ctx)



    def visitJd(self, ctx:HireParser.JdContext):
        return {
            "command": "jd",
            "requirements": self.visit(ctx.requirements()),
            "preferences": self.visit(ctx.preferences()) if ctx.preferences() else None,
        }
    
        

    def visitRequirements(self, ctx: HireParser.RequirementsContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    def visitPreferences(self, ctx: HireParser.PreferencesContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    

    def visitRequirePosition(self, ctx):
        return self._build_kv("position", ctx)

    def visitRequireLevel(self, ctx):
        return self._build_kv("level", ctx)

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
        return self._build_kv("major", ctx)

    def visitRequireDegree(self, ctx):
        return self._build_kv("degree", ctx)

    def visitRequireGPA(self, ctx):
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return ("gpa", " ".join(tokens))

    def visitRequireExperience(self, ctx):
        return self._build_simple_kv("experience", ctx)

    def visitRequireLanguage(self, ctx):
        return self._build_kv("language", ctx)

    def visitRequireActivites(self, ctx):
        return self._build_simple_kv("activities", ctx)
    
    def visitPosition(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#level.
    def visitLevel(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#degree.
    def visitDegree(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#major.
    def visitMajor(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#tool.
    def visitTool(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#pro_lang.
    def visitPro_lang(self, ctx):
        return ctx.getText()

    # Visit a parse tree produced by HireParser#framework.
    def visitFramework(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#db.
    def visitDb(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireParser#lang.
    def visitLang(self, ctx):
        return ctx.getText()

    # === Utility functions ===


    def _build_simple_kv(self, key, ctx):
        """Skip first child rồi collects mấy tokens qua getText() cho nên in range(1, ...)"""
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        return (key, " ".join(tokens))
    
    def _build_kv(self, key, ctx):
        # """Skip first child rồi collects mấy tokens qua getText() cho nên in range(1, ...)"""
        # tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        # return (key, " ".join(tokens)) # Trả về tuple
        values = []
        for child in ctx.children:
            v = self.visit(child)
            if v is not None:
                values.append(v)
        return (key, " ".join(values))
    
    def _build_list_kv(self, key, ctx):
        # """Nên trả về tuple vì khi final result là dict mà mình nest dict[dict] nó sẽ error"""
        # tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        # return (key, tokens)
        values = []
        for child in ctx.children:
            val = self.visit(child)
            if isinstance(val, str):  # only collect meaningful results
                values.append(val)
<<<<<<< HEAD
        return (key, values)
=======
        return (key, values)
>>>>>>> 78a7718f4ced4b8944551c05325e1c75ce3ca506
