def gauss_rectangle_method(matrix, verbose=False):
    n = len(matrix)
    
    # Прямой ход
    for k in range(n):
        if verbose:
            print(f"\nШаг {k+1}:")
            print("Исходная матрица:")
            for row in matrix:
                print([f"{x:.4f}" for x in row])
        
        max_row = k
        max_val = abs(matrix[k][k])
        for i in range(k+1, n):
            if abs(matrix[i][k]) > max_val:
                max_val = abs(matrix[i][k])
                max_row = i
        
        if max_row != k:
            matrix[k], matrix[max_row] = matrix[max_row], matrix[k]
            if verbose:
                print(f"Перестановка строк {k+1} и {max_row+1}")
        
        for i in range(k+1, n):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, n+1):
                matrix[i][j] -= factor * matrix[k][j]
        
        if verbose:
            print("Матрица после исключения:")
            for row in matrix:
                print([f"{x:.4f}" for x in row])
    
    # Обратный ход
    x = [0] * n
    for k in range(n-1, -1, -1):
        x[k] = matrix[k][n]
        for j in range(k+1, n):
            x[k] -= matrix[k][j] * x[j]
        x[k] /= matrix[k][k]
    
    return x, matrix

a = [
    [2,  1,  4,   16],
    [3,  2,  1,   10],
    [1,  3,  3,  16]
]


solution, transformed = gauss_rectangle_method(a, verbose=True)
    
print("\nТреугольная матрица:")
for row in transformed:
    print([f"{x:.6f}" for x in row])
    
print("\nРешение:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
