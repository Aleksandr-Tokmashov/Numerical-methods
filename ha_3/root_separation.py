def R(coefficients):
    an = coefficients[0]
    if an <= 0:
        raise ValueError("a_n должен быть положительным")

    i = 0
    C = 0
    
    for index, ai in enumerate(coefficients):
        if ai < 0:
            if i == 0:
                i = index
            if abs(ai) > C:
                C = abs(ai)
    
    if C == 0:
        return 0
    
    n = len(coefficients) - 1
    k = n - i
    
    return 1 + (C / an) ** (1 / k)

def calculate_x(coefficients):
    n = len(coefficients) - 1
    
    P1 = coefficients[::-1]
    P2 = [coeff * (-1)**(n-i) for i, coeff in enumerate(coefficients)]
    P3 = [coeff * (-1)**i for i, coeff in enumerate(coefficients[::-1])]
    
    if P1[0] <= 0:
        P1 = [-coeff for coeff in P1]
    R1 = R(P1)
    
    if P2[0] <= 0:
        P2 = [-coeff for coeff in P2]
    R2 = R(P2)
    
    if P3[0] <= 0:
        P3 = [-coeff for coeff in P3]
    R3 = R(P3)
    
    Rn = R(coefficients)
    
    return {
        f'{1/R1} <= x-полож <= {Rn}',
        f'{-1*R2} <= x-отриц <= {-1/R3}',
    }

arr = [1, 2, -5, 8, -7, -3]
print(R(arr))
print(calculate_x(arr))