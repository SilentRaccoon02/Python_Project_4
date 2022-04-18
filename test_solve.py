from tools import Matrix, Vector
import solve

m_a = Matrix([[1, 2, 4],
              [0, 3, 5],
              [0, 0, 6]])

m_b = Matrix([[1, 0, 0],
              [2, 4, 0],
              [3, 5, 6]])

v_a = Vector([7, 7, 7])

# top
# 1.56
# 0.39
# 1.17
print(solve.top(m_a, v_a))
print()

# bottom
# 7
# -1.75
# -0.875
print(solve.bottom(m_b, v_a))
