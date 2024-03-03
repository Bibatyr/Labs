def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{file_path}' successfully.")
    except IOError:
        print(f"Error writing to file '{file_path}'.")