def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Conferences copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files bot found.")