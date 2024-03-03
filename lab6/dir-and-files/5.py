def write(path, list):
    with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

path = "c:\Users\Пользователь\Desktop\lab6\dir-and-files\file.txt"
list = [1, 2, 3, 4, 5]
write(path, list)
