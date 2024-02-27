import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)

text_string = input("Enter a snake case string: ")
camel_case_string = snake_to_camel(text_string)
print("Camel case string:", camel_case_string)