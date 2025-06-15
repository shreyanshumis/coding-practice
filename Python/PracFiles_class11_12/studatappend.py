import pickle
stuffi = {}
stuf = open('C:\\Users\\mryts\\OneDrive\\Desktop\\stuffi.txt','ab')
an = 'y'
while an =='y':
    rno = int(input("Enter the roll no. : "))
    name = input("Enter the name : ")
    marks = float(input("Enter the marks : "))
    stuffi['roll no']=rno
    stuffi['name']=name
    stuffi['marks']=marks
    pickle.dump(stuffi,stuf)
    an=input("Want to append some more records? \n say y if you do, say n if not. . . . \n")
stuf.close()