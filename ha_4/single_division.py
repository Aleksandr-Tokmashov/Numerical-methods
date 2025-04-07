def single_division_method(matrix):
    n = len(matrix)
    
    # Прямой ход метода Гаусса
    for k in range(n):
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
    
    return x

a = [
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
]

solution = single_division_method(a)
print("Решение системы:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.4f}")