
class Student:
    def __init__(self, name, sid, credits, gpa):
        self.name = name
        self.bannerID = sid
        self.credits = credits
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
        current_student = Student(data[0], int(data[1]), gpa=float(data[3]), credits=int(data[2]))
        list_of_students.append(current_student)
    return list_of_students


# Here's how we'll sort by name
def get_key(student_to_sort):
    return student_to_sort.name


def main():
    student_data = get_data('W11-students.txt')
    student_data.sort(key=get_key)
    stu_to_find = input("What student should we find? ")
    result = binary_search(student_data, stu_to_find.title())
    print(result)


main()
