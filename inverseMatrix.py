


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    det -= matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    det += matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    return det

def inverse_matrix_3x3(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        return "Die Matrix ist nicht invertierbar."
    else:
        inverse = [[0]*3 for _ in range(3)]
        inverse[0][0] = (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) / det
        inverse[0][1] = (matrix[0][2]*matrix[2][1] - matrix[0][1]*matrix[2][2]) / det
        inverse[0][2] = (matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]) / det
        inverse[1][0] = (matrix[1][2]*matrix[2][0] - matrix[1][0]*matrix[2][2]) / det
        inverse[1][1] = (matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0]) / det
        inverse[1][2] = (matrix[0][2]*matrix[1][0] - matrix[0][0]*matrix[1][2]) / det
        inverse[2][0] = (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]) / det
        inverse[2][1] = (matrix[0][1]*matrix[2][0] - matrix[0][0]*matrix[2][1]) / det
        inverse[2][2] = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) / det
        return inverse

# Beispiel-Matrix
matrix = [[4, -2, 2],
          [2, 0, 6],
          [-1, 3, 3]]

# Berechnung der inversen Matrix
inverse = inverse_matrix_3x3(matrix)
print("Inverse Matrix:")
for row in inverse:
    print(row)
