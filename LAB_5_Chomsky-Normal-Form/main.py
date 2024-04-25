import grammar

if __name__ == '__main__':
    V_n = {"S", "A", "B", "D", "C"}
    V_t = {"a", "b"}
    S = "S"
    P = {
        "S": {"bA", "B", "aA"},
        "A": {"epsilon", "aS", "ABab"},
        "B": {"a", "bS"},
        "C": {"abC"},
        "D": {"AB"}
    }

    # Instance of Grammar Class with uppercase notation of Non-Terminal Terms
    print("\nGenerate Grammar: ")
    variant = grammar.Grammar(V_n, V_t, P, S)

    print("Printing Grammar: ", end="")
    variant.print_variables()

    # Check the Grammar type from Laboratory Work 5
    print("Check Type of Grammar:")
    variant.check_type_grammar()

    CNF_Grammar = variant.convert_to_Chomsky_Normal_Form()
