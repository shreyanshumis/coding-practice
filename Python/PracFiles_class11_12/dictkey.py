info = {'User1':'CS','User2':'Economics','User3':'Accounts','User4':'Business Studies'}
inp = input("Enter the value which will be searched \n ...")
for a in info:
    if info[a].upper() == inp.upper():
        print("The key of the value given is -",a)
        break
    else: 
        print("Value does not exist")
