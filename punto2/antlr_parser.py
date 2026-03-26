from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

def parse_antlr(s):
    inp = InputStream(s)
    lexer = ExprLexer(inp)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    parser.expr()
    return True
