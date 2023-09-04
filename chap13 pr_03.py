from functools import reduce
list = [9, 9, 8, 7, 67, 99, 90]
a = reduce(max, list)
print(a)