def unique(nums):
    unique_values = []
    [unique_values.append(i) for i in nums if i not in unique_values]
    return unique_values

s = list(map(int, input().split()))
print(unique(s))