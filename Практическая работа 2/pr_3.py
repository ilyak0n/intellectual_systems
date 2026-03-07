import numpy as np
rows = int(input("Введите количество строк:"))
cols = int(input("Введите количество столбцов:"))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Введите элемент матрицы:строка " + str(i+1) +", столбец " + str(j+1) +" ="))
        row.append(element)
    matrix.append(row)
matrix = np.array(matrix)
print( "Матрица:\n", matrix)
rank = np.linalg.matrix_rank(matrix)
print("Ранг матрицы:\n", rank)