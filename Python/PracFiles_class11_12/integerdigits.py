num = int(input("Enter a number from 0-999: "))
if num<0:
    print("Invalid input, please try again \n Valid range is from 0 to 999")
elif num<10:
    print("Single digit number")
elif num<100:
    print("Double digit number")
elif num<=999:
    print("Triple digit number")
else:
    print("Invalid input, please try again \n Valid range is from 0 to 999")
    