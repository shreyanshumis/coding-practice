def count_spaces(string):
    space_count = 0

    for char in string:
        if char == ' ':
            space_count += 1

    return space_count

if __name__ == "__main__":
    string = input("Enter a sentence: ")
    spaces = count_spaces(string)
    print("Number of spaces:", spaces)
