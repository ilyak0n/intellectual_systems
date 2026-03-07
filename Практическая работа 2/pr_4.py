import numpy as np
def compiling_matrices():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input("Введите элемент матрицы: " + str(i+1) +" " + str(j+1) +": "))
            row.append(element)
        matrix.append(row)
    return (matrix)
    matrix_a = np.array(matrix)
    print( "Матрица:\n", matrix)
    rank = np.linalg.matrix_rank(matrix)
    print("Ранг матрицы:\n", rank)
print("Введите матрицу А")
matrix_A = compiling_matrices()
print("Введите матрицу B")
matrix_B = compiling_matrices()
a = np.dot(matrix_A,matrix_B)
print("Произведение матриц A на В\n", a)