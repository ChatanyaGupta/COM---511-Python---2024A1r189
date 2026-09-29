# wap to  Convert tuple → list → update → tuple
t = (10, 20, 30, 40)

print("Original tuple:", t)

lst = list(t)

lst[2] = 100

t = tuple(lst)

print("Updated tuple:", t)