largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if (num == "done"):
        break
    try:
        num = int(num)
        value = num
        if smallest is None and largest is None:
            smallest = value
            largest = value
        elif smallest > value:
            smallest = value
        elif largest < value:
            largest = value
    except:
        print("invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)