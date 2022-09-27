file1 = open("W3-PeerAssistLoop.txt", "r")
someLines = file1.readlines()

for lines in someLines:
    lines = lines.split(',')
    print(f"Name: {lines[0]}")
    avgGrade = (int(lines[1])+int(lines[2])+int(lines[3]))/3
# "int" is needed to convert a "string" number in a seperate file into an "integer" number that Python can recognize.
    print(f"Name: {lines[0]}, GPA: {avgGrade}")
