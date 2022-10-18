rec_file = open("W5-sillyRec.txt", 'r')
all_lines = rec_file.readlines()
line_number = 1
for line in all_lines:
    if line_number % 2 ==1:
        print(line.strip())
    line_number += 1
# "x += y" is the same as "x = x + y"
