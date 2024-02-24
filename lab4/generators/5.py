def gen(N):
    for i in range(N, 0, -1):
        yield i

N = int(input())
generate = gen(N)
for q in generate:
    print(q)