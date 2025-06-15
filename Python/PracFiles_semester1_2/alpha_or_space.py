def check(string):
    if string[0].isalpha():
        return "Match Found"
    else:
        return "No match"

inp = input("Enter a string: ")
result = check(inp)
print(result)
