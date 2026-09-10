#convert decimal to binary

num = int(input("Enter a decimal number: "))

if num == 0:
    binary = "0"
else:
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

print("Binary representation:", binary)