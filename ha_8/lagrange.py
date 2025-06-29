import numpy as np

# Глобальный многочлен
def lagrange_global(x_nodes, y_nodes, x):
    n = len(x_nodes)
    y = 0.0
    
    for i in range(n):
        # Вычисляем базисный полином Лагранжа L_i(x)
        li = 1.0
        for j in range(n):
            if j != i:
                li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        y += y_nodes[i] * li
    
    return y

# Пример использования
x_nodes = np.array([1.0, 2.0, 4.0, 5.0])  # Неравномерная сетка
y_nodes = np.array([1.0, 4.0, 16.0, 25.0])  # Функция y = x^2

x = 3.0
y_interp = lagrange_global(x_nodes, y_nodes, x)
print(f"Глобальная интерполяция в точке x = {x}: {y_interp}")
print(f"Точное значение: {x**2}")

# Кусочный многочлен
def lagrange_piecewise(x_nodes, y_nodes, x, k=2):
    n = len(x_nodes)
    
    # Находим индекс отрезка, содержащего x
    idx = 0
    while idx < n - 1 and x > x_nodes[idx + 1]:
        idx += 1
    
    # Определяем окно интерполяции
    left = max(0, idx - k//2)
    right = min(n - 1, left + k)
    left = max(0, right - k)
    
    # Выбираем узлы для интерполяции
    interp_nodes = x_nodes[left:right+1]
    interp_values = y_nodes[left:right+1]
    
    # Применяем глобальный метод к выбранным узлам
    return lagrange_global(interp_nodes, interp_values, x)

# Пример использования
x = 3.0
y_interp_piecewise = lagrange_piecewise(x_nodes, y_nodes, x, k=2)
print(f"\nКусочная интерполяция (k=2) в точке x = {x}: {y_interp_piecewise}")

def finite_differences(y_nodes):
    """
    Вычисление конечных разностей
    
    Параметры:
    y_nodes - значения функции в узлах
    
    Возвращает:
    diff_table - таблица конечных разностей
    """
    n = len(y_nodes)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y_nodes
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i,j] = diff_table[i+1,j-1] - diff_table[i,j-1]
    
    return diff_table

# Глобальный многочлен Ньютона для равномерной сетки
def newton_global_uniform(x_nodes, y_nodes, x):
    n = len(x_nodes)
    h = x_nodes[1] - x_nodes[0]  # шаг сетки
    t = (x - x_nodes[0]) / h
    
    # Вычисляем конечные разности
    diff_table = finite_differences(y_nodes)
    
    # Вычисляем значение многочлена Ньютона
    y = diff_table[0,0]
    product = 1.0
    
    for i in range(1, n):
        product *= (t - (i - 1)) / i
        y += diff_table[0,i] * product
    
    return y

# Пример с равномерной сеткой
x_uniform = np.array([1.0, 2.0, 3.0, 4.0])  # Равномерная сетка
y_uniform = np.array([1.0, 4.0, 9.0, 16.0])  # Функция y = x^2

x = 2.5
y_newton = newton_global_uniform(x_uniform, y_uniform, x)
print(f"\nГлобальная интерполяция Ньютона в точке x = {x}: {y_newton}")


# Кусочный многочлен Ньютона для равномерной сетки
def newton_piecewise_uniform(x_nodes, y_nodes, x, k=2):
    n = len(x_nodes)
    
    # Находим индекс отрезка, содержащего x
    idx = 0
    while idx < n - 1 and x > x_nodes[idx + 1]:
        idx += 1
    
    # Определяем окно интерполяции
    left = max(0, idx - k//2)
    right = min(n - 1, left + k)
    left = max(0, right - k)
    
    # Выбираем узлы для интерполяции
    interp_nodes = x_nodes[left:right+1]
    interp_values = y_nodes[left:right+1]
    
    # Применяем глобальный метод Ньютона к выбранным узлам
    return newton_global_uniform(interp_nodes, interp_values, x)

# Пример использования
x = 2.5
y_newton_piecewise = newton_piecewise_uniform(x_uniform, y_uniform, x, k=2)
print(f"\nКусочная интерполяция Ньютона (k=2) в точке x = {x}: {y_newton_piecewise}")