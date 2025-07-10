---
title: Calculus
description: Zero-dependency Python snippets for basic calculus operations (derivatives, integrals, limits, numerical methods) using the standard library.
keywords: area, benchmarking, calculus, complex, derivative, edge-case, error-handling, finite-difference, higher-derivative, integral, limit, math, multivariate, numbers, optimization, partial-derivative, performance, physics, simpson, trapezoidal, velocity
---

# Calculus

Zero-dependency Python snippets for basic calculus operations (derivatives, integrals, limits, numerical methods) using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Numerical derivative (finite difference)

`math` `calculus` `derivative` `finite-difference`

Approximate derivative numerically

```python
def derivative(f, x, h=1e-5):
    """Approximate the derivative of f at x using central difference."""
    return (f(x + h) - f(x - h)) / (2 * h)


# Examples
def f(x):
    return x**2


print(derivative(f, 3))  # ~6.0
```

!!! note "Notes"
    - Central difference method
    - h controls accuracy

<hr class="snippet-divider">

### Numerical integral (trapezoidal rule)

`math` `calculus` `integral` `trapezoidal`

Approximate integral numerically

```python
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
```

!!! note "Notes"
    - Trapezoidal rule
    - n controls accuracy

<hr class="snippet-divider">

### Numerical limit (approaching a point)

`math` `calculus` `limit` `numbers`

Approximate limit numerically

```python
def limit(f, x, h=1e-5):
    """Approximate the limit of f as x is approached from the right."""
    return f(x + h)


# Examples
def f(x):
    return (x**2 - 1) / (x - 1)


print(limit(f, 1))  # ~2.00001
```

!!! note "Notes"
    - Approaches from the right
    - h controls proximity

<hr class="snippet-divider">

## Complex

###  Higher-order derivatives

`math` `calculus` `higher-derivative` `complex`

Compute higher-order derivatives

```python
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
```

!!! note "Notes"
    - Recursive central difference
    - n controls order

<hr class="snippet-divider">

### Definite integral (Simpson's rule)

`math` `calculus` `simpson` `integral` `complex`

Approximate integral with Simpson's rule

```python
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
```

!!! note "Notes"
    - Simpson's rule is more accurate
    - n must be even

<hr class="snippet-divider">

### Numerical partial derivatives (multivariate)

`math` `calculus` `partial-derivative` `multivariate`

Compute partial derivatives numerically

```python
def partial_derivative(f, x, y, h=1e-5):
    """Approximate partial derivatives of f(x, y) at (x, y)."""
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return df_dx, df_dy


# Examples
def f(x, y):
    return x * y + y**2


print(partial_derivative(f, 1, 2))  # (~2.0, ~5.0)
```

!!! note "Notes"
    - For functions of two variables
    - Returns tuple of partials

<hr class="snippet-divider">

## Edge Cases

###  Handle invalid functions and domains

`math` `calculus` `error-handling` `edge-case`

Robust calculus operations

```python
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
```

!!! note "Notes"
    - Handles division by zero, invalid input
    - Returns None or error

<hr class="snippet-divider">

### Performance comparison

`math` `calculus` `performance` `benchmarking`

Benchmark calculus operations

```python
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
```

!!! note "Notes"
    - Numerical methods are slower than direct math
    - Useful for performance-critical code

<hr class="snippet-divider">

## Practical Examples

###  Physics and optimization

`math` `calculus` `physics` `optimization` `area` `velocity`

Use calculus in physics and optimization

```python
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
```

!!! note "Notes"
    - Derivatives for velocity, optimization
    - Integrals for area, probability

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Statistics Advanced](statistics_advanced.md)
- **Reference**: See [📂 Linear Algebra](linear_algebra.md)

## 🏷️ Tags

`math`, `calculus`, `derivative`, `integral`, `limit`, `numbers`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Calculus Snippets Use Only Standard Library
- Numerical Methods for Derivatives and Integrals
- Handles Edge Cases and Invalid Input
- Suitable for Educational and Practical Use
