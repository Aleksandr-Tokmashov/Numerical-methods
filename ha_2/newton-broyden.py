def newton_broyden_method(x, arr, e=1e-5, c_k = 0.5):
    n = len(arr) - 1

    def f(x):
        value = 0
        for i in range(n + 1):
            value += arr[i] * x**i
        return value

    def df(x):
        value = 0
        for i in range(1, n + 1):
            value += i * arr[i] * x**(i - 1)
        return value

    while True:
        fx = f(x)
        if abs(fx) < e:
            print(f"Корень: {x}")
            return x

        dfx = df(x)
        if dfx == 0:
            raise ValueError("Производная равна нулю, метод Ньютона-Бройдена не сходится.")


        x_new = x - c_k * (fx / dfx)

        if abs(f(x_new)) < abs(fx):
            x = x_new
        else:
            c_k = 0.25
            x_new = x - c_k * (fx / dfx)
            if abs(f(x_new)) < abs(fx):
                x = x_new
            else:
                raise ValueError("Метод Ньютона-Бройдена не сходится.")

x0 = 1
coefficients =  [6, -5, 1]

print(f"Корень: {newton_broyden_method(x0, coefficients)}")