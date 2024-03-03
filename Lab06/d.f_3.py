import os

def check_path(path):
    if os.path.exists(path):
        print("path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("path does not exist")

