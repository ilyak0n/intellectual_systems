import numpy as np
rows = int(input("Введите количество строк:"))
cols = int(input("Введите количество столбцов:"))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Введите элемент матрицы: ["+ str(i+1) +"][" + str(j+1) +"]: "))
        row.append(element)
    matrix.append(row)
matrix = np.array(matrix)
print( "Матрица:\n", matrix)
result = np.linalg.inv(matrix)
print("Обратная матрица:\n", result)