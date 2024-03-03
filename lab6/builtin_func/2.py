def count(num):
    upp_count = sum(1 for char in num if char.isupper())
    low_count = sum(1 for char in num if char.islower())
    return upp_count, low_count

input_str = input()
upper, lower = count(input_str)
print(upper)
print(lower)