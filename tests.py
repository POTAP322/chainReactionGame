file = open('levels/level1', 'r')
lines = file.readlines()
matrix = [line.strip().split() for line in lines]
matrix = [[int(num) for num in row] for row in matrix]
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j])