l1=['a','b','c']
l2=['h','i','t']
l3=['0','2','2']
print("Originally:")
print("list 1=", l1)
print("List 2 =", l2)
print("List 3 =", l3)
l3.extend(l1)
l3.extend(l2)
print("The list after addition is :")
print(l3)