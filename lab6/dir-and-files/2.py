import os

def check(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")

        if os.access(path, os.R_OK):
            print("Readable")
        else:
            print("Not readable")

        if os.access(path, os.W_OK):
            print("Writable")
        else:
            print("Not writable")

        if os.access(path, os.X_OK):
            print("Executable")
        else:
            print("Not executable")

    else:
        print(f"The path {path} does not exist.")

path = "C:"
check(path)