# wap to Multiple students using list of tuples


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))

    student = (name, roll, marks)
    students.append(student)

print("\nAll Student Records:")
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Marks:", student[2])
        print()