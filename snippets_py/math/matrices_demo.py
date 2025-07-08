# 🧩 Matrix creation and display
def create_matrix(rows, cols, fill=0):
    """Create a matrix (list of lists) with given dimensions and fill value."""
    return [[fill for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """Pretty-print a matrix."""
    for row in matrix:
        print(" ".join(str(x) for x in row))


# Examples
m = create_matrix(2, 3, 1)
print_matrix(m)
# 1 1 1
# 1 1 1


# 🧩 Matrix addition and subtraction
def add_matrices(a, b):
    """Add two matrices elementwise."""
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def subtract_matrices(a, b):
    """Subtract two matrices elementwise."""
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


# Examples
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(add_matrices(A, B))  # [[6, 8], [10, 12]]
print(subtract_matrices(A, B))  # [[-4, -4], [-4, -4]]


# 🧩 Matrix multiplication (dot product)
def create_matrix(rows, cols, fill=0):
    # Function is defined in one of the above code block
    pass


def multiply_matrices(a, b):
    """Multiply two matrices (dot product)."""
    result = create_matrix(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
    return result


# Examples
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(multiply_matrices(A, B))  # [[4, 4], [10, 8]]


# 🧩 Matrix transpose
def transpose_matrix(matrix):
    """Transpose a matrix (swap rows and columns)."""
    return [list(row) for row in zip(*matrix)]


# Examples
A = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(A))  # [[1, 4], [2, 5], [3, 6]]


# 🧩 Identity, zero, and diagonal matrices
def create_matrix(rows, cols, fill=0):
    # Function is defined in one of the above code block
    pass


def identity_matrix(n):
    """Create an n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def zero_matrix(rows, cols):
    """Create a zero matrix."""
    return create_matrix(rows, cols, 0)


def diagonal_matrix(diag):
    """Create a diagonal matrix from a list of diagonal elements."""
    n = len(diag)
    return [[diag[i] if i == j else 0 for j in range(n)] for i in range(n)]


# Examples
print(identity_matrix(3))  # [[1,0,0],[0,1,0],[0,0,1]]
print(zero_matrix(2, 2))  # [[0,0],[0,0]]
print(diagonal_matrix([1, 2, 3]))  # [[1,0,0],[0,2,0],[0,0,3]]


# 🧩 Determinant (2x2, 3x3)
def determinant_2x2(m):
    """Determinant of a 2x2 matrix."""
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def determinant_3x3(m):
    """Determinant of a 3x3 matrix."""
    return (
        m[0][0] * m[1][1] * m[2][2]
        + m[0][1] * m[1][2] * m[2][0]
        + m[0][2] * m[1][0] * m[2][1]
        - m[0][2] * m[1][1] * m[2][0]
        - m[0][0] * m[1][2] * m[2][1]
        - m[0][1] * m[1][0] * m[2][2]
    )


# Examples
M2 = [[1, 2], [3, 4]]
M3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
print(determinant_2x2(M2))  # -2
print(determinant_3x3(M3))  # -306


# 🧩 Inverse (2x2)
def determinant_2x2(m):
    # Function is defined in one of the above code block
    pass


def inverse_2x2(m):
    """Inverse of a 2x2 matrix."""
    det = determinant_2x2(m)
    if det == 0:
        raise ValueError("Singular matrix")
    return [[m[1][1] / det, -m[0][1] / det], [-m[1][0] / det, m[0][0] / det]]


# Examples
M = [[4, 7], [2, 6]]
print(inverse_2x2(M))  # [[0.6, -0.7], [-0.2, 0.4]]


# 🧩 Handle invalid matrices
def add_matrices(a, b):
    # Function is defined in one of the above code block
    pass


def safe_add_matrices(a, b):
    """Add matrices, return None on error."""
    try:
        return add_matrices(a, b)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Examples
print(safe_add_matrices([[1, 2]], [[1, 2], [3, 4]]))  # Error, returns None


# 🧩 Performance comparison
import time


def create_matrix(rows, cols, fill=0):
    # Function is defined in one of the above code block
    pass


def add_matrices(a, b):
    # Function is defined in one of the above code block
    pass


def benchmark_matrix_addition():
    """Benchmark matrix addition."""
    n = 1000
    A = create_matrix(n, n, 1)
    B = create_matrix(n, n, 2)
    start = time.time()
    add_matrices(A, B)
    print(f"Addition: {time.time() - start:.6f}s")


# benchmark_matrix_addition()


# 🧩 Solving systems of equations (2x2)
def solve_2x2(a, b, c, d, e, f):
    """Solve ax + by = e, cx + dy = f for x, y."""
    det = a * d - b * c
    if det == 0:
        raise ValueError("No unique solution")
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det
    return x, y


# Examples
print(solve_2x2(2, 1, 1, -1, 1, 0))  # (1.0, -1.0)
