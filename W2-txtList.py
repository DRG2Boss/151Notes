my_file = open('W2-requiredCS.txt', 'r')
all_lines = my_file.readlines()
# Make sure you use readLINES and not readLINE, readLINE only reads first line of file.
for line in all_lines:
    upper_case_line = line.upper()
#    upper_case_line = upper_case_line.strip()
# "strip" command will remove any whitespace from the left and right sides of a string
    course_and_name = upper_case_line.split(' : ')
    print(course_and_name[0])
    print(course_and_name[1])

# "for (new variable) in (existing variable):" is a looping index
print("Those are the required COMP courses for the major")
