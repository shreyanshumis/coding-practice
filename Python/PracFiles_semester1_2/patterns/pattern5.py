def pat(num):
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)
        stars = '*' * i
        print(spaces + stars)

user_input = int(input("Enter a number: "))
pat(user_input)