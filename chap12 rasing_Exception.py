def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good, Viraaj")

a = increment(9)
print(a)