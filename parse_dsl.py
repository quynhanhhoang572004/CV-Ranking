from antlr4 import *
from parse.MatcherLexer import MatcherLexer
from parse.MatcherParser import MatcherParser
from parse.MatcherListener import MatcherListener

class Rule:
    def __init__(self, type, **kwargs):
        self.type = type
        self.details = kwargs
    def __repr__(self):
        return f"{self.type.upper()}: {self.details}"
    

class DSLListener(MatcherListener):
    def __init__(self):
        self.rules = []

    def enterRequireRule(self, ctx):
        skill = ctx.STRING().getText().strip('"')
        self.rules.append(Rule("require", skill=skill))

    def enterPreferRule(self, ctx):
        skill = ctx.STRING().getText().strip('"')
        weight = int(ctx.INT().getText())
        self.rules.append(Rule("prefer", skill=skill, weight=weight))

    def enterScoreRule(self, ctx):
        cond = ctx.condition()
        left = f"{cond.IDENTIFIER(0).getText()}.{cond.IDENTIFIER(1).getText()}"
        op = cond.comparator().getText()
        val = cond.value().getText().strip('"') if cond.value().STRING() else int(cond.value().INT().getText())
        delta = int(ctx.scoreAction().INT().getText())
        sign = ctx.scoreAction().getText()[6]  # '+' or '-'
        score = delta if sign == '+' else -delta
        self.rules.append(Rule("score", condition=(left, op, val), delta=score))


def parse_dsl(dsl_code):
    input_stream = InputStream(dsl_code)
    lexer = MatcherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MatcherParser(stream)
    tree = parser.matchBlock()

    listener = DSLListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rules

# Example use
if __name__ == "__main__":
    dsl = '''
    match {
      require skill "Python"
      prefer skill "Machine Learning" weight 2
      if experience.years >= 3 then score +5
      if education.degree == "PhD" then score +10
    }
    '''
    rules = parse_dsl(dsl)
    for r in rules:
        print(r)
    

