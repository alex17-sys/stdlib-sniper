---
title: Decimal Precision Operations
description: Zero-dependency Python snippets for decimal arithmetic with precision using the standard library.
keywords: addition, arithmetic, benchmarking, compare, context, currency, decimal, division, edge-case, equality, error-handling, exp, finance, float, global, interest, ln, localcontext, log10, math, multiplication, performance, precision, quantize, rounding, sqrt, subtraction, validation
---

# Decimal Precision Operations

Zero-dependency Python snippets for decimal arithmetic with precision using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic decimal arithmetic

`math` `decimal` `precision` `arithmetic` `addition` `subtraction` `multiplication` `division`

Perform basic decimal arithmetic with precision

```python
from decimal import Decimal, getcontext


def add_decimals(a, b, precision=2):
    """Add two decimal numbers with specified precision."""
    getcontext().prec = precision
    return Decimal(a) + Decimal(b)


def subtract_decimals(a, b, precision=2):
    """Subtract two decimal numbers with specified precision."""
    getcontext().prec = precision
    return Decimal(a) - Decimal(b)


def multiply_decimals(a, b, precision=2):
    """Multiply two decimal numbers with specified precision."""
    getcontext().prec = precision
    return Decimal(a) * Decimal(b)


def divide_decimals(a, b, precision=2):
    """Divide two decimal numbers with specified precision."""
    getcontext().prec = precision
    return Decimal(a) / Decimal(b)


# Basic decimal arithmetic
print(add_decimals("1.234", "2.345", 4))  # 3.579
print(subtract_decimals("5.5", "2.2", 3))  # 3.3
print(multiply_decimals("1.5", "2.5", 5))  # 3.75
print(divide_decimals("10", "3", 6))  # 3.33333
```

!!! note "Notes"
    - Uses decimal module
    - String input recommended for precision
    - Set precision per operation
    - Avoids floating point errors

<hr class="snippet-divider">

### Set global decimal precision

`math` `decimal` `precision` `global` `context`

Set and get global decimal precision

```python
from decimal import getcontext


def set_global_precision(precision):
    """Set global decimal precision for all operations."""
    getcontext().prec = precision


def get_global_precision():
    """Get current global decimal precision."""
    return getcontext().prec


# Set and get global precision
set_global_precision(8)
print(get_global_precision())  # 8
```

!!! note "Notes"
    - Global context affects all Decimal operations
    - Useful for consistent precision
    - Can be reset as needed

<hr class="snippet-divider">

### Decimal rounding and quantization

`math` `decimal` `rounding` `quantize` `precision`

Round and quantize decimal values

```python
from decimal import Decimal


def round_decimal(value, places):
    """Round decimal to specified number of places."""
    d = Decimal(value)
    return d.quantize(Decimal("1." + "0" * places))


def quantize_decimal(value, quant):
    """Quantize decimal to nearest multiple of quant."""
    d = Decimal(value)
    return d.quantize(Decimal(quant))


# Examples
print(round_decimal("3.14159", 2))  # 3.14
print(quantize_decimal("2.71828", "0.01"))  # 2.72
```

!!! note "Notes"
    - Quantize for fixed-point rounding
    - Useful for currency, measurements
    - Avoids binary float issues

<hr class="snippet-divider">

## Complex

###  Decimal context management

`math` `decimal` `context` `localcontext` `precision`

Use local context for decimal precision

```python
from decimal import Decimal, localcontext


def decimal_with_context(a, b, precision=4):
    """Perform decimal arithmetic with local context precision."""
    with localcontext() as ctx:
        ctx.prec = precision
        result = Decimal(a) / Decimal(b)
    return result


# Example
print(decimal_with_context("1", "3", 6))  # 0.333333
```

!!! note "Notes"
    - Local context for temporary precision
    - Does not affect global context
    - Useful for isolated calculations

<hr class="snippet-divider">

### Decimal math functions

`math` `decimal` `sqrt` `exp` `ln` `log10` `precision`

Perform math functions with decimal precision

```python
from decimal import Decimal, getcontext


def decimal_sqrt(value, precision=6):
    """Calculate square root with decimal precision."""
    getcontext().prec = precision
    return Decimal(value).sqrt()


def decimal_exp(value, precision=6):
    """Calculate exponential with decimal precision."""
    getcontext().prec = precision
    return Decimal(value).exp()


def decimal_ln(value, precision=6):
    """Calculate natural logarithm with decimal precision."""
    getcontext().prec = precision
    return Decimal(value).ln()


def decimal_log10(value, precision=6):
    """Calculate base-10 logarithm with decimal precision."""
    getcontext().prec = precision
    return Decimal(value).log10()


# Examples
print(decimal_sqrt("2", 10))  # 1.414213562
print(decimal_exp("1", 8))  # 2.7182818
print(decimal_ln("10", 8))  # 2.3025851
print(decimal_log10("100", 8))  # 2
```

