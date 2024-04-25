from lexer import Lexer
from parser import Parser
from my_ast import print_ast


text = "12 + 34 - 56 + 78"
lexer = Lexer(text)
lexer.tokenize()
parser = Parser(lexer)
ast = parser.parse()

print("Tokens:")
for token in lexer.tokens:
    print(token)

print("\nAST:")
print_ast(ast)
