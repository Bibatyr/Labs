import string

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is {letter}.txt file.")
        print(f"File '{file_name}' created successfully.")

generate_files()