import os
def delete(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File {path} deleted successfully.")
    else:
        print(f"File {path} not found.")

file = "C:\Users\Пользователь\Desktop\lab6\dir-and-files\file.txt"
delete(file)