# 6th  wap to rotate a list one position to right 

lst = [1, 2, 3, 4, 5]

last = lst.pop()
lst.insert(0, last)

print("List after rotation:", lst)
