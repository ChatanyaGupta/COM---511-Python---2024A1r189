#WAP a python program to input numbers in a list containing unique elements 
n = int(input("Enter number of elements: "))
numbers = []
unique = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)