!!! note "Notes"
    - Decimal math functions
    - High-precision calculations
    - Useful for scientific computing

<hr class="snippet-divider">

### Decimal comparisons and equality

`math` `decimal` `compare` `equality` `precision`

Compare decimal values for equality and order

```python
from decimal import Decimal


def decimals_equal(a, b, places=6):
    """Check if two decimals are equal up to specified places."""
    d1 = Decimal(a).quantize(Decimal("1." + "0" * places))
    d2 = Decimal(b).quantize(Decimal("1." + "0" * places))
    return d1 == d2


def decimal_compare(a, b):
    """Compare two decimals: returns -1, 0, 1."""
    d1 = Decimal(a)
    d2 = Decimal(b)
    return (d1 > d2) - (d1 < d2)


# Examples
print(decimals_equal("1.234567", "1.234568", 5))  # True
print(decimal_compare("2.5", "2.50"))  # 0
```

!!! note "Notes"
    - Quantize for equality
    - Useful for financial calculations
    - Avoids float comparison issues

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in decimal arithmetic

`math` `decimal` `error-handling` `edge-case` `validation`

Robust decimal arithmetic with error handling

```python
from decimal import Decimal, getcontext


def robust_decimal(value):
    """Create Decimal with error handling."""
    try:
        return Decimal(value)
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_divide_decimals(a, b, precision=6):
    """Safe division with zero and error handling."""
    getcontext().prec = precision
    try:
        return Decimal(a) / Decimal(b)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test edge cases
print(robust_decimal("abc"))  # Error, returns None
print(safe_divide_decimals("1", "0"))  # Error, returns None
```

!!! note "Notes"
    - Input validation
    - Division by zero
    - Error messages
    - Robustness for user input

<hr class="snippet-divider">

### Performance comparison

`math` `decimal` `float` `performance` `benchmarking`

Benchmark Decimal vs float arithmetic

```python
import time
from decimal import Decimal

def benchmark_decimal_vs_float():
    """Compare performance of Decimal vs float arithmetic."""
    a, b = "1.23456789", "9.87654321"
    n = 100000

    # Decimal arithmetic
    start = time.time()
    for _ in range(n):
        Decimal(a) + Decimal(b)
    decimal_time = time.time() - start

    # Float arithmetic
    a_f, b_f = float(a), float(b)
    start = time.time()
    for _ in range(n):
        a_f + b_f
    float_time = time.time() - start

    print(f"Decimal: {decimal_time:.6f}s, Float: {float_time:.6f}s")
    print(f"Decimal is {decimal_time / float_time:.2f}x slower")


# benchmark_decimal_vs_float()
```

!!! note "Notes"
    - Decimal is slower than float
    - Use Decimal for precision, float for speed
    - Trade-off between accuracy and performance

<hr class="snippet-divider">

## Practical Examples

###  Financial calculations

`math` `decimal` `finance` `currency` `interest` `precision`

Use decimal arithmetic in financial calculations

```python
from decimal import Decimal, getcontext


def calculate_interest(principal, rate, time, precision=2):
    """Calculate simple interest with decimal precision."""
    getcontext().prec = precision
    principal = Decimal(principal)
    rate = Decimal(rate)
    time = Decimal(time)
    interest = principal * rate * time / Decimal("100")
    return interest


def currency_addition(amounts, precision=2):
    """Add list of currency amounts with decimal precision."""
    getcontext().prec = precision
    total = sum(Decimal(a) for a in amounts)
    return total


# Examples
interest = calculate_interest("1000", "5", "3", 4)
print(f"Interest: {interest}")

total = currency_addition(["10.25", "20.50", "5.75"], 2)
print(f"Total: {total}")
```

!!! note "Notes"
    - Financial calculations
    - Currency addition
    - Interest calculation
    - Avoids rounding errors

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Percentage](percentage.md)
- **Reference**: See [📂 Fraction Math](fraction_math.md)

## 🏷️ Tags

`math`, `decimal`, `precision`, `arithmetic`, `finance`, `error-handling`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Decimal Arithmetic Supports High-Precision Calculations
- Use for Financial, Scientific, and User-Facing Applications
- Edge Case Handling Ensures Robustness
- Trade-Off Between Precision and Performance
