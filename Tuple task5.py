 # WAP to Check value and display its position using tuple

t = (10, 20, 30, 40, 50)

value = int(input("Enter value: "))

if value in t:
    print("Value found at position:", t.index(value) + 1)
else:
    print("Value not found")