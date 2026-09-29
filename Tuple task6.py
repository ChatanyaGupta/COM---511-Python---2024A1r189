 #wap to Student data as tuple and display grade

student = (
    input("Enter name: "),
    int(input("Enter roll number: ")),
    int(input("Enter marks: "))
)

name, roll, marks = student

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Name:", name)
print("Roll Number:", roll)
print("Marks:", marks)
print("Grade:", grade)