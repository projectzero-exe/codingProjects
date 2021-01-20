import sys

input = sys.argv
input.pop(0)
# input1 = [int(i) for i in input]





# for item in input1:
#
#
#     if item % 3 == 0 and item % 5 == 0:
#         print("fizzbuzz")
#     elif item % 5 == 0:
#         print("buzz")
#     elif item % 3  == 0:
#         print("fizz")
#
#     else:
#         print(item)
#

for item in input:
    item1 = int(item)
    fizz = 'fizz' if item1 % 3 == 0 else ''
    buzz = 'buzz' if item1 % 5 == 0 else ''
    print(f'{fizz}{buzz}' or item1)
