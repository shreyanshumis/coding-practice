def pat(num_lines):
    for i in range(num_lines, 0, -1):
        spaces = ' ' * (num_lines - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

user_input = int(input("Enter the number of lines for the upside-down Christmas tree: "))
pat(user_input)
