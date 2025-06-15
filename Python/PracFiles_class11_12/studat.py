import pickle
stu = {}
stuf = open('C:\\Users\\mryts\\OneDrive\\Desktop\\stu.txt','wb')
an = 'y'
while an =='y':
    rno = int(input("Enter the roll no. : "))
    name = input("Enter the name : ")
    marks = float(input("Enter the marks : "))
    stu['roll no']=rno
    stu['name']=name
    stu['marks']=marks
    pickle.dump(stu,stuf)
    an=input("Want to enter some more records? \n say y if you do, say n if not. . . . \n")
stuf.close()