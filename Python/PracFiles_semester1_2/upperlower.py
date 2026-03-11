def string_test (s):
    d = {
        "upperCase":0,
        "lowerCase":0,
        "whitespace":0,
        "digit":0
    }
    for c in s:
        if c.isupper():
            d["upperCase"]+=1
        elif c.islower():
            d["lowerCase"]+=1
        elif c.isspace(): #==" " can also be used
            d["whitespace"]+=1
        elif c.isdigit():
            d["digit"]+=1
        else:
            pass

    print("The String: ",s)
    print("No. of Upper case characters: ", d["upperCase"])
    print("No. of Lower case characters: ", d["lowerCase"])
    print("No. of whitespaces: ",d["whitespace"])
    print("No. of digits: ",d["digit"])

i= input("Enter a sentence:")
string_test(i)
