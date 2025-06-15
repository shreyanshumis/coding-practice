dictionary = {"Shrey" : "I mean"}
user = input("Enter a word to search : ")
if user in dictionary.keys():
    print(dictionary[user])
else:
    print("Invalid input")