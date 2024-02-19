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
