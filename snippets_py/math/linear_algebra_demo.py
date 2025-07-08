# 🧩 Vector addition, subtraction, and scalar multiplication
def add_vectors(a, b):
    """Add two vectors (lists/tuples)."""
    return [x + y for x, y in zip(a, b)]


def subtract_vectors(a, b):
    """Subtract two vectors."""
    return [x - y for x, y in zip(a, b)]


def scalar_multiply_vector(scalar, v):
    """Multiply vector by scalar."""
    return [scalar * x for x in v]


# Examples
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Add: {add_vectors(a, b)}")  # [5, 7, 9]
print(f"Subtract: {subtract_vectors(a, b)}")  # [-3, -3, -3]
print(f"Scalar multiply: {scalar_multiply_vector(2, a)}")  # [2, 4, 6]


# 🧩 Dot product and cross product
def dot_product(a, b):
    """Calculate dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def cross_product(a, b):
    """Calculate cross product of two 3D vectors."""
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


# Examples
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Dot: {dot_product(a, b)}")  # 32
print(f"Cross: {cross_product(a, b)}")  # [-3, 6, -3]


# 🧩 Vector norm, length, and normalization
import math


def vector_norm(v):
    """Calculate Euclidean norm (length) of vector."""
    return math.sqrt(sum(x**2 for x in v))


def normalize_vector(v):
    """Normalize vector to unit length."""
    norm = vector_norm(v)
    if norm == 0:
        return v
    return [x / norm for x in v]


# Examples
v = [3, 4]
print(f"Norm: {vector_norm(v)}")  # 5.0
print(f"Normalized: {normalize_vector(v)}")  # [0.6, 0.8]


# 🧩 Matrix addition, subtraction, and scalar multiplication
def add_matrices(A, B):
    """Add two matrices (lists of lists)."""
    return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]


def subtract_matrices(A, B):
    """Subtract two matrices."""
    return [[a - b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]


def scalar_multiply_matrix(scalar, M):
    """Multiply matrix by scalar."""
    return [[scalar * x for x in row] for row in M]


# Examples
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f"Add: {add_matrices(A, B)}")  # [[6, 8], [10, 12]]
print(f"Subtract: {subtract_matrices(A, B)}")  # [[-4, -4], [-4, -4]]
print(f"Scalar multiply: {scalar_multiply_matrix(2, A)}")  # [[2, 4], [6, 8]]


# 🧩 Matrix multiplication and transpose
def matrix_multiply(A, B):
    """Multiply two matrices."""
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result


def transpose_matrix(M):
    """Transpose a matrix."""
    return [list(row) for row in zip(*M)]


# Examples
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(f"Multiply: {matrix_multiply(A, B)}")  # [[4, 4], [10, 8]]
print(f"Transpose: {transpose_matrix(A)}")  # [[1, 3], [2, 4]]


# 🧩 Identity, zero, and diagonal matrices
def identity_matrix(n):
    """Create n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def zero_matrix(rows, cols):
    """Create zero matrix of given size."""
    return [[0 for _ in range(cols)] for _ in range(rows)]


def diagonal_matrix(diagonal):
    """Create diagonal matrix from list."""
    n = len(diagonal)
    return [[diagonal[i] if i == j else 0 for j in range(n)] for i in range(n)]


# Examples
print(f"Identity: {identity_matrix(3)}")  # 3x3 identity
print(f"Zero: {zero_matrix(2, 3)}")  # 2x3 zero matrix
print(f"Diagonal: {diagonal_matrix([1, 2, 3])}")  # 3x3 diagonal


# 🧩 Determinant and inverse (2x2, 3x3)
def determinant_2x2(M):
    """Calculate determinant of 2x2 matrix."""
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def determinant_3x3(M):
    """Calculate determinant of 3x3 matrix."""
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h


def inverse_2x2(M):
    """Calculate inverse of 2x2 matrix."""
    det = determinant_2x2(M)
    if det == 0:
        raise ValueError("Matrix is singular")
    return [[M[1][1] / det, -M[0][1] / det], [-M[1][0] / det, M[0][0] / det]]


# Examples
A = [[4, 7], [2, 6]]
print(f"Determinant 2x2: {determinant_2x2(A)}")  # 10
print(f"Inverse 2x2: {inverse_2x2(A)}")  # [[0.6, -0.7], [-0.2, 0.4]]


# 🧩 Handle edge cases in linear algebra
def inverse_2x2(M):
    # Function is defined in one of the above code block
    pass


def matrix_multiply(A, B):
    # Function is defined in one of the above code block
    pass


def robust_matrix_multiply(A, B):
    """Matrix multiplication with error handling."""
    try:
        return matrix_multiply(A, B)
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_inverse_2x2(M):
    """Safe inverse calculation with singular check."""
    try:
        return inverse_2x2(M)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test edge cases
print(robust_matrix_multiply([[1, 2]], [[1, 2], [3, 4]]))  # None (dimension mismatch)
print(safe_inverse_2x2([[1, 2], [2, 4]]))  # None (singular)


# 🧩 Performance comparison
import time


def matrix_multiply(A, B):
    # Function is defined in one of the above code block
    pass


def benchmark_matrix_multiply():
    """Benchmark matrix multiplication."""
    A = [[i for i in range(10)] for _ in range(10)]
    B = [[i for i in range(10)] for _ in range(10)]
    n = 1000

    start = time.time()
    for _ in range(n):
        matrix_multiply(A, B)
    elapsed = time.time() - start
    print(f"Matrix multiply: {elapsed:.4f}s")


# benchmark_matrix_multiply()


# 🧩 Solve system of linear equations (2x2)
def solve_2x2_system(a, b, c, d, e, f):
    """Solve system: ax + by = e, cx + dy = f."""
    det = a * d - b * c
    if det == 0:
        raise ValueError("No unique solution")
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det
    return x, y


# Example
x, y = solve_2x2_system(2, 1, 1, -1, 1, 0)
print(f"Solution: x={x}, y={y}")
