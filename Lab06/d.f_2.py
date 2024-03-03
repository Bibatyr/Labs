import os 

def check_path_access(path):
    if not os.path.exists(path):
        print("path does not exist")
        return
    
    if not os.access(path, os.R_OK):
        print("Path is not readable.")
    else:
        print("Path is readable.")

    if not os.access(path, os.W_OK):
        print("Path is not writeable.")
    else:
        print("Path is writeable.")

    if not os.access(path, os.X_OK):
        print("Path is not executable.")
    else:
        print("Path is executable.")

#Example
path = "C:\Сodes2"
check_path_access(path)