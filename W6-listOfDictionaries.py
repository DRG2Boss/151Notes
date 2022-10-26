# Building 3 dictionaries to start.
the_record = {'name': "Stu Dent",
 'gpa': 3.4,
 'studentID': 11112222}

student1 = {'name' : "Hard Worker",
 'gpa': 3.8,
 'studentID': 12121212}

student2 = {'name' : "Playstoo Muchgames",
 'gpa': 2.01,
 'studentID': 121123123}

# Now we will create an empty list and insert the various dictionaries into it.
all_students = []
all_students.append(student1)
all_students.append(student2)
all_students.append(the_record)

# Print the new list to see excactly how it would display.
print(all_students)
