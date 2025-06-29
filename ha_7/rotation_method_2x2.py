import numpy as np

def rotation_method_2x2(A, epsilon=1e-6):
    # Проверяем, что матрица симметрична
    if not np.allclose(A, A.T):
        raise ValueError("Матрица должна быть симметричной")
    
    # Для матрицы 2x2 достаточно одной итерации
    k = 0
    A_k = A.copy()
    H_product = np.eye(2)  
    
    # Находим максимальный внедиагональный элемент
    i, j = 0, 1 
    
    if np.abs(A_k[i,j]) > epsilon:
        # Вычисляем угол поворота
        if np.isclose(A_k[i,i], A_k[j,j]):
            phi = np.pi/4
        else:
            phi = 0.5 * np.arctan(2*A_k[i,j] / (A_k[i,i] - A_k[j,j]))
        
        # Создаем матрицу вращения
        c = np.cos(phi)
        s = np.sin(phi)
        H = np.array([[c, -s], [s, c]])
        
        # Вычисляем новую матрицу
        A_k = H.T @ A_k @ H
        
        # Обновляем произведение матриц вращения
        H_product = H_product @ H
    else:
        pass
    
    # Собственные значения - диагональные элементы
    eigenvalues = np.array([A_k[0,0], A_k[1,1]])
    
    # Собственные векторы - столбцы произведения матриц вращения
    eigenvectors = H_product
    
    return eigenvalues, eigenvectors

# Пример использования
if __name__ == "__main__":
    A = np.array([[4, 1],
                  [1, 3]], dtype=float)
    
    print("Исходная матрица A:")
    print(A)
    
    eigenvalues, eigenvectors = rotation_method_2x2(A)
    
    print("\nРезультаты метода вращений Якоби:")
    print(f"Собственные значения: {eigenvalues}")
    print("Собственные векторы (в столбцах):")
    print(eigenvectors)