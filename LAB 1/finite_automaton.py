class FiniteAutomaton:
    def __init__(self):
        self.Q = set()  # Set of states
        self.Sigma = set()  # Input alphabet
        self.delta = dict()  # Transition function
        self.q0 = None  # Initial state
        self.F = set()  # Set of accepting states

    def string_belongs_to_language(self, input_string):
        current_state = self.q0
        for symbol in input_string:
            if (current_state, symbol) not in self.delta:
                return False  # No transition defined for current state and input symbol
            next_state = self.delta[(current_state, symbol)]
            current_state = next_state
        return current_state in self.F  # Check if final state is one of the accepting states
