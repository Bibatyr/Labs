import re

def replace_chars(text):
    pattern = r'[ ,.]'
    replacement = ':'
    result = re.sub(pattern, replacement, text)
    return result

text = input("Enter a string: ")
result = replace_chars(text)
print("After replacement", result)