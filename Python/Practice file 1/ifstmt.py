#if statement
print("This defines the if statement")
var = 100
if(var==100):
    print("True")
print("Executed")

#if-else statement
print("This defines the if else statement")
if(var == 10):
    print("Very true")
else:
    print("Very false")
print("Executed again")

#nested if statement
print("This defines the nested if statement")
if(var == 100):
    if(var<15):
        print("var is smaller than 15")
    if(var>105):
        print("var is greater than 105")
print("Executed yet again")

#if else if ladder
print("This defines an if else if ladder")
i= 20
if( i == 10):
    print("No")
elif(i == 15):
    print("5 numbers away")
elif(i== 20):
    print("Right")
else:
    print("NOOOOOO")