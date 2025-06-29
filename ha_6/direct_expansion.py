import numpy as np
from numpy.linalg import eig

def characteristic_polynomial(A):
    n = A.shape[0]
    E = np.eye(n)
    
    if n == 2:
        return [1, -np.trace(A), np.linalg.det(A)]
    elif n == 3:
        return [1, -np.trace(A), 
                (np.trace(A)**2 - np.trace(A @ A))/2, 
                -np.linalg.det(A)]
    else:
        # Для матриц большего размера используем встроенную функцию numpy
        return np.poly(A)

def find_eigenvalues(A, tol=1e-6):
    coeffs = characteristic_polynomial(A)
    roots = np.roots(coeffs)
    return np.array([np.real(root) if np.abs(np.imag(root)) < tol else root for root in roots])

def find_eigenvectors(A, eigenvalues, tol=1e-6):
    n = A.shape[0]
    eigenvectors = []
    
    for λ in eigenvalues:
        # Создаем матрицу (A - λE)
        M = A - λ * np.eye(n)
        
        # Находим ядро матрицы (решаем (A - λE)x = 0)
        _, s, vh = np.linalg.svd(M)
        # Находим количество нулевых сингулярных значений
        null_space = np.sum(s < tol)
        
        # Берем последние null_space строк vh как базис ядра
        basis = vh[-null_space:].T
        
        # Нормализуем векторы
        for i in range(basis.shape[1]):
            basis[:, i] = basis[:, i] / np.linalg.norm(basis[:, i])
        
        eigenvectors.append(basis)
    
    return eigenvectors

def direct_expansion_method(A, tol=1e-6):
    # 1. Находим собственные значения
    eigenvalues = find_eigenvalues(A, tol)
    
    # 2. Находим собственные векторы для каждого значения
    eigenvectors = find_eigenvectors(A, eigenvalues, tol)
    
    return eigenvalues, eigenvectors

# Пример использования
if __name__ == "__main__":
    A = np.array([[4, -1, 1],
                  [-1, 5, 2],
                  [1, 2, 4]], dtype=float)
    
    print("Исходная матрица A:")
    print(A)
    
    print("\nРезультаты нашего метода:")
    eigenvalues, eigenvectors = direct_expansion_method(A)
    
    print("\nСобственные значения:")
    for i, λ in enumerate(eigenvalues):
        print(f"λ_{i+1} = {λ:.6f}")
    
    print("\nСобственные векторы:")
    for i, vecs in enumerate(eigenvectors):
        print(f"Для λ_{i+1} = {eigenvalues[i]:.6f}:")
        for j in range(vecs.shape[1]):
            print(f"  Вектор {j+1}: {vecs[:, j]}")
