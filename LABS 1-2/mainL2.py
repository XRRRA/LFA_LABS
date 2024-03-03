from grammar import Grammar
from finite_automaton import FiniteAutomaton

# Define the grammar variant
grammar = Grammar()
grammar.VN = {'S', 'B', 'D'}
grammar.VT = {'a', 'b', 'c', 'd'}
grammar.P = {
    'S': ['aS', 'bB'],
    'B': ['cB', 'd', 'aD'],
    'D': ['aB', 'b']
}

# Check the type of each grammar
print("Grammar Classification:", grammar.check_grammar_type())

# Define the finite automaton variant
finite_automaton = FiniteAutomaton()
finite_automaton.Q = {'q0', 'q1', 'q2'}
finite_automaton.Sigma = {'a', 'b', 'c'}
finite_automaton.delta = {('q0', 'a', 'q0'), ('q0', 'b', 'q1'), ('q1', 'c', 'q1'),
                          ('q1', 'c', 'q2'), ('q2', 'a', 'q0'), ('q1', 'a', 'q1')}
finite_automaton.q0 = 'q0'
finite_automaton.F = {'q2'}

# Convert finite automaton to regular grammar
regular_grammar = finite_automaton.to_regular_grammar()

# Print the regular grammar productions
print("Regular Grammar Productions for the NDFA:")
for non_terminal, productions in regular_grammar.P.items():
    for production in productions:
        print(non_terminal, "->", production)

# Determine if the finite automaton is deterministic
is_deterministic = finite_automaton.is_deterministic()

if is_deterministic:
    print("The NDFA is deterministic.")
else:
    print("The NDFA is non-deterministic.")

# Convert finite automaton to deterministic finite automaton
dfa = finite_automaton.to_deterministic_finite_automaton()

# Check if the resulting DFA is deterministic
is_deterministic_dfa = dfa.is_deterministic()
if is_deterministic_dfa:
    print("The converted DFA is deterministic.")
else:
    print("The converted DFA is non-deterministic.")
