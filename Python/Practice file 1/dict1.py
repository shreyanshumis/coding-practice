n = int(input("How many students ?"))
compwin={}
for a in range(n):
    key =  input("Name of the student:")
    value = int(input("Number of competitions won:"))
    compwin[key]= value
print("the dictionary value is:")
print(compwin)