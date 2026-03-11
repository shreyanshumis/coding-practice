def print_christmas_tree(num_lines):
    for i in range(1, num_lines + 1):
        spaces = ' ' * (num_lines - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

user_input = int(input("Enter the number of lines for the Christmas tree: "))
print_christmas_tree(user_input)
