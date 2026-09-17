#  9th wap to ninput two list and create a third list containg common elements 


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common Elements:", common)
