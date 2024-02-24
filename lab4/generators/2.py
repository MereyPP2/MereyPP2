def generate(n):
    for i in range(0, n+1, 2):
        yield i

num = int(input())
for x in generate(num):
    print(x)