def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk)-1

def pop(stk):
    if(stk==[]):
        print("Stack empty;Underflow")
    else:
        print("City deleted :",stk.pop())

#__Main__
stack=[]
top = None
while True:
    print("Stack Operation:")
    print("1.City Addition")
    print("2.City Removal")
    print("3.Exit")
    ch = int(input("Enter your choice(1-3):"))
    if ch==1:
        pincode = int(input("Enter Pin Code of a city to be inserted :"))
        cname = input("Enter City Name to be inserted :")
        item = [pincode,cname]
        push(stack,item)
        input()
    elif ch==2:
        pop(stack)
        input() 
    elif ch==3:
        break
    else:
        print("Invalid choice ")
    input()