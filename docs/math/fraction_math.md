# Fraction Math Operations

Zero-dependency Python snippets using only the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic fraction arithmetic

`math` `fraction` `arithmetic` `addition` `subtraction` `multiplication` `division`

Perform basic fraction arithmetic

```python
from fractions import Fraction


def add_fractions(a, b):
    """Add two fractions."""
    return Fraction(a) + Fraction(b)


def subtract_fractions(a, b):
    """Subtract two fractions."""
    return Fraction(a) - Fraction(b)


def multiply_fractions(a, b):
    """Multiply two fractions."""
    return Fraction(a) * Fraction(b)


def divide_fractions(a, b):
    """Divide two fractions."""
    return Fraction(a) / Fraction(b)


# Basic fraction arithmetic
print(add_fractions("1/3", "1/6"))  # 1/2
print(subtract_fractions("3/4", "1/2"))  # 1/4
print(multiply_fractions("2/3", "3/5"))  # 2/5
print(divide_fractions("3/4", "2/5"))  # 15/8
```

!!! note "Notes"
    - Uses fractions module
    - Accepts string or Fraction input
    - Results are always reduced
    - Exact rational arithmetic

<hr class="snippet-divider">

### Create and simplify fractions

`math` `fraction` `simplify` `create` `lowest-terms`

Create and simplify fractions

```python
from fractions import Fraction


def create_fraction(numerator, denominator=1):
    """Create a fraction from numerator and denominator."""
    return Fraction(numerator, denominator)


def simplify_fraction(frac):
    """Simplify a fraction to lowest terms."""
    return Fraction(frac.numerator, frac.denominator)


# Examples
f = create_fraction(8, 12)
print(f"Created: {f}, Simplified: {simplify_fraction(f)}")  # 2/3
```

!!! note "Notes"
    - Automatic simplification
    - Handles negative values
    - Numerator/denominator access

<hr class="snippet-divider">

### Fraction to float and decimal

`math` `fraction` `float` `decimal` `conversion`

Convert fractions to float and decimal

```python
from fractions import Fraction


from decimal import Decimal


def fraction_to_float(frac):
    """Convert fraction to float."""
    return float(frac)


def fraction_to_decimal(frac, precision=6):
    """Convert fraction to Decimal with specified precision."""
    from decimal import getcontext

    getcontext().prec = precision
    return Decimal(frac.numerator) / Decimal(frac.denominator)


# Examples
f = Fraction(1, 3)
print(fraction_to_float(f))  # 0.333...
print(fraction_to_decimal(f, 8))  # 0.33333333
```

!!! note "Notes"
    - Float conversion may lose precision
    - Decimal for high-precision
    - Useful for display and calculations

<hr class="snippet-divider">

## Complex

###  Fraction comparison and equality

`math` `fraction` `compare` `equality` `order`

Compare fractions for equality and order

```python
from fractions import Fraction


def fractions_equal(a, b):
    """Check if two fractions are equal."""
    return Fraction(a) == Fraction(b)


def compare_fractions(a, b):
    """Compare two fractions: returns -1, 0, 1."""
    f1 = Fraction(a)
    f2 = Fraction(b)
    return (f1 > f2) - (f1 < f2)


# Examples
print(fractions_equal("2/4", "1/2"))  # True
print(compare_fractions("3/5", "2/3"))  # -1
```

!!! note "Notes"
    - Exact comparison
    - Useful for sorting
    - Handles negative values

<hr class="snippet-divider">

### Fraction reduction and expansion

`math` `fraction` `reduce` `expand` `lowest-terms`

Reduce and expand fractions

```python
from fractions import Fraction


def reduce_fraction(frac):
    """Reduce fraction to lowest terms."""
    return frac.limit_denominator()


def expand_fraction(frac, factor):
    """Expand fraction by multiplying numerator and denominator."""
    return Fraction(frac.numerator * factor, frac.denominator * factor)


# Examples
f = Fraction(2, 4)
print(reduce_fraction(f))  # 1/2
print(expand_fraction(f, 3))  # 6/12
```

!!! note "Notes"
    - Reduction to lowest terms
    - Expansion for common denominators
    - Useful for arithmetic

<hr class="snippet-divider">

### Fraction from float and decimal

`math` `fraction` `from-float` `from-decimal` `conversion`

Create fractions from float and decimal

```python
from fractions import Fraction


def fraction_from_float(value):
    """Create fraction from float value."""
    return Fraction(value).limit_denominator()


def fraction_from_decimal(value):
    """Create fraction from Decimal value."""
    return Fraction(str(value))


# Examples
print(fraction_from_float(0.75))  # 3/4
from decimal import Decimal

print(fraction_from_decimal(Decimal("0.125")))  # 1/8
```

!!! note "Notes"
    - Float to fraction (approximate)
    - Decimal to fraction (exact)
    - Useful for parsing input

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in fraction arithmetic

`math` `fraction` `error-handling` `edge-case` `validation`

Robust fraction arithmetic with error handling

```python
from fractions import Fraction


def robust_fraction(a, b=1):
    """Create Fraction with error handling."""
    try:
        return Fraction(a, b)
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_divide_fractions(a, b):
    """Safe division with zero and error handling."""
    try:
        return Fraction(a) / Fraction(b)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test edge cases
print(robust_fraction("abc"))  # Error, returns None
print(safe_divide_fractions("1/2", "0"))  # Error, returns None
```

!!! note "Notes"
    - Input validation
    - Division by zero
    - Error messages
    - Robustness for user input

<hr class="snippet-divider">

### Performance comparison

`math` `fraction` `float` `performance` `benchmarking`

Benchmark Fraction vs float arithmetic

```python
import time
from fractions import Fraction


def benchmark_fraction_vs_float():
    """Compare performance of Fraction vs float arithmetic."""
    a, b = "1/3", "2/5"
    n = 100000

    # Fraction arithmetic
    start = time.time()
    for _ in range(n):
        Fraction(a) + Fraction(b)
    fraction_time = time.time() - start

    # Float arithmetic
    a_f, b_f = float(Fraction(a)), float(Fraction(b))
    start = time.time()
    for _ in range(n):
        a_f + b_f
    float_time = time.time() - start

    print(f"Fraction: {fraction_time:.6f}s, Float: {float_time:.6f}s")
    print(f"Fraction is {fraction_time / float_time:.2f}x slower")


# benchmark_fraction_vs_float()
```

!!! note "Notes"
    - Fraction is slower than float
    - Use Fraction for exactness, float for speed
    - Trade-off between accuracy and performance

<hr class="snippet-divider">

## Practical Examples

###  Ratio and proportion calculations

`math` `fraction` `ratio` `proportion` `scaling`

Use fractions for ratio and proportion calculations

```python
from fractions import Fraction


def calculate_ratio(a, b):
    """Calculate ratio as a fraction."""
    return Fraction(a, b)


def scale_recipe(ingredients, factor):
    """Scale recipe ingredient amounts by a factor (as fractions)."""
    return {k: Fraction(v) * factor for k, v in ingredients.items()}


# Examples
ratio = calculate_ratio(3, 4)
print(f"Ratio: {ratio}")

recipe = {"flour": "2/3", "sugar": "1/4", "milk": "1/2"}
scaled = scale_recipe(recipe, Fraction(3, 2))
print(f"Scaled recipe: {scaled}")
```

!!! note "Notes"
    - Ratio as fraction
    - Recipe scaling
    - Proportional calculations
    - Exact arithmetic

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Decimal Precision](decimal_precision.md)
- **Reference**: See [📂 GCD/LCM](gcd_lcm.md)
- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)

## 🏷️ Tags

`math`, `fraction`, `arithmetic`, `ratio`, `proportion`, `conversion`, `error-handling`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Fraction Arithmetic Supports Exact Rational Calculations
- Use for Ratios, Proportions, and Financial Applications
- Edge Case Handling Ensures Robustness
- Trade-Off Between Exactness and Performance
