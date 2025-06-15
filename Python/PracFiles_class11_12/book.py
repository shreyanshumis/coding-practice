def separate():
    print("─"*50)
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk, item):
    stk.append(item)
    top = len(stk)-1
def Display(stk):
    if isEmpty(stk):
        print("Stack empty")
    else:
        top=len(stk)-1
        print(stk[top]),"<- Top"
        for a in range(top-1,-1,-1):
            print(stk[a])
#__Main__
Stack = []
top = None
while True:
    separate()
    print("───Books───")
    print("1. Push")
    print("2. Display stack")
    print("3. Exit")
    ch = int(input("Enter your choice (1-3) :"))
    if ch == 1:
        bookno = int(input("Enter the book number:"))
        bookname= input("Enter the book name:")
        item=[bookno,bookname]
        Push(Stack, item)
        input()
    elif ch == 2:
        Display(Stack)
        input()
    elif ch == 3:
        break
    else:
        print("Wrong choice")
        input()
