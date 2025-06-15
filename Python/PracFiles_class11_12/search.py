import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='xqtoj0lpspk',database='Proj')

cur=con.cursor()
while True:
    found =0 
    s = input("Enter the Stream you want to find: ")
    query = "SELECT * from Student where Stream='%s'"%s
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
        found=1
    if found==0:
        print("Records not found")
    ch = input("To search more records, Press 1 or else Press 2 : ")
    if ch == '2':
        break