from parse.HireXVisitor import HireXVisitor
from parse.HireXParser import HireXParser

class HireXProcessor(HireXVisitor):
    def visitProgram(self, ctx:HireXParser.ProgramContext):
        return self.visitChildren(ctx)
    
    def visitShowConditional(self, ctx:HireXParser.ShowConditionalContext):
        return {
            "command": "show_cv_with",
            "condition": self.visit(ctx.condition())  # e.g., {"level": "senior"}
        }
    
    def visitCondition(self, ctx:HireXParser.ConditionContext):
        return self.visitChildren(ctx)


    def visitJd(self, ctx:HireXParser.JdContext):
        return {
            "command": "jd",
            "requirements": self.visit(ctx.requirements()),
            "preferences": self.visit(ctx.preferences()) if ctx.preferences() else None,
        }
    
        

    def visitRequirements(self, ctx: HireXParser.RequirementsContext):
        return dict(
        filter(
            lambda pair: isinstance(pair, tuple),
            map(lambda child: self.visit(child), ctx.children)
        )
    )

    def visitPreferences(self, ctx: HireXParser.PreferencesContext):
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
        tokens = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount())]
        # Look for the first number in the tokens
        for token in tokens:
            if token.isdigit():
                return ("experience", f"{token}")
        return ("experience", "0") 
            

    def visitRequireLanguage(self, ctx):
        return self._build_kv("language", ctx)

    def visitRequireActivites(self, ctx):
        return self._build_simple_kv("activities", ctx)
    
    def visitRequireName(self, ctx):
        return self._build_simple_kv("name", ctx)
    
    def visitPosition(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#level.
    def visitLevel(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#degree.
    def visitDegree(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#major.
    def visitMajor(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#tool.
    def visitTool(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#pro_lang.
    def visitProLang(self, ctx):
        return ctx.getText()

    # Visit a parse tree produced by HireXParser#framework.
    def visitFramework(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#db.
    def visitDb(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by HireXParser#lang.
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
        return (key, values)