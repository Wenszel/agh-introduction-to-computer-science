import numpy as np


def determinant(matrix: list) -> int:
    """ The function returns the determinant of a given square matrix using the Laplace Expansion """
    degree = len(matrix)
    if degree == 1:
        return matrix[0][0]
    columns = [i for i in range(degree)]
    total = 0
    for col in columns:
        sub_matrix = [[matrix[r][c] for c in range(degree) if c != col] for r in range(1, degree)]
        total += matrix[0][col] * (-1) ** col * determinant(sub_matrix)
    return total


t = [[1, 2, 3], [4, 5, 1], [2, 3, 4]]
print("For the given matrix:\n", np.array(t))
print("The determinant is: ", determinant(t))
