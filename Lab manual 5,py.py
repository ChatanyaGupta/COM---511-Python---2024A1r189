# 5 Linear Search and Binary Search

a = [10, 20, 30, 40, 50]
x = int(input("Enter number to search: "))

found = False

for i in range(len(a)):
    if a[i] == x:
        print("Element found at index", i)
        found = True
        break

if found == False:
    print("Element not found")


low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == x:
        print("Binary Search: Element found at index", mid)
        found = True
        break
    elif x > a[mid]:
        low = mid + 1
    else:
        high = mid - 1

if found == False:
    print("Binary Search: Element not found")