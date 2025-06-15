a = input("Enter the number :")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int (a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid input")

print("Important code")

#We can also put multiple except blocks for a try and handle things differently for each type of error

#ValueError
#IndexError
#MemoryError etc. 