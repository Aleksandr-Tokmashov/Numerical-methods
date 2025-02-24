def newton_method(x, arr, e=1e-5):
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
            raise ValueError("Производная равна нулю, метод Ньютона не сходится.")

        x = x - fx / dfx

x0 = 1
coefficients = [5, 0, 1, 0, 2, 3]

print(f"Корень: {newton_method(x0, coefficients)}")
