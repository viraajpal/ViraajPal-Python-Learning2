def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

q = lambda num: num>6

l = [3, 7, 8, 3, 2, 1, 2, 4,  9, 6, 6, 75, 8796]
print(list(filter(greater_than_5, l)))
print(list(filter(q, l)))