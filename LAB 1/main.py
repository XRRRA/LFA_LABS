# Import the Grammar and FiniteAutomaton classes from your module
from grammar import Grammar

# Instantiate the Grammar class
grammar = Grammar()

# Generate 5 valid strings
generated_strings = grammar.generate_string()

# Print the generated strings
for i, string in enumerate(generated_strings, start=1):
    print(f"Generated string {i}: {string}")

# Convert Grammar to FiniteAutomaton
finite_automaton = grammar.to_finite_automaton()

# Add transitions
finite_automaton.delta = {
    ('S', 'a'): 'S',
    ('S', 'b'): 'B',
    ('B', 'c'): 'B',
    ('B', 'd'): 'S',
    ('B', 'a'): 'D',
    ('D', 'a'): 'B',
    ('D', 'b'): 'S'
}

# Verify attributes of the FiniteAutomaton object
print("\nStates (Q):", finite_automaton.Q)
print("Alphabet (Sigma):", finite_automaton.Sigma)
print("Transitions (delta):", finite_automaton.delta)
print("Initial state (q0):", finite_automaton.q0)
print("Accepting state (F):", finite_automaton.F)


# Test string_belongs_to_language method
input_string = "aabaad"
if finite_automaton.string_belongs_to_language(input_string):
    print(f"\nThe input string '{input_string}' belongs to the language.")
else:
    print(f"\nThe input string '{input_string}' does not belong to the language.")