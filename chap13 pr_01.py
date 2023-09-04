name =input("Enter your name: ")
marks =input("Enter your marks: ")
phone =input("Enter your phone: ")

template = "The name of the student is {}, his marks are {} and phone number is {} "
output = template.format(name, marks, phone)
print(output)