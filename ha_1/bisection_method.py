def bisection_method(a, b, arr, e=1e-5):
    n = len(arr) - 1

    def f(x):
        value = 0
        for i in range(n + 1):
            value += arr[i] * x**i
        return value

    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала.")

    while True:
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < e or (b - a) / 2 < e:
            print(f"Корень: {c}")
            return c

        if fc * f(a) < 0:
            b = c
        else:
            a = c


a, b = -2, 0

coefficients = [5, 0, 1, 0, 2, 3]
print(f"Корень: {bisection_method(a, b, coefficients)}")
