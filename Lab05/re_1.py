import re

def match_string(pattern, text):
    match = re.fullmatch(pattern, text)
    if match:
        print("String matches the pattern.")
    else:
        print("String does not match the pattern.")
    
pattern = r'ab*'
text = input("Enter a string: ")

match_string(pattern, text)