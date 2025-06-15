print("Enter 1- Addition \n 2- Subtraction \n 3- Multiplication \n 4- Division \n 5- Find the Remainder")
choice = int(input())

print("Enter 2 numbers:")
no1 = int(input())
no2 = int(input())

if choice==1:
    print(no1+no2)
elif choice==2:
    print(no1-no2)
elif choice==3:
    print(no1*no2)
elif choice==4:
    print(no1/no2)
elif choice==5:
    print(no1%no2)
else:
    print("Invalid input")