import numpy as np

def rotation_method(A, epsilon=1e-6, max_iterations=1000):
    n = A.shape[0]
    
    # Проверяем, что матрица симметрична
    if not np.allclose(A, A.T):
        raise ValueError("Матрица должна быть симметричной")
    
    A_k = A.copy()
    H_product = np.eye(n) 
    iterations = 0
    
    for _ in range(max_iterations):
        # Находим максимальный внедиагональный элемент
        max_val = 0
        p, q = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(A_k[i,j]) > max_val:
                    max_val = abs(A_k[i,j])
                    p, q = i, j
        
        # Проверяем условие остановки
        if max_val < epsilon:
            break
        
        # Вычисляем угол поворота
        if np.isclose(A_k[p,p], A_k[q,q]):
            phi = np.pi/4
        else:
            phi = 0.5 * np.arctan(2*A_k[p,q] / (A_k[p,p] - A_k[q,q]))
        
        # Создаем матрицу вращения
        c = np.cos(phi)
        s = np.sin(phi)
        H = np.eye(n)
        H[p,p] = c
        H[p,q] = -s
        H[q,p] = s
        H[q,q] = c
        
        # Вычисляем новую матрицу
        A_k = H.T @ A_k @ H
        
        # Обновляем произведение матриц вращения
        H_product = H_product @ H
        
        iterations += 1
    
    # Собственные значения - диагональные элементы
    eigenvalues = np.diag(A_k)
    
    # Собственные векторы - столбцы произведения матриц вращения
    eigenvectors = H_product
    
    return eigenvalues, eigenvectors, iterations

# Пример использования
if __name__ == "__main__":
    A = np.array([[4, -1, 1],
                  [-1, 5, 2],
                  [1, 2, 4]], dtype=float)
    
    print("Исходная матрица A:")
    print(A)
    
    # Применяем метод вращений Якоби
    eigenvalues, eigenvectors, iterations = rotation_method(A)
    
    print("\nРезультаты метода вращений Якоби:")
    print(f"Количество итераций: {iterations}")
    print(f"Собственные значения: {eigenvalues}")
    print("Собственные векторы (в столбцах):")
    print(eigenvectors)
    