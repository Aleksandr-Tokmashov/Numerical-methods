import numpy as np

def simple_iteration_method(A, b, epsilon=1e-6, max_iterations=1000, norm_type='3'):
    n = len(b)
    x = np.zeros(n)
    
    alpha = np.eye(n) - A
    beta = b.copy()
    
    if norm_type == '1':
        matrix_norm = lambda mat: np.max(np.sum(np.abs(mat), axis=0))
        vector_norm = lambda vec: np.max(np.abs(vec))
    elif norm_type == '2':
        matrix_norm = lambda mat: np.max(np.sum(np.abs(mat), axis=1))
        vector_norm = lambda vec: np.sum(np.abs(vec))
    else:
        matrix_norm = lambda mat: np.sqrt(np.sum(mat**2))
        vector_norm = lambda vec: np.sqrt(np.sum(vec**2))
    
    alpha_norm = matrix_norm(alpha)
    if alpha_norm >= 1:
        print(f"Норма матрицы alpha ({alpha_norm}) >= 1")
    
    for k in range(max_iterations):
        x_old = x.copy()
        x = alpha @ x_old + beta
        
        delta = vector_norm(x - x_old)
        if delta < epsilon:
            print(f"Итерация {k+1}: достигнута точность {delta:.2e}")
            break
    
    return x, k+1


if __name__ == "__main__":
    A = np.array([
        [4, -1, 1],
        [-1, 5, 2],
        [1, 2, 4]
    ], dtype=float)
    
    b = np.array([6, 12, 15], dtype=float)
    
    print("Исходная матрица A:")
    print(A)
    print("\nВектор b:")
    print(b)
    
    # Нормализуем систему
    n = len(b)
    for i in range(n):
        divisor = A[i, i]
        A[i, :] /= divisor
        b[i] /= divisor
    
    print("\nПреобразованная матрица A (нормированная):")
    print(A)
    print("\nПреобразованный вектор b:")
    print(b)

    
    # Решаем систему с разными нормами для сравнения
    print("\nРешаем систему с евклидовой нормой (норма 3):")
    solution, iterations = simple_iteration_method(A, b, epsilon=1e-6, norm_type='3')
    print(f"Решение: {solution}")
    print(f"Количество итераций: {iterations}")
    
    print("\nРешаем систему с нормой 1:")
    solution, iterations = simple_iteration_method(A, b, epsilon=1e-6, norm_type='1')
    print(f"Решение: {solution}")
    print(f"Количество итераций: {iterations}")
    
    print("\nРешаем систему с нормой 2:")
    solution, iterations = simple_iteration_method(A, b, epsilon=1e-6, norm_type='2')
    print(f"Решение: {solution}")
    print(f"Количество итераций: {iterations}")