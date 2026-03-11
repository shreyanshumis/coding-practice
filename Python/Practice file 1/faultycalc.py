print("Enter 1- Addition \n 2- Subtraction \n 3- Multiplication \n 4- Division")
user = int(input())
a = int(input("Enter the operator"))
b = int(input("Enter the other number"))
c = 0
def add():
    if a==56 and b==9:
        c = 77
    else:
        c = a+b
    return c
def subtract():
    c = a-b
    return c
def mult():
    if a==45 and b==3:
        c=555
    else:
        c=a*b
    return c
def div():
    if a==56 and b==6:
        c = 4
    else:
        c =float(a/b)
    return c

if user == 1:
    print("The sum of the two numbers is : ", add())
elif user == 2:
    print("The number after subtraction is : ", subtract())
elif user == 3:
    print("The product of the two numbers is : ", mult())
elif user == 4:
    print("The number after division is : ", div())
else:
    print("Invalid Input.")