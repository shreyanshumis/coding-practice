import math

if __name__ == "__main__":
    num = int(input("Enter a number"))
    sq = math.sqrt(num)

    if(sq*sq == num):
        print("The number is a square number")
    elif(sq*sq != num):
        print("The number isnt a square number")
    else:
        print("Invalid input")
