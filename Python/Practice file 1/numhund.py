while (True):
    i = int(input("Enter a number which is above 100 - \n"))
    if i>=100:
        print("Congratulations you printed a number greater than 100!, the number is - ",+ i,"\n")
        break
    elif i<100:
        print("Try again!\n")
    else:
        print("Invalid input")
        continue
