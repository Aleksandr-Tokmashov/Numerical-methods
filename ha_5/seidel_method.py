import numpy as np

def seidel_method(A, b, epsilon=1e-6, max_iterations=1000, norm_type='3'):
    n = len(b)
    x = np.zeros(n)
    
    if norm_type == '1':
        vector_norm = lambda vec: np.max(np.abs(vec))
    elif norm_type == '2':
        vector_norm = lambda vec: np.sum(np.abs(vec))
    else: 
        vector_norm = lambda vec: np.sqrt(np.sum(vec**2))
    
    iterations = 0
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])  
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        iterations += 1
        
        delta = vector_norm(x - x_old)
        if delta < epsilon:
            print(f"Итерация {iterations}: достигнута точность {delta:.2e}")
            break
    
    return x, iterations


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
    
    # Решаем систему методом Зейделя
    print("\nРешаем систему методом Зейделя с евклидовой нормой:")
    solution, iterations = seidel_method(A, b, epsilon=1e-6)
    print(f"Решение: {solution}")
    print(f"Количество итераций: {iterations}")