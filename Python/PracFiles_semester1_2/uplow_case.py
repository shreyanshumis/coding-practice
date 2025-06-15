def counter(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    upper, lower = counter(string)
    print("Uppercase count:", upper)
    print("Lowercase count:", lower)