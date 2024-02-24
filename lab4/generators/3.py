def generate(n):
    for i in range(0, n+1):
        if i%12==0:
            yield i

n = int(input())
divisible = generate(n)
for num in divisible:
    print(num)
