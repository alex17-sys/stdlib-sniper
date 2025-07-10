---
title: Roots
description: Zero-dependency Python snippets for extracting roots (square, cube, nth) using the standard library.
keywords: benchmarking, cbrt, complex, cube-root, edge-case, error-handling, finance, general, geometry, integer, interest, math, nth-root, perfect-cube, perfect-square, performance, pythagoras, root, sqrt, square-root
---

# Roots

Zero-dependency Python snippets for extracting roots (square, cube, nth) using the standard library.

8 snippets available in this sub-category.

---

## Simple

###  Square root

`math` `root` `sqrt` `square-root`

Compute square root

```python
def sqrt(x):
    """Compute the square root of x."""
    return x**0.5


# Examples
print(sqrt(9))  # 3.0
print(sqrt(2))  # 1.4142135623730951
```

!!! note "Notes"
    - Returns float
    - For negative x, use complex (see below)

<hr class="snippet-divider">

### Cube root

`math` `root` `cbrt` `cube-root`

Compute cube root

```python
def cbrt(x):
    """Compute the cube root of x."""
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))


# Examples
print(cbrt(27))  # 3.0
print(cbrt(-8))  # -2.0
```

!!! note "Notes"
    - Handles negative numbers
    - Returns float

<hr class="snippet-divider">

### Nth root

`math` `root` `nth-root` `general`

Compute nth root

```python
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
```

!!! note "Notes"
    - Handles odd roots of negatives
    - Raises error for even roots of negatives

<hr class="snippet-divider">

## Complex

###  Roots of negative numbers (complex)

`math` `root` `complex` `sqrt` `nth-root`

Compute roots with complex results

```python
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
```

!!! note "Notes"
    - Use cmath for complex roots
    - Returns complex type

<hr class="snippet-divider">

### Integer roots and perfect powers

`math` `root` `perfect-square` `perfect-cube` `integer`

Check for perfect powers

```python
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
```

!!! note "Notes"
    - Useful for number theory
    - Handles negatives for cubes

<hr class="snippet-divider">

## Edge Cases

###  Handle invalid roots

`math` `root` `error-handling` `edge-case`

Robust root extraction

```python
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
```

!!! note "Notes"
    - Handles negatives and invalid input
    - Returns None or error

<hr class="snippet-divider">

### Performance comparison

`math` `root` `performance` `benchmarking`

Benchmark root extraction

```python
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
```

!!! note "Notes"
    - Root extraction is fast
    - Useful for performance-critical code

<hr class="snippet-divider">

## Practical Examples

###  Geometry and finance

`math` `root` `geometry` `finance` `pythagoras` `interest`

Use roots in geometry and finance

```python
def hypotenuse(a, b):
    """Compute hypotenuse using Pythagoras' theorem."""
    return (a**2 + b**2) ** 0.5


def compound_interest(principal, rate, periods):
    """Compute final amount with compound interest."""
    return principal * (1 + rate) ** periods


# Examples
print(hypotenuse(3, 4))  # 5.0
print(compound_interest(1000, 0.05, 2))  # 1102.5
```

!!! note "Notes"
    - Roots in geometric and financial formulas
    - Pythagoras, compound interest

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Exponents](exponents.md)
- **Reference**: See [📂 Complex Math](complex_math.md)

## 🏷️ Tags

`math`, `root`, `sqrt`, `cbrt`, `nth-root`, `complex`, `geometry`, `finance`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Root Extraction is Fundamental in Math and Science
- Handles Real and Complex Roots
- Robust to Edge Cases and Invalid Input
- Fast for Most Applications
