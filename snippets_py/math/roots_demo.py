# 🧩 Square root
def sqrt(x):
    """Compute the square root of x."""
    return x**0.5


# Examples
print(sqrt(9))  # 3.0
print(sqrt(2))  # 1.4142135623730951


# 🧩 Cube root
def cbrt(x):
    """Compute the cube root of x."""
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))


# Examples
print(cbrt(27))  # 3.0
print(cbrt(-8))  # -2.0


# 🧩 Nth root
def nth_root(x, n):
    """Compute the nth root of x."""
    if x < 0 and n % 2 == 1:
        return -((-x) ** (1 / n))
    elif x < 0:
        raise ValueError("Even root of negative number")
    return x ** (1 / n)


# Examples
print(nth_root(16, 4))  # 2.0
print(nth_root(-27, 3))  # -3.0


# 🧩 Roots of negative numbers (complex)
import cmath


def sqrt_complex(x):
    """Compute the square root, supporting complex results."""
    return cmath.sqrt(x)


def nth_root_complex(x, n):
    """Compute the nth root, supporting complex results."""
    return x ** (1 / n) if x.imag or x >= 0 else cmath.exp(cmath.log(x) / n)


# Examples
print(sqrt_complex(-1))  # 1j
print(nth_root_complex(-8, 3))  # (1+1.732j) (for complex input)


# 🧩 Integer roots and perfect powers
def is_perfect_square(x):
    """Check if x is a perfect square."""
    if x < 0:
        return False
    root = int(x**0.5)
    return root * root == x


def is_perfect_cube(x):
    """Check if x is a perfect cube."""
    root = round(abs(x) ** (1 / 3))
    return root**3 == abs(x)


# Examples
print(is_perfect_square(16))  # True
print(is_perfect_cube(-27))  # True


# 🧩 Handle invalid roots
def safe_sqrt(x):
    """Safe square root, returns None for negatives."""
    try:
        if x < 0:
            return None
        return x**0.5
    except Exception as e:
        print(f"Error: {e}")
        return None


# Examples
print(safe_sqrt(-4))  # None


# 🧩 Performance comparison
import time


def benchmark_roots():
    """Benchmark sqrt and nth_root."""
    n = 1000000
    x = 12345.6789

    start = time.time()
    for _ in range(n):
        x**0.5
    sqrt_time = time.time() - start

    start = time.time()
    for _ in range(n):
        x ** (1 / 3)
    cbrt_time = time.time() - start

    print(f"sqrt: {sqrt_time:.6f}s, cbrt: {cbrt_time:.6f}s")


# benchmark_roots()


# 🧩 Geometry and finance
def hypotenuse(a, b):
    """Compute hypotenuse using Pythagoras' theorem."""
    return (a**2 + b**2) ** 0.5


def compound_interest(principal, rate, periods):
    """Compute final amount with compound interest."""
    return principal * (1 + rate) ** periods


# Examples
print(hypotenuse(3, 4))  # 5.0
print(compound_interest(1000, 0.05, 2))  # 1102.5
