students = ["Nathan", "Kelvin", "Mariama", "Barry", "Tori", "Michael", "Dominic", "Jose", "Colin", "Emily", "John"]

students.append("Pascal")
# This will add the string to the END of the list.
students.insert(2, "Dan")
# This will INSERT the string to the THIRD position on the list. Moves all list items that follow to the next spot.

print(students[0])
# "0" is the first item in the list
print(students[-4])
# Negative numbers work backwards from the end of the list. This STARTS at -1 for some reason, not 0.
