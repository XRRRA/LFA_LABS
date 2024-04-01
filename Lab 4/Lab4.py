import re
import itertools


def generate_combinations(regex):
    patterns = re.findall(r'\((.*?)\)', regex)
    combinations = []

    for pattern in patterns:
        options = pattern.split('|')
        combinations.append(options)

    valid_combinations = list(itertools.product(*combinations))
    return [''.join(combo) for combo in valid_combinations]


def explain_regex_processing(regex):
    # Split the regular expression into components
    components = regex.split(' ')
    explanation = []
    for component in components:
        if component.startswith('(') and component.endswith(')'):
            explanation.append(f"Match one of: {component[1:-1].split('|')}")
        elif component.endswith('*'):
            explanation.append(f"Match zero or more occurrences of: {component[:-1]}")
        elif component.endswith('?'):
            explanation.append(f"Match zero or one occurrence of: {component[:-1]}")
        elif component.endswith('^+'):
            explanation.append(f"Match one or more occurrences of: {component[:-2]}")
        elif component.startswith('^') and component.endswith('+'):
            explanation.append(f"Match exactly 5 occurrences of: {component[1:-2]}")
        else:
            explanation.append(f"Match: {component}")

    return explanation


# Variant 2
variant2_regex = "M?N^2 (O|P)^3 Q^* R^+ (X|Y|Z)^3 8^+ (9|0) (H|I) (J|K) L*N?"
variant2_combinations = generate_combinations(variant2_regex)
variant2_processing_sequence = explain_regex_processing(variant2_regex)

print("Variant 2:")
print("Generated Combinations:", variant2_combinations)
print("Processing Sequence:")
for step, explanation in enumerate(variant2_processing_sequence, 1):
    print(f"Step {step}: {explanation}")
print()