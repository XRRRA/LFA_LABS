# grammar.py
import random

from finite_automaton import FiniteAutomaton


class Grammar:
    def __init__(self):
        self.VN = set()
        self.VT = set()
        self.P = {}

    def generate_string(self):
        generated_strings = []
        for _ in range(5):
            generated_string = self._generate_string_helper('S', '')
            generated_strings.append(generated_string)
        return generated_strings

    def _generate_string_helper(self, symbol, current_string):
        if symbol in self.VT:
            return current_string + symbol
        else:
            productions = self.P[symbol]
            chosen_production = random.choice(productions)
            for s in chosen_production:
                current_string = self._generate_string_helper(s, current_string)
            return current_string

    def to_finite_automaton(self):
        finite_automaton = FiniteAutomaton()

        finite_automaton.Q = self.VN.union(self.VT)
        finite_automaton.Sigma = self.VT
        finite_automaton.delta = set()

        for non_terminal, productions in self.P.items():
            for production in productions:
                if len(production) > 1:
                    current_state = production[0]
                    next_state = production[1]
                    finite_automaton.delta.add((non_terminal, current_state, next_state))
                else:
                    # Handle terminal elements
                    if non_terminal in finite_automaton.F:
                        finite_automaton.delta.add((non_terminal, production, 'X'))
                    else:
                        # Update terminal values
                        if production == 'b':
                            finite_automaton.delta.add((non_terminal, production, 'X'))
                        elif production == 'd':
                            finite_automaton.delta.add((non_terminal, production, 'X'))
                        else:
                            finite_automaton.delta.add((non_terminal, production, production))

        finite_automaton.q0 = 'S'
        finite_automaton.F = {'X'}

        return finite_automaton

    def check_grammar_type(self):
        start_symbol = None
        has_epsilon = False
        for non_terminal, productions in self.P.items():
            if not start_symbol:
                start_symbol = non_terminal
            for production in productions:
                if 'ε' in production:
                    has_epsilon = True
                if len(production) > 2:
                    return "Type-0 (Unrestricted)"
                if len(production) == 2:
                    if production[0] in self.VN and production[1] in self.VT:
                        return "Type-1 (Context-Sensitive)"
                if len(production) == 1:
                    if production[0] in self.VT:
                        return "Type-3 (Regular)"
        if start_symbol and not has_epsilon:
            return "Type-2 (Context-Free)"
        return "Type-0 (Unrestricted)"
