#recursive function for sum
def sum(n):
    print(n,"+")
    if n<=1:
        return n
    else:
        return n + sum(n-1)
    
    
Inp = int(input("Enter a number"))
print("=======\n",sum(Inp))