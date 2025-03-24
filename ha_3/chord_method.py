def chord_method(a, b, arr, e=1e-5):
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

    def d2f(x):
        value = 0
        for i in range(2, n + 1):
            value += i * (i - 1) * arr[i] * x**(i - 2)
        return value

    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала.")

    if fa * d2f(a) > 0:
        fixed_point = a
        moving_point = b
    else:
        fixed_point = b
        moving_point = a

    while True:
        fx_fixed = f(fixed_point)
        fx_moving = f(moving_point)

        if fixed_point == a:
            new_point = moving_point - (fx_moving * (moving_point - fixed_point)) / (fx_moving - fx_fixed)
        else:
            new_point = moving_point - (fx_moving * (fixed_point - moving_point)) / (fx_fixed - fx_moving)

        f_new = f(new_point)

        if abs(f_new) < e:
            return new_point

        moving_point = new_point


a, b = -2, 0
coefficients = [5, 0, 1, 0, 2, 3] 
print(f"Корень: {chord_method(a, b, coefficients)}")