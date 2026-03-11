info = {'Aryan':'Comp','Mark':'Economics','Nisha':'English','Ali':'Business'}
inp = input("Enter the value which will be searched")
for a in info:
    if info[a].upper() == inp.upper():
        print("The key of the value given is -",a)
        break
    else: 
        print("Value does not exist")
#Now run it