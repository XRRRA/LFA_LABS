# finite_automaton.py
from lib2to3.pgen2.grammar import Grammar


class FiniteAutomaton:
    def __init__(self):
        self.Q = set()
        self.Sigma = set()
        self.delta = set()
        self.q0 = None
        self.F = set()

    def string_belongs_to_language(self, input_string):
        current_state = self.q0
        for symbol in input_string:
            next_states = {next_state for (state, input_symbol, next_state) in self.delta
                           if state == current_state and input_symbol == symbol}
            if not next_states:
                return False
            current_state = next_states.pop()
        return current_state in self.F

    def to_regular_grammar(self):
        regular_grammar = Grammar()
        regular_grammar.VN = self.Q
        regular_grammar.VT = self.Sigma
        regular_grammar.P = {}

        for state in self.Q:
            regular_grammar.P[state] = []

        for transition in self.delta:
            if transition[2] != 'X':
                next_state_str = ''.join(transition[2])  # Convert tuple to string
                regular_grammar.P[transition[0]].append(transition[1] + next_state_str)  # Concatenate strings

        return regular_grammar

    def is_deterministic(self):
        for state in self.Q:
            for symbol in self.Sigma:
                next_states = {next_state for (_, input_symbol, next_state) in self.delta
                               if _ == state and input_symbol == symbol}
                if len(next_states) > 1:
                    return False
        return True

    def to_deterministic_finite_automaton(self):
        dfa = FiniteAutomaton()
        dfa.Sigma = self.Sigma
        dfa.q0 = frozenset([self.q0])  # Initial state is the epsilon closure of the original initial state
        dfa.F = set()
        dfa.Q = set()  # Initialize set of states
        dfa.delta = set()

        # Compute epsilon closure of a state in the NFA
        def epsilon_closure(state):
            closure = set(state)
            stack = list(state)
            while stack:
                currentState = stack.pop()
                for (_, input_symbol, nextState) in self.delta:
                    if currentState == nextState and input_symbol == 'ε' and nextState not in closure:
                        closure.add(nextState)
                        stack.append(nextState)
            return frozenset(closure)

        # Initialize unprocessed states with the epsilon closure of the initial state
        unprocessed_states = [dfa.q0]
        dfa.Q.add(dfa.q0)

        # Explore states of the DFA using subset construction algorithm
        while unprocessed_states:
            current_state = unprocessed_states.pop(0)
            for symbol in dfa.Sigma:
                next_state = set()
                for state in current_state:
                    # Find next states according to the NFA transitions and epsilon closures
                    next_state |= {next_state for (_, input_symbol, next_state) in self.delta
                                   if state in current_state and input_symbol == symbol}
                next_state_closure = epsilon_closure(next_state)
                if next_state_closure:
                    dfa.delta.add((current_state, symbol, next_state_closure))
                    if next_state_closure not in dfa.Q:
                        dfa.Q.add(next_state_closure)
                        unprocessed_states.append(next_state_closure)
                    if any(state in self.F for state in next_state_closure):
                        dfa.F.add(next_state_closure)

        return dfa



