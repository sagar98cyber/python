matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0])

matrix[0][2] =30

print(matrix)

for row in matrix:
    for item in row:
        print(item)