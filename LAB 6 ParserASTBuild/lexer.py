import re
from token_type import TokenType


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.current_pos = 0

        # Define keywords, operators, identifiers, etc.
        self.keywords = {'if', 'else', 'while', 'for', 'int', 'float'}
        self.operators = {'+', '-', '*', '/', '=', '<', '>', '==', ':'}
        self.delimiters = {';', '(', ')', '{', '}', ',', "'"}

    def tokenize(self):
        while self.current_pos < len(self.input_text):
            char = self.input_text[self.current_pos]

            if char.isspace():
                self.current_pos += 1

            elif re.match(r'[0-9]', char):
                number = self._read_number()
                self.tokens.append((TokenType.NUMBER, number))

            elif re.match(r'[a-zA-Z]', char):
                word = self._read_word()
                if word in self.keywords:
                    self.tokens.append((TokenType.KEYWORD, word))
                else:
                    self.tokens.append((TokenType.IDENTIFIER, word))

            elif char in self.operators:
                self.tokens.append((TokenType.OPERATOR, char))
                self.current_pos += 1

            elif char in self.delimiters:
                self.tokens.append((TokenType.DELIMITER, char))
                self.current_pos += 1

            elif char == '"':
                self.current_pos += 1
                string_value = self._read_string()
                self.tokens.append((TokenType.STRING, string_value))
            elif char == '#':
                comment = self._read_comment()
                self.tokens.append((TokenType.COMMENT, comment))
            else:
                raise Exception(f"Unknown character: '{char}' at position {self.current_pos}")

    def _read_number(self):
        number = ''
        while self.current_pos < len(self.input_text) and \
                (self.input_text[self.current_pos].isdigit() or self.input_text[self.current_pos] == '.'):
            number += self.input_text[self.current_pos]
            self.current_pos += 1
        return number

    def _read_word(self):
        word = ''
        while self.current_pos < len(self.input_text) and \
              self.input_text[self.current_pos].isalnum():
            word += self.input_text[self.current_pos]
            self.current_pos += 1
        return word

    def _read_string(self):
        string_value = ''
        while self.current_pos < len(self.input_text) and self.input_text[self.current_pos] != '"':
            string_value += self.input_text[self.current_pos]
            self.current_pos += 1
        if self.current_pos == len(self.input_text):
            raise Exception("Unterminated string!")
        self.current_pos += 1
        return string_value

    def _read_comment(self):
        comment = ''
        while self.current_pos < len(self.input_text) and self.input_text[self.current_pos] != '\n':
            comment += self.input_text[self.current_pos]
            self.current_pos += 1
        return comment
