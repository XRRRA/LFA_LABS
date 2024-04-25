from lexer import Lexer
from parser import Parser
from token_type import TokenType

if __name__ == '__main__':
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
