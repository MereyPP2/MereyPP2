from functools import reduce

def multip(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result
input_numbers = input()
numbers_list = [int(num) for num in input_numbers.split()]

result = multip(numbers_list)
print(result)

