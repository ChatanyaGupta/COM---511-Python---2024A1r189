# 6 WAP to Reverse every kth row in a matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

n = 2

# Jump directly to every nth row (0-indexed: index n-1, 2n-1, ...)
for i in range(n - 1, len(matrix), n):
    matrix[i].reverse()

for row in matrix:
    print(row)