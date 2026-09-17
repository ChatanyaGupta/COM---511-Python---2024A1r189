
# 8th wap to count how many times a particular element appear in a list 


lst = [10, 20, 30, 20, 40, 20, 50]

print("List:", lst)

element = int(input("Enter the element to count: "))

count = lst.count(element)

print("The element", element, "appears", count, "times in the list.")
