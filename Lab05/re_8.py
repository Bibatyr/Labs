import re

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

input_string = input("Enter a string: ")
splitted_string = split_at_uppercase(input_string)
print("Split at uppercase string:", splitted_string)