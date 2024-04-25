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
        return self.expression()

    def expression(self):
        """ Parse an expression. """
        return self.addition()

    def addition(self):
        """ Handle addition and subtraction. """
        result = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            result = BinOp(left=result, op=op, right=right)

        return result

    def term(self):
        """ Handle multiplication and division. """
        result = self.factor()

        while self.current_token.type in (TokenType.TIMES, TokenType.DIVIDE):
            op = self.current_token
            self.advance()
            right = self.factor()
            result = BinOp(left=result, op=op, right=right)

        return result

    def factor(self):
        """ Handle parentheses and numbers. """
        token = self.current_token

        if token.type == TokenType.INTEGER:
            self.advance()
            return Num(token)
        elif token.type == TokenType.LPAREN:
            self.advance()
            result = self.expression()
            if self.current_token.type != TokenType.RPAREN:
                self.error()
            self.advance()
            return result
        else:
            self.error()
