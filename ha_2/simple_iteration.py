def simple_iteration_method(x, arr, e=1e-5):
    n = len(arr) - 1

    def f(x):
        value = 0
        for i in range(n + 1):
            value += arr[i] * x**i
        return value

    def g(x):
        return (6 + x**2) / 5

    while True:
        try:
            x_new = g(x)
        except OverflowError:
            raise ValueError("Переполнение: метод простых итераций не сходится.")

        if abs(x_new - x) < e:
            print(f"Корень: {x_new}")
            return x_new
        x = x_new



x0 = 1  
coefficients = [6, -5, 1]  

print(f"Корень: {simple_iteration_method(x0, coefficients)}")