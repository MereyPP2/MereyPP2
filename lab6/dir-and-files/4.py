def count(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in {file_path}: {len(lines)}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

path = "C:\Users\Пользователь\Desktop\lab6\dir-and-files\file.txt"
count(path)