import time
import math

def square(num, mils):
    time.sleep(mils / 1000.0)
    result = math.sqrt(num)
    return result

num_inp = int(input())
mils_inp = int(input())
result = square(num_inp, mils_inp)
print(f"Square root of {num_inp} after {mils_inp} milliseconds is {result}")

