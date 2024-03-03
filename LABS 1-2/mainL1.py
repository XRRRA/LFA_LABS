from grammar import Grammar

grammar = Grammar()
generated_strings = grammar.generate_string()

# Print the generated strings
for i, string in enumerate(generated_strings, start=1):
    print(f"Generated string {i}: {string}")

# Convert Grammar to FiniteAutomaton
finite_automaton = grammar.to_finite_automaton()

# Verify attributes of the FiniteAutomaton object
print("\nStates (Q):", finite_automaton.Q)
print("Alphabet (Sigma):", finite_automaton.Sigma)
print("Transitions (delta):", finite_automaton.delta)
print("Initial state (q0):", finite_automaton.q0)
print("Accepting state (F):", finite_automaton.F)


# Test string_belongs_to_language method
input_string = "abd"
if finite_automaton.string_belongs_to_language(input_string):
    print(f"\nThe input string '{input_string}' belongs to the language.")
else:
    print(f"\nThe input string '{input_string}' does not belong to the language.")