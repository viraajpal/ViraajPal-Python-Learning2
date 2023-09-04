a = [23, 66, 87, 99, 78, 66, 55, 44, 43, 42, 421]
#  = []
# or item in a:
#    if item%2==0:
#        b.append(item)

# rint(b)
# list comprehention in python

b = [i for i in a if i%2==0]
print(b)