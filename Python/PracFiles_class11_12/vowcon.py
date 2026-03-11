myfile=open('C:\\Users\\mryts\\OneDrive\\Desktop\\petra.txt','r')
ch=" "
vcount=0
ccount=0
while ch :
    ch=myfile.read(1)
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        vcount=vcount+1
    else:
        ccount=ccount+1
print("vowels in the file = ",vcount)
print("consonants in the file = ",ccount)
myfile.close()