def count(string):
    count = 0
    index = 0

    while index < len(string):
        if string[index:index + 3] == "ing":
            count += 1
            index += 3
        else:
            index += 1

    return count

strr = input("Enter a string: ")
occur = count(strr)
print("Occurrences of 'ing':", occur)
