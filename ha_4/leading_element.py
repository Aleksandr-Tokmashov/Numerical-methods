def leading_element_method(matrix):
    n = len(matrix)
    
    for k in range(n):
        max_row = k
        max_val = abs(matrix[k][k])
        for i in range(k + 1, n):
            if abs(matrix[i][k]) > max_val:
                max_val = abs(matrix[i][k])
                max_row = i
       
        if max_row != k:
            matrix[k], matrix[max_row] = matrix[max_row], matrix[k]
        
        pivot = matrix[k][k]
        
        for j in range(k, n + 1):
            matrix[k][j] /= pivot
        
        for i in range(k + 1, n):
            factor = matrix[i][k]
            for j in range(k, n + 1):
                matrix[i][j] -= factor * matrix[k][j]
    
    # Обратный ход метода Гаусса
    x = [0] * n
    for k in range(n - 1, -1, -1):
        x[k] = matrix[k][n]
        for j in range(k + 1, n):
            x[k] -= matrix[k][j] * x[j]
    
    return x, matrix

a = [
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, 6]
]


solution, transformed_matrix = leading_element_method(a)
print("\nПреобразованная матрица:")
for line in transformed_matrix:
    print([f"{x:.4f}" for x in line])
    
print("\nРешение системы:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")