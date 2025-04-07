def lu_decomposition(A):
    n = len(A)
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum_ = 0.0
            for j in range(i):
                sum_ += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum_

        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0 
            else:
                sum_ = 0.0
                for j in range(i):
                    sum_ += L[k][j] * U[j][i]
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

def forward_substitution(L, b):
    n = len(L)
    y = [0.0 for _ in range(n)]
    
    for i in range(n):
        sum_ = 0.0
        for j in range(i):
            sum_ += L[i][j] * y[j]
        y[i] = (b[i] - sum_) / L[i][i]
    
    return y

def backward_substitution(U, y):
    n = len(U)
    x = [0.0 for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        sum_ = 0.0
        for j in range(i+1, n):
            sum_ += U[i][j] * x[j]
        x[i] = (y[i] - sum_) / U[i][i]
    
    return x

def solve_system_with_lu(A, b):
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

A = [
    [2.0, -1.0, 3.0],
    [1.0, 2.0, 1.0],
    [3.0, 0.0, -1.0]
]

b = [9.0, 8.0, 3.0]

solution = solve_system_with_lu(A, b)

print("Решение системы:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
