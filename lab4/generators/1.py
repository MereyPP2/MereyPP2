def generate_squares(N):
    for i in range(N):
        yield i **2

num = int(input())
generate = generate_squares(num)
for q in generate:
    print(q)