import numpy as np

def power_iteration(A, epsilon=1e-6, max_iterations=1000):
    n = A.shape[0]
    
    # 1. Выбираем произвольное начальное приближение вектора
    x = np.random.rand(n)
    x = x / np.linalg.norm(x)  # Нормализуем вектор
    
    prev_eigenvalue = 0
    iterations = 0
    
    for k in range(max_iterations):
        # 2. Умножаем матрицу на текущий вектор
        x_new = A @ x
        
        # 3. Находим приближение собственного значения (через отношение Рэлея)
        eigenvalue = np.dot(x_new, x) / np.dot(x, x)
        
        # 4. Нормализуем вектор
        x_new = x_new / np.linalg.norm(x_new)
        
        # 5. Проверяем условие остановки
        if np.abs(eigenvalue - prev_eigenvalue) < epsilon:
            break
            
        # Обновляем значения для следующей итерации
        x = x_new
        prev_eigenvalue = eigenvalue
        iterations += 1
    
    return eigenvalue, x, iterations

# Пример использования
if __name__ == "__main__":
    A = np.array([[4, -1, 1],
                  [-1, 5, 2],
                  [1, 2, 4]], dtype=float)
    
    print("Исходная матрица A:")
    print(A)
    
    print("\nПрименение степенного метода:")
    eigenvalue, eigenvector, iterations = power_iteration(A)
    
    print(f"Найденное доминирующее собственное значение: {eigenvalue:.6f}")
    print(f"Соответствующий собственный вектор: {eigenvector}")
    print(f"Количество итераций: {iterations}")