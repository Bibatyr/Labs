import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return
    
    if not os.access(file_path, os.F_OK):
        print("Error: File is not accessible.")
        return
    

    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")