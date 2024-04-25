import unittest
from grammar import Grammar


class TestGrammarMethods(unittest.TestCase):

    def setUp(self):
        # This method will run before each test case
        print("\n" * 3)  # Adding three empty lines before each test

    def tearDown(self):
        # This method will run after each test case
        print("\n" * 2)  # Adding two empty lines after each test

    def test_epsilon_elimination(self):
        # Test case 1: Grammar with epsilon production
        print("Test Case 1: Grammar with epsilon production")
        print("Testing elimination of epsilon productions...")
        V_n = {"S", "A"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "b", "epsilon"},
            "A": {"a"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P = grammar.eliminate_epsilon_productions()
        self.assertNotIn("\u03B5", new_P["S"])
        self.assertEqual(len(new_P["S"]), 2)  # Expect two productions after epsilon elimination

        # Test case 2: Grammar without epsilon production
        print("Test Case 2: Grammar without epsilon production")
        print("Testing elimination of epsilon productions...")
        V_n = {"S", "A"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "b"},
            "A": {"a"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P = grammar.eliminate_epsilon_productions()
        self.assertNotIn("\u03B5", new_P["S"])
        self.assertEqual(len(new_P["S"]), 2)  # No change expected

    def test_inaccessible_elimination(self):
        # Test case 1: Grammar with inaccessible symbols
        print("Test Case 1: Grammar with inaccessible symbols")
        print("Testing elimination of inaccessible symbols...")
        V_n = {"S", "A", "B"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA"},
            "A": {"b"},
            "B": {"a"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P, new_V_n = grammar.eliminate_inaccessible_symbols(grammar.P, grammar.V_n)
        self.assertNotIn("B", new_V_n)  # Symbol B should be removed

        # Test case 2: Grammar without inaccessible symbols
        print("Test Case 2: Grammar without inaccessible symbols")
        print("Testing elimination of inaccessible symbols...")
        V_n = {"S", "A"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA"},
            "A": {"b"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P, new_V_n = grammar.eliminate_inaccessible_symbols(grammar.P, grammar.V_n)
        self.assertEqual(new_V_n, {"S", "A"})  # No change expected

    def test_unit_production_elimination(self):
        # Test case 1: Grammar with unit productions
        print("Test Case 1: Grammar with unit productions")
        print("Testing elimination of unit productions...")
        V_n = {"S", "A", "B"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "B"},
            "A": {"B"},
            "B": {"a"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P = grammar.eliminate_unit_productions(grammar.P)
        self.assertNotIn("A", new_P["S"])  # Unit production A -> B eliminated

        # Test case 2: Grammar without unit productions
        print("Test Case 2: Grammar without unit productions")
        print("Testing elimination of unit productions...")
        V_n = {"S", "A", "B"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "B"},
            "A": {"a"},
            "B": {"a"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        new_P = grammar.eliminate_unit_productions(grammar.P)
        self.assertEqual(len(new_P["S"]), 2)  # No change expected

    def test_chomsky_normal_form_conversion(self):
        # Test case 1: Grammar conversion to Chomsky Normal Form
        print("Test Case 1: Grammar conversion to Chomsky Normal Form")
        print("Testing conversion to Chomsky Normal Form...")
        V_n = {"S", "A", "B"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "B"},
            "A": {"aS", "ABab"},
            "B": {"a", "bS"}
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        cnf_grammar = grammar.convert_to_Chomsky_Normal_Form()
        self.assertEqual(cnf_grammar.type_grammar, 2)  # Converted grammar should be type 2 (CFG)

        # Test case 2: Grammar not suitable for Chomsky Normal Form conversion
        print("Test Case 2: Grammar not suitable for Chomsky Normal Form conversion")
        print("Testing conversion to Chomsky Normal Form...")
        V_n = {"S", "A", "B"}
        V_t = {"a", "b"}
        P = {
            "S": {"aA", "B"},
            "A": {"aS", "ABab"},
            "B": {"abC"},
            "C": {"abC"},
        }
        S = "S"

        grammar = Grammar(V_n, V_t, P, S)
        cnf_grammar = grammar.convert_to_Chomsky_Normal_Form()
        self.assertIsNone(cnf_grammar)  # Should return None if conversion is not possible


if __name__ == '__main__':
    unittest.main()
