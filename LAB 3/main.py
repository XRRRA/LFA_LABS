import re


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []  # Tokens will be stored here
        self.current_pos = 0

        # Define keywords, operators, identifiers, etc.
        self.keywords = {'if', 'else', 'while', 'for', 'int', 'float'}
        self.operators = {'+', '-', '*', '/', '=', '<', '>', '==', ':'}
        self.delimiters = {';', '(', ')', '{', '}', ',', "'"}

    def tokenize(self):
        while self.current_pos < len(self.input_text):
            char = self.input_text[self.current_pos]

            if char.isspace():
                self.current_pos += 1  # Skip whitespace

            elif re.match(r'[0-9]', char):  # Numeric literal
                number = self._read_number()
                self.tokens.append(('NUMBER', number))

            elif re.match(r'[a-zA-Z]', char):  # Identifier or keyword
                word = self._read_word()
                if word in self.keywords:
                    self.tokens.append(('KEYWORD', word))
                else:
                    self.tokens.append(('IDENTIFIER', word))

            elif char in self.operators:
                self.tokens.append(('OPERATOR', char))
                self.current_pos += 1

            elif char in self.delimiters:
                self.tokens.append(('DELIMITER', char))
                self.current_pos += 1

            elif char == '"':
                self.current_pos += 1
                string_value = self._read_string()
                self.tokens.append(('STRING', string_value))
            elif char == '#':  # Comment start
                comment = self._read_comment()
                self.tokens.append(('COMMENT', comment))
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
              self.input_text[self.current_pos].isalnum():  # Check for alphanumeric
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


source_code = """
# A simple calculator program

def add(num1, num2):
    # Adds two numbers and returns the result.
    return num1 + num2

def subtract(num1, num2):
    # Subtracts two numbers and returns the result.
    return num1 - num2

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number format. Please try again.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        else:
            print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.") 
"""
lexer = Lexer(source_code)
lexer.tokenize()
print(lexer.tokens)
