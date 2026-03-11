
myfile= open(r'C:\\Users\\mryts\\OneDrive\\Desktop\\petra.txt',"r")
str = myfile.read()
size= len(str)
print("Size of the given file is \n")
print(size, "bytes")
myfile.close()
