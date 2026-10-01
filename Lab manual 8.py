# create a database using list and tuple. each student record must contain roll no,name,branch,and cgpa.store each record as a tuple inside a list.display all records and search for a student using roll no.
# conditions:each record should be stored as a tuple. the complete database should be stored as a list. roll numbers must be unique.

students = []
n = int(input("Number of students: "))

for _ in range(n):
    roll = input("Roll no: ")
    while any(s[0] == roll for s in students):
        print("Roll number already used.")
        roll = input("Enter a unique roll no: ")

    students.append((roll, input("Name: "), input("Branch: "),
                     float(input("CGPA: "))))

print("\nRecords:")
for student in students:
    print(student)

key = input("\nSearch roll no: ")
for student in students:
    if student[0] == key:
        print("Found:", student)
        break
else:
    print("Not found")