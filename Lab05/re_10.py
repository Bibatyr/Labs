import re

def camel_to_snake(camel_case):
    return re.sub(r'(?<!!^)(?=[A-Z])', '_', camel_case).lower()

camel_case_string = input("Enter a camel case tring: ")
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case string:", snake_case_string)