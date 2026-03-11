myfile=open('C:\\Users\\mryts\\OneDrive\\Desktop\\petra.txt',"r")
li=" "
while li:
    li=myfile.readline()
    for word in li.split():
        print(word,end="#")
myfile.close()