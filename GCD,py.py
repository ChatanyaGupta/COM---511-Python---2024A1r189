#wap to input two numbers and find their GCD using a loop 


a = int(input("Enter first number: "))
b = int(input("Enter second number:"))

while b != 0:
    a, b = b, a % b

print("GCD =", a)

