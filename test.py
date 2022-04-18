from tools import Matrix, Vector
from simple_iteration import simple_iteration
from Seidel import seidel
from LU import lu
from QR import qr


def test():
    a = Matrix([[0, 2, 3],
                [1, 2, 4],
                [4, 5, 6]])

    b = Vector([13, 17, 32])

    print(simple_iteration(a, b))
    print()
    print(seidel(a, b))
    print()
    print(lu(a, b))
    print()
    print(qr(a, b))


if __name__ == '__main__':
    test()
