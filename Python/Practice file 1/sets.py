s ={2,3,5,46,69}

ss = set()
#empty set be like
sss= {}
#this is an empty dictionary and not a set, use the above method to make an empty set

print(type(s))
print(type(ss))
print(type(sss))

#======================================================================
s1 = {1,2,5,6}
s2 = {3,6,7}

#Union - combines all the non duplicate elements
print(s1.union(s2)) #Merger of 2 sets

#Intersection - shows only the common elements
print(s1.intersection(s2))

#Symmetric difference - shows only the non common elements
print(s1.symmetric_difference(s2))

#Difference update - elemts only present in the original set and not in both the sets (A-B in a way)
print(s1.difference(s2))

#Checks if items of a given set are present in another set - Returns True/False
print(s1.isdisjoint(s2))

#checks if an given set is a superset of another or not
print(s1.issuperset(s2)) 

#checks if a given set is a subset of another or not
print(s1.issubset(s2))

#Add -  to add a single item to the set
s1.add(10)
print(s1)

#Remove() / Discard() - to remove an item from the set
#If we try to remove an element from a set which is NOT present in the set, remove raises an error but discard doesnt.
s1.remove(10)
print(s1)

#pop removes the last element of the set but we dont know which element gets popped since the sets are unordered
popped = s1.pop()
print(popped)

#Del is a keyword(NOT A METHOD) used for deleting the entire set
#---------------> del s1

#If you dont want to delete the entire set but only the items in that set, we can use clear instead
s1.clear()
print(s1)

#Check if a value is present in set -use the 'in' keyword
if 10 in s1:
    print("Yes!")
else:
    print("No it's absent")


#Update - If you want to add more than one item
#update functions actually change the values in the original set
s1.update(s2) #Adds in the values of s2 into s1
s1.intersection_update(s2)#same but intersection instead of union...

#END.