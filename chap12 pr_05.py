num = int(input("Enter a number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("another.txt", "a") as f:
    f.write(str(table))
    f.write('\n')