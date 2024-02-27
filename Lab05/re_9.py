import re

def insert_space(text):
    return re.sub(r'([A-Z][a-z]+)', r' \1', text).strip()

input_string = input("Enter a string: ")
modified_string = insert_space(input_string)
print("String with spaces inserted:", modified_string)