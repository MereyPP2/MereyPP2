import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
        head, tail = os.path.split(path)
        print(f"Directory: {head}")
        print(f"File name: {tail}")
    else:
        print(f"The path {path} does not exist.")

path_to_check = "C:\Users\Пользователь\Desktop\lab6\dir-and-files\file.txt"
check_path(path_to_check)