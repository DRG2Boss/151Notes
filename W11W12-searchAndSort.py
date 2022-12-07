
class Student:
    def __init__(self, name, sid, sCredits, gpa):
        self.name = name
        self.bannerID = sid
        self.credits = sCredits
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, bannerID: {self.bannerID} \n GPA: {self.gpa}, credits: {self.credits}"
# end Student class


def binary_search(list_of_students, student_to_find):
    if list_of_students == []:
        return None
    middle = len(list_of_students)//2
    middle_student = list_of_students[middle]
    if middle_student.name == student_to_find:
        return middle_student
    if middle_student.name < student_to_find:
        return binary_search(list_of_students[middle:], student_to_find)
    else:
        return binary_search(list_of_students[:middle], student_to_find)


def get_data(filename):
    student_file = open(filename)
    all_lines = student_file.readlines()
    list_of_students = []
    for line in all_lines:
        data = line.split('|')
        current_student = Student(data[0], int(data[1]), gpa=float(data[3]), sCredits=int(data[2]))
        list_of_students.append(current_student)
    return list_of_students

# Here's how we'll sort by name
def get_key(student_to_sort):
    return student_to_sort.name


def main():
    student_data = get_data('W11-students.txt')
    student_data.sort(key=get_key)
    median_student = find_median(student_data)
    print(median_student)
    # stu_to_find = input("What student should we find? ")
    # result = binary_search(student_data, stu_to_find.title())
    # print(result)


def find_sum_of_credits():
    student_data = get_data('W11-students.txt')
    find_sum = 0
    for someone in student_data:
        sum = sum + someone.credits
    return sum


def recursive_sum_of_credits(student_list):
    # Note: "not" student_list is the same thing as student_list == []
    if not student_list:
        return 0
    first_student = student_list[0]
    return first_student.credits + recursive_sum_of_credits(student_list[1:])

# recursive_sum = recursive_sum_of_credits(get_data("W11-students.txt"))
# sum = find_sum_of_credits()
# print(f"those students have {sum} credits all together.")
# print(f"the recursive calculated sum is {recursive_sum}.")


def find_average(student_list):
    total = 0
    for student in student_list:
        total += student.gpa
    return total/len(student_list)

# average = find_average(get_data("W11-students.txt"))
# print(f"the average gpa was {average}")

def find_median(sorted_student_data):
    middle_loc = len(sorted_student_data)//2
    return sorted_student_data(middle_loc)

main()
