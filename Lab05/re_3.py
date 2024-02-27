import re

def find_sequence(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, text)
    return matches

text = input("Enter a string: ")
sequences = find_sequence(text)
print("Sequences of lowercase letters joined with an underscore:")
print(sequences)