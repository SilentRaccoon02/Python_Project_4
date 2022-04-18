from tools import Matrix, Vector


# решить систему
# верхняя диагональ
def top(a: Matrix, b: Vector) -> Vector:
    if len(a) != len(b):
        raise ValueError('Incorrect data')

    n = len(a)
    x = Vector([0 for _ in range(n)])

    for i in range(n - 1, -1, -1):
        b_sum = b[i]

        for j in range(i + 1, n):
            b_sum -= a[i, j] * x[j]
        x[i] = b_sum / a[i, i]

    return x


# решить систему
# нижняя диагональ
def bottom(a: Matrix, b: Vector) -> Vector:
    if len(a) != len(b):
        raise ValueError('Incorrect data')

    n = len(a)
    x = Vector([0 for _ in range(n)])

    for i in range(n):
        b_sum = b[i]

        for j in range(0, i):
            b_sum -= a[i, j] * x[j]
        x[i] = b_sum / a[i, i]

    return x
