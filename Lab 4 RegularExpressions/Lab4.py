import random


def generate_string(pattern: str) -> str:
    result = ""
    i = 0
    while i < len(pattern):
        char = pattern[i]
        if char == '(':
            j = i + 1
            subpattern = ""
            while pattern[j] != ')':
                subpattern += pattern[j]
                j += 1
            choices = subpattern.split('|')
            subpattern = random.choice(choices)
            repeat = 1
            i = j + 1
            # Handling special characters '^', '*', '+', '?'
            if j + 1 < len(pattern):
                next_char = pattern[j + 1]
                if next_char == '^':
                    if pattern[j + 2].isdigit():
                        repeat = int(pattern[j + 2])
                        i = j + 3
                elif next_char == '*':
                    repeat = random.randint(0, 3)
                    i = j + 2
                elif next_char == '+':
                    repeat = random.randint(1, 3)
                    i = j + 2
                elif next_char == '?':
                    repeat = random.randint(0, 1)
                    i = j + 2
            result += subpattern * repeat
            continue
        # Handling special characters '*', '+', '?', '^'
        next_char = pattern[i + 1] if i + 1 < len(pattern) else ""
        if next_char == '^':
            result += char * int(pattern[i+2])
            i += 3
            continue
        elif next_char == '*':
            result += char * random.randint(0, 5)
            i += 2
            continue
        elif next_char == '+':
            result += char * random.randint(1, 5)
            i += 2
            continue
        elif next_char == '?':
            result += char * random.randint(0, 1)
            i += 2
            continue
        result += char
        i += 1
    return result


def explain_pattern_processing(pattern: str) -> list:
    explanation = []
    i = 0
    while i < len(pattern):
        char = pattern[i]
        if char == '(':
            j = i + 1
            subpattern = ""
            while pattern[j] != ')':
                subpattern += pattern[j]
                j += 1
            choices = subpattern.split('|')
            explanation.append(f"Select one of: {choices}")
            i = j + 1
            # Handling special characters '^', '*', '+', '?'
            if j + 1 < len(pattern):
                next_char = pattern[j + 1]
                if next_char == '^':
                    repeat = int(pattern[j + 2])
                    explanation.append(f"Repeat the selection {repeat} times")
                    i = j + 3
                elif next_char == '*':
                    explanation.append("Randomly repeat zero to three times")
                    i = j + 2
                elif next_char == '+':
                    explanation.append("Randomly repeat one to three times")
                    i = j + 2
                elif next_char == '?':
                    explanation.append("Randomly repeat zero or one time")
                    i = j + 2
            continue
        # Handling special characters '*', '+', '?', '^'
        next_char = pattern[i + 1] if i + 1 < len(pattern) else ""
        if next_char == '^':
            repeat = int(pattern[i + 2])
            explanation.append(f"Repeat {char} {repeat} times")
            i += 3
            continue
        elif next_char == '*':
            explanation.append(f"Randomly repeat {char} zero to five times")
            i += 2
            continue
        elif next_char == '+':
            explanation.append(f"Randomly repeat {char} one to five times")
            i += 2
            continue
        elif next_char == '?':
            explanation.append(f"Randomly repeat {char} zero or one time")
            i += 2
            continue
        explanation.append(f"Use character: {char}")
        i += 1

    return explanation


pattern1 = "M?N^2(O|P)^3Q*R+"
pattern2 = "(X|Y|Z)^38+(9|0)^2"
pattern3 = "(H|i)(J|K)L*N?"

# Pattern 1
print("Explanation for Pattern 1:")
explanations = explain_pattern_processing(pattern1)
for step in explanations:
    print(step)

print("\nExamples of words made after pattern 1:")
generated_strings = [generate_string(pattern1) for _ in range(5)]
print(", ".join(generated_strings))

# Pattern 2
print("\nExplanation for Pattern 2:")
explanations = explain_pattern_processing(pattern2)
for step in explanations:
    print(step)

print("\nExamples of words made after pattern 2:")
generated_strings = [generate_string(pattern2) for _ in range(5)]
print(", ".join(generated_strings))

# Pattern 3
print("\nExplanation for Pattern 3:")
explanations = explain_pattern_processing(pattern3)
for step in explanations:
    print(step)

print("\nExamples of words made after pattern 3:")
generated_strings = [generate_string(pattern3) for _ in range(5)]
print(", ".join(generated_strings))
