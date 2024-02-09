def spy_games(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if nums == code[0]:
            code.pop(0)
    return len(code) == 1

game = list(map(int, input().split()))
print(spy_games(game))