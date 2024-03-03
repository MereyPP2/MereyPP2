with open('1.txt', 'r') as path1, open('2.txt', 'a') as path2:
    for line in path1:
        path2.write(line)