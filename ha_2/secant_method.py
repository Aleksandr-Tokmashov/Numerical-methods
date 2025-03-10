def secant_method(x0, x1, arr, e=1e-5):
    n = len(arr) - 1

    def f(x):
        value = 0
        for i in range(n + 1):
            value += arr[i] * x**i
        return value

    while True:
        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1) < e:
            print(f"Корень: {x1}")
            return x1

        if fx1 == fx0:
            raise ValueError("Деление на ноль, метод секущих не сходится.")

        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_new

x0 = 1
x1 = 2
coefficients = [6, -5, 1]

print(f"Корень: {secant_method(x0, x1, coefficients)}")