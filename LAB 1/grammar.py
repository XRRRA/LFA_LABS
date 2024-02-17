import random

from finite_automaton import FiniteAutomaton


class Grammar:
    def __init__(self):
        self.VN = {'S', 'B', 'D'}
        self.VT = {'a', 'b', 'c', 'd'}
        self.P = {
            'S': ['aS', 'bB'],
            'B': ['cB', 'd', 'aD'],
            'D': ['aB', 'b']
        }

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

        # Adding states
        finite_automaton.Q = self.VN.union(self.VT)

        # Adding alphabet
        finite_automaton.Sigma = self.VT

        # Adding transitions
        for non_terminal, productions in self.P.items():
            for production in productions:
                if len(production) > 1:
                    current_state = production[0]
                    next_state = production[1]
                    finite_automaton.delta.setdefault((non_terminal, current_state), set()).add(next_state)

        # Adding initial state
        finite_automaton.q0 = 'S'

        # Adding accepting states
        finite_automaton.F = {'S'}

        return finite_automaton







