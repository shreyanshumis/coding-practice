guesses = [1,2,3,4,5]
i = 1
num = 14
for i in guesses:
    numin = int(input("Guess the number"))
    if numin is num:
        j = 5 - i
        print("YOU WIN \nGAME OVER")
        print("Guesses made", +i)
        print("You had ",+ j," guesses left")
        break
    elif numin > num:
        print("The number is smaller than the number you guessed.")
    elif numin < num:
        print("The number is greater than the number you guessed.")
    else:
        print("Invalid input")