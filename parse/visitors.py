from parse.cv_scanVisitor import cv_scanVisitor

class MyVisitor(cv_scanVisitor):
    def visitHeading(self, ctx):
        return {"heading": ctx.getText().strip("# ").strip()}

    def visitParagraph(self, ctx):
        return {"paragraph": ctx.getText().strip()}
