import numpy as np

int_numberOfRows = 0
str_matrix = ''
str_matrixRow = ''
int_numberOfRows = input('Введите колличество строк')
int_numberOfRows = int(int_numberOfRows)

for i in range(int_numberOfRows):
    str_matrixRow = input('Введите строку матрицы')
    str_matrix = str_matrix + str_matrixRow + '; '
str_matrix = str_matrix[:-2]

matrix = np.matrix(str_matrix)

print('Матрица:')
for i in (str_matrix.split('; ')):
    print(i)
print('Определитель:')
print(round(np.linalg.det(matrix)))