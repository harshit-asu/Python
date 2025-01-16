import time
import random
from functools import reduce

numbers = list(range(10000000))
random.shuffle(numbers)

print("\nFind the maximum element in a list with 10 million numbers: \n")

start = time.time()

max_num = -1

for num in numbers:
    if max_num < num:
        max_num = num

end = time.time()

print(f"for loop with basic 'if' took \t{end-start} seconds.")


start = time.time()

max_num = max(numbers)

end = time.time()

print(f"built-in 'max' function took \t{end-start} seconds.")


start = time.time()

for num in numbers:
    max_num = max(max_num, num)

end = time.time()

print(f"'for' loop and max took \t{end-start} seconds.")


start = time.time()

for i in range(len(numbers)):
    if max_num < numbers[i]:
        max_num = numbers[i]

end = time.time()

print(f"'for' loop with index took \t{end-start} seconds.")


start = time.time()

for i in range(len(numbers)):
    max_num = max(max_num, numbers[i])

end = time.time()

print(f"for loop with index+max took \t{end-start} seconds.")


start = time.time()

max_num = reduce(max, numbers)

end = time.time()

print(f"reduce function with max took \t{end-start} seconds.")