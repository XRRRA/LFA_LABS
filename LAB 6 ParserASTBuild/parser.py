from token_type import *
from my_token import *
from my_ast import *


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF, None)

    def error(self):
        raise Exception('Invalid syntax')

    def parse(self):
        if self.current_token.type == TokenType.EOF:
            return None

        left = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            left = BinOp(left=left, op=op, right=right)
        return left

    def term(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.advance()
            return Num(token)
        else:
            self.error()
