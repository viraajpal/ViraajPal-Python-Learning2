def square(num):
    return num*num

L = [2, 6, 8, 9]
# method 1
L2 = []
for item in L:
    L2.append(square(item))
print(L2)

#method 2
print(list(map(square, L)))
