def solve(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if 2* i + 4* j == legs:
            return i, j
    return False
x, y = solve(int(input()), int(input()))
print(x. y)