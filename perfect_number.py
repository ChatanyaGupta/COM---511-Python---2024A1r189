#wap to checl whether a no is a perfect no.a no is perfect no if the sum of its proper divisor is equal tp no itself

num = int(input("Enter a number: "))

divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")