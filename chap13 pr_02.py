l = [6,8,5,9,70,80,90,95,85,75]

a = filter(lambda a: a%5==0, l)
print(list(a))