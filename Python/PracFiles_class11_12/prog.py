import mysql.connector
conektr = mysql.connector.connect(host="localhost",user="root",password="xqtoj0lpspk",database="Proj")
crsr=conektr.cursor()
while True:
    roll = int(input("Enter the roll number:"))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks:"))
    stream = input("Enter the stream:")
    queryval = crsr.execute("INSERT into student values (%s, '%s', %s, '%s')"%(roll,name,marks,stream))
    print("done!")
    crsr.execute(queryval)
    conektr.commit()
    utta = input("Press 1 to continue, 2 to exit.")
    if utta=='2':
        break
print("The records have been updated!")