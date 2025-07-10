---
title: Complex Number Operations
description: Zero-dependency Python snippets for complex number arithmetic using the standard library.
keywords: abs, addition, arithmetic, benchmarking, complex, conjugate, cos, cosh, create, division, edge-case, engineering, error-handling, exp, float, imaginary, impedance, log, math, multiplication, performance, phase, phasor, polar, power, real, rect, roots, signal-processing, sin, sinh, sqrt, subtraction, tan, tanh, validation
---

# Complex Number Operations

Zero-dependency Python snippets for complex number arithmetic using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic complex arithmetic

`math` `complex` `arithmetic` `addition` `subtraction` `multiplication` `division`

Perform basic complex arithmetic

```python
def add_complex(a, b):
    """Add two complex numbers."""
    return complex(a) + complex(b)


def subtract_complex(a, b):
    """Subtract two complex numbers."""
    return complex(a) - complex(b)


def multiply_complex(a, b):
    """Multiply two complex numbers."""
    return complex(a) * complex(b)


def divide_complex(a, b):
    """Divide two complex numbers."""
    return complex(a) / complex(b)


# Basic complex arithmetic
print(add_complex(1 + 2j, 3 - 4j))  # (4-2j)
print(subtract_complex(5, 2j))  # (5-2j)
print(multiply_complex(2 + 3j, 4 - 1j))  # (11+10j)
print(divide_complex(1 + 1j, 1 - 1j))  # 1j
```

!!! note "Notes"
    - Uses built-in complex type
    - Accepts real, imaginary, or complex input
    - Standard arithmetic operations

<hr class="snippet-divider">

### Create and access complex numbers

`math` `complex` `create` `real` `imaginary` `conjugate`

Create and access complex numbers

```python
def create_complex(real, imag=0):
    """Create a complex number from real and imaginary parts."""
    return complex(real, imag)


def real_part(z):
    """Get real part of complex number."""
    return z.real


def imag_part(z):
    """Get imaginary part of complex number."""
    return z.imag


def conjugate(z):
    """Get complex conjugate."""
    return z.conjugate()


# Examples
z = create_complex(3, 4)
print(f"z = {z}, real: {real_part(z)}, imag: {imag_part(z)}, conj: {conjugate(z)}")
```

!!! note "Notes"
    - Real and imaginary parts
    - Conjugate for division
    - Useful for polar/cartesian conversion

<hr class="snippet-divider">

### Absolute value, phase, and polar form

`math` `complex` `abs` `phase` `polar` `rect`

Work with absolute value, phase, and polar form

```python
import cmath


def abs_complex(z):
    """Get absolute value (modulus) of complex number."""
    return abs(z)


def phase_complex(z):
    """Get phase (argument) of complex number in radians."""
    return cmath.phase(z)


def polar_complex(z):
    """Get polar coordinates (r, θ) of complex number."""
    return cmath.polar(z)


def rect_complex(r, theta):
    """Convert polar coordinates to complex number."""
    return cmath.rect(r, theta)


# Examples
z = 1 + 1j
print(f"abs: {abs_complex(z):.3f}, phase: {phase_complex(z):.3f}")
print(f"polar: {polar_complex(z)}")
print(f"rect: {rect_complex(1.414, 0.785)}")
```

!!! note "Notes"
    - Modulus and argument
    - Polar/cartesian conversion
    - cmath module for advanced functions

<hr class="snippet-divider">

## Complex

###  Complex exponentials and logarithms

`math` `complex` `exp` `log` `power`

Calculate exponentials and logarithms of complex numbers

```python
import cmath


def exp_complex(z):
    """Calculate exponential of complex number."""
    return cmath.exp(z)


def log_complex(z, base=cmath.e):
    """Calculate logarithm of complex number."""
    if base == cmath.e:
        return cmath.log(z)
    else:
        return cmath.log(z) / cmath.log(base)


def pow_complex(z, w):
    """Raise complex number z to power w."""
    return z**w


# Examples
z = 1 + 1j
print(f"exp(z): {exp_complex(z)}")
print(f"log(z): {log_complex(z)}")
print(f"z^2: {pow_complex(z, 2)}")
```

!!! note "Notes"
    - Euler's formula
    - Complex logarithms
    - Arbitrary powers

<hr class="snippet-divider">

### Complex roots and powers

`math` `complex` `sqrt` `roots` `power`

Calculate roots and powers of complex numbers

```python
import cmath


def sqrt_complex(z):
    """Calculate square root of complex number."""
    return cmath.sqrt(z)


def nth_roots_complex(z, n):
    """Calculate all n-th roots of complex number."""
    r, theta = cmath.polar(z)
    return [cmath.rect(r ** (1 / n), (theta + 2 * cmath.pi * k) / n) for k in range(n)]


# Examples
z = -1
print(f"sqrt(-1): {sqrt_complex(z)}")
roots = nth_roots_complex(1, 4)
print(f"4th roots of 1: {roots}")
```

