info = {
    'Name' : "Shrey", 'Course' : "BCA" , 'Hates' : "Maths"
}


print(info['Name']) #Gives an error if key is not present
print(info.get('Name'))#Returns none if the key is not present

#-------------------------------------------------------------#
#To access all keys
print(info.keys())

#To access all values
print(info.values())

for key in info.keys():
    print(info[key])

#to access key value pairs
print(info.items())
#----------------------------------------------------------------

s1={122:60, 29:40, 69:69, 420:69}
s2={10:13, 70:56}


#update
print(s1.update(s1))

#clear
print(s1.clear)

#empty dict
emp = {}

#pop
print(s1.pop(122))

#popitem - removes the last key-value pair
print(s1.popitem())

#deletes a dictionary
#============> del s1

#deletes a key-value pair
del s1[122]
