# 🧩 Numerical derivative (finite difference)
def derivative(f, x, h=1e-5):
    """Approximate the derivative of f at x using central difference."""
    return (f(x + h) - f(x - h)) / (2 * h)


# Examples
def f(x):
    return x**2


print(derivative(f, 3))  # ~6.0


# 🧩 Numerical integral (trapezoidal rule)
def integral(f, a, b, n=1000):
    """Approximate the definite integral of f from a to b using trapezoidal rule."""
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h


# Examples
def f(x):
    return x**2


print(integral(f, 0, 1))  # ~0.3333


# 🧩 Numerical limit (approaching a point)
def limit(f, x, h=1e-5):
    """Approximate the limit of f as x is approached from the right."""
    return f(x + h)


# Examples
def f(x):
    return (x**2 - 1) / (x - 1)


print(limit(f, 1))  # ~2.00001


# 🧩 Higher-order derivatives
def derivative(f, x, h=1e-5):
    # See above defined function
    pass


def nth_derivative(f, x, n, h=1e-5):
    """Approximate the nth derivative of f at x."""
    if n == 0:
        return f(x)
    elif n == 1:
        return derivative(f, x, h)
    else:
        return (nth_derivative(f, x + h, n - 1, h) - nth_derivative(f, x - h, n - 1, h)) / (2 * h)


# Examples
def f(x):
    return x**3


print(nth_derivative(f, 2, 2))  # ~12.0


# 🧩 Definite integral (Simpson's rule)
def simpsons_rule(f, a, b, n=1000):
    """Approximate the definite integral using Simpson's rule (n even)."""
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3


# Examples
def f(x):
    return x**2


print(simpsons_rule(f, 0, 1))  # ~0.3333


# 🧩 Numerical partial derivatives (multivariate)
def partial_derivative(f, x, y, h=1e-5):
    """Approximate partial derivatives of f(x, y) at (x, y)."""
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return df_dx, df_dy


# Examples
def f(x, y):
    return x * y + y**2


print(partial_derivative(f, 1, 2))  # (~2.0, ~5.0)


# 🧩 Handle invalid functions and domains
def derivative(f, x, h=1e-5):
    # See above defined function
    pass


def safe_derivative(f, x, h=1e-5):
    """Safe derivative, returns None on error."""
    try:
        return derivative(f, x, h)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Examples
def f(x):
    return 1 / x


print(safe_derivative(f, 0))  # Error, returns None


# 🧩 Performance comparison
import time


def derivative(f, x, h=1e-5):
    # See above defined function
    pass


def benchmark_derivative():
    """Benchmark numerical derivative."""

    def f(x):
        return x**2

    n = 100000
    start = time.time()
    for i in range(n):
        derivative(f, i)
    print(f"Derivative: {time.time() - start:.6f}s")


# benchmark_derivative()


# 🧩 Physics and optimization
def derivative(f, x, h=1e-5):
    # See above defined function
    pass


def integral(f, a, b, n=1000):
    # See above defined function
    pass


def velocity(position, t, h=1e-5):
    """Compute velocity as derivative of position function."""
    return derivative(position, t, h)


def area_under_curve(f, a, b):
    """Compute area under curve using integral."""
    return integral(f, a, b)


# Examples
def s(t):
    return 3 * t**2


print(velocity(s, 2))  # ~12.0
print(area_under_curve(s, 0, 2))  # ~16.0
