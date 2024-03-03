import os

def list_directories_and_files(path, include_all = False):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
        print("\nFiles:")
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                print(item)

        if include_all:
            print("\nAll Directories and Files:")
            for root, dirs, files in os.walk(path):
                for dir_name in dirs:
                    print(os.path.join(root, dir_name))
                for file_name in files:
                    print(os.path.join(root, file_name))

#Example
path = "C:\Сodes2\Lab06"
list_directories_and_files(path)