print("What is your age?")
age = int(input())
if age > 18:
    print("Congratulations! You are eligible to drive.")
elif age == 18:
    print("We will check if you can drive, visit us.")
else:
    print("Sorry, but you aren't eligible to drive.")