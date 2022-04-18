from tools import Matrix, Vector
import tools

# инициализация векторов
v_a = Vector([1, 2, 3])

v_b = Vector([4, 5, 6])

# инициализация матриц
m_a = Matrix([[3, 1, 1],
              [1, 5, 1],
              [1, 1, 7]])

m_b = Matrix([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m_c = Matrix([[0, 2, 3],
              [1, 2, 4],
              [4, 5, 6]])

m_d = Matrix([[1, 2, 3]])

# умножение вектора на число
# 2
# 4
# 6
print(v_a * float(2))
print()

# умножение вектора на строку
# 1 2 3
# 2 4 6
# 3 6 9
print(v_a * m_d)
print()

# деление вектора на число
# 0.5
# 1
# 1.5
print(v_a / float(2))
print()

# сложение векторов
# 5
# 7
# 9
print(v_a + v_b)
print()

# вычитание векторов
# -3
# -3
# -3
print(v_a - v_b)
print()

# транспонирование вектора
# 1 2 3
print(v_a.transpose)
print()

# евклидова норма вектора
# 3.74
print('%.2f' % v_a.norm)
print()

# инициализация вектора с помощью вектора
v_c = Vector(v_a)
v_c[0] = -100
print(v_a)
print(v_c)
print()

# cut вектора
# 2
# 3
v_c.cut(1)
print(v_c)
print()

# умножение квадратной матрицы на число
# 6 2  2
# 2 10 2
# 2 2  14
print(m_a * float(2))
print()

# умножение квадратной матрицы на матрицу
# 14 19 24
# 28 35 42
# 54 63 72
print(m_a * m_b)
print()

# умножение квадратной матрицы на вектор
# 8
# 14
# 24
print(m_a * v_a)
print()

# умножение строки на вектор
# 14
print(m_d * v_a)
print()

# деление квадратной матрицы на число
# 1.5 0.5 0.5
# 0.5 2.5 0.5
# 0.5 0.5 3.5
print(m_a / float(2))
print()

# сложение квадратных матриц
# 4 3  4
# 5 10 7
# 8 9  16
print(m_a + m_b)
print()

# вычитание квадратных матриц
#  2 -1 -2
# -3  0 -5
# -6 -7 -2
print(m_a - m_b)
print()

# евклидова норма матрицы
# 9.43
print('%.2f' % m_a.norm(0))
print()

# транспонирование строки
# 1
# 2
# 3
print(m_d.transpose)
print()

# транспонирование матрицы
print(m_b.transpose)
print()
# 1 4 7
# 2 5 8
# 3 6 9

# инициализация матрица с помощью матрицы
m_e = Matrix(m_a)
m_e[0, 0] = -100
print(m_a)
print(m_e)
print()

# cut матрицы
m_e.cut(1)
print(m_e)
print()

# создать орт
# 1
# 0
# 0
print(tools.ort(3, 0))
print()

# создать нулевую матрицу
# 0 0 0
# 0 0 0
# 0 0 0
print(tools.zeros(3))
print()

# создать единичную матрицу
# 1 0 0
# 0 1 0
# 0 0 1
print(tools.eye(3))
print()

# расширить матрицу единицами
# 1 0 0 0
# 0 3 1 1
# 0 1 5 1
# 0 1 1 7
print(tools.extend(m_a, 4))
print()

# получить вектор по индексу
print(tools.column(m_a, 0))
print()
# 3
# 1
# 1

# перестановки
# 0 1 0
# 1 0 0
# 0 0 1
print(m_c.permutation)
print()

# убрать нули главной диагонали
m_f, v_d = tools.permutation(m_c, v_a)
print(m_f)
print(v_d)
