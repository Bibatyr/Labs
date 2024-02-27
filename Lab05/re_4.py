import re

def find_sequence(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

text = input("Enter a string: ")
sequences = find_sequence(text)
print("Sequences of one uppercase letter followed be lowercase letters:")
print(sequences)