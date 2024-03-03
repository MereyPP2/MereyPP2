def all_elements_true(input_tuple):
    return all(input_tuple)
tuple_elements = eval(input())
result = all_elements_true(tuple_elements)
if result:
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")