!!! note "Notes"
    - Square roots
    - n-th roots (De Moivre's theorem)
    - Useful for signal processing

<hr class="snippet-divider">

### Trigonometric and hyperbolic functions

`math` `complex` `sin` `cos` `tan` `sinh` `cosh` `tanh`

Calculate trigonometric and hyperbolic functions of complex numbers

```python
import cmath


def sin_complex(z):
    """Calculate sine of complex number."""
    return cmath.sin(z)


def cos_complex(z):
    """Calculate cosine of complex number."""
    return cmath.cos(z)


def tan_complex(z):
    """Calculate tangent of complex number."""
    return cmath.tan(z)


def sinh_complex(z):
    """Calculate hyperbolic sine of complex number."""
    return cmath.sinh(z)


def cosh_complex(z):
    """Calculate hyperbolic cosine of complex number."""
    return cmath.cosh(z)


def tanh_complex(z):
    """Calculate hyperbolic tangent of complex number."""
    return cmath.tanh(z)


# Examples
z = 1 + 1j
print(f"sin(z): {sin_complex(z)}")
print(f"cos(z): {cos_complex(z)}")
print(f"sinh(z): {sinh_complex(z)}")
```

!!! note "Notes"
    - Trigonometric and hyperbolic functions
    - cmath module
    - Useful for engineering and physics

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in complex arithmetic

`math` `complex` `error-handling` `edge-case` `validation`

Robust complex arithmetic with error handling

```python
def robust_complex(a, b=0):
    """Create complex number with error handling."""
    try:
        return complex(a, b)
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_divide_complex(a, b):
    """Safe division with zero and error handling."""
    try:
        return complex(a) / complex(b)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test edge cases
print(robust_complex("abc"))  # Error, returns None
print(safe_divide_complex(1, 0))  # Error, returns None
```

!!! note "Notes"
    - Input validation
    - Division by zero
    - Error messages
    - Robustness for user input

<hr class="snippet-divider">

### Performance comparison

`math` `complex` `float` `performance` `benchmarking`

Benchmark complex vs float arithmetic

```python
import time


def benchmark_complex_vs_float():
    """Compare performance of complex vs float arithmetic."""
    a, b = 1 + 2j, 3 - 4j
    n = 100000

    # Complex arithmetic
    start = time.time()
    for _ in range(n):
        a + b
    complex_time = time.time() - start

    # Float arithmetic
    a_f, b_f = 1.0, 2.0
    start = time.time()
    for _ in range(n):
        a_f + b_f
    float_time = time.time() - start

    print(f"Complex: {complex_time:.6f}s, Float: {float_time:.6f}s")
    print(f"Complex is {complex_time / float_time:.2f}x slower")


# benchmark_complex_vs_float()
```

!!! note "Notes"
    - Complex is slower than float
    - Use complex for advanced math, float for speed
    - Trade-off between capability and performance

<hr class="snippet-divider">

## Practical Examples

###  Signal processing and engineering

`math` `complex` `signal-processing` `engineering` `impedance` `phasor`

Use complex numbers in signal processing and engineering

```python
import cmath


def impedance(resistance, reactance):
    """Calculate impedance as a complex number."""
    return complex(resistance, reactance)


def phasor(amplitude, phase):
    """Create phasor (complex representation of sinusoid)."""
    import cmath

    return cmath.rect(amplitude, phase)


def ac_voltage(amplitude, frequency, time, phase=0):
    """Calculate AC voltage as a complex exponential."""
    import cmath

    omega = 2 * cmath.pi * frequency
    return amplitude * cmath.exp(1j * (omega * time + phase))


# Examples
z = impedance(10, 5)
print(f"Impedance: {z}")

phasor_val = phasor(1, cmath.pi / 4)
print(f"Phasor: {phasor_val}")

voltage = ac_voltage(120, 60, 0.01)
print(f"AC voltage: {voltage}")
```

!!! note "Notes"
    - Impedance calculation
    - Phasor representation
    - AC voltage as complex exponential
    - Engineering applications

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Trigonometry](trigonometry.md)
- **Reference**: See [📂 Exponents](exponents.md)
- **Reference**: See [📂 Roots](roots.md)
- **Reference**: See [📂 Matrices](matrices.md)

## 🏷️ Tags

`math`, `complex`, `arithmetic`, `polar`, `engineering`, `signal-processing`, `error-handling`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Complex Number Functions Support Engineering and Scientific Applications
- Use for Signal Processing, AC Circuits, and Advanced Math
- Edge Case Handling Ensures Robustness
- Trade-Off Between Capability and Performance
