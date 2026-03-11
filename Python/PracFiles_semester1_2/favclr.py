#a. Find out how many students are in the dictionary
#b. Change Lisa’s favourite colour
#c. Remove 'Jenny' and her favourite colour
#d. Sort and print students and their favouritecolours alphabetically by name

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print ("The number of people are :", len(people))

people['Lisa']='Blue'

print("The dictionary after lisa's colour change is :", people)

del people['Jenny']

print("The dictionary after the deletion of Jenny is :", people)

print("The dictionary after sorting is: ", sorted(people.items()))