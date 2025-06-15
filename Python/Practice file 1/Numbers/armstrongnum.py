if __name__ == "__main__":

    num = int(input("Enter a number"))
    orignum = num
    newnum = 0
    while(num>0):
        temp = num%10
        temp = pow(temp,3)
        newnum += temp
        num //= 10
    
    if newnum == orignum:
        print("It is an armstrong number")
    else:
        print("It isnt")