people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

num_students = len(people)
print("Number of students:", num_students)

people['Lisa'] = 'Green'

del people['Jenny']

sorted_people = sorted(people.items(), key=lambda x: x[0])
for student, color in sorted_people:
    print(student, ":", color)
