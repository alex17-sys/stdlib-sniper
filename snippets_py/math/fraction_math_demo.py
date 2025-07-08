# 🧩 Basic fraction arithmetic
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


# 🧩 Create and simplify fractions
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


# 🧩 Fraction to float and decimal
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


# 🧩 Fraction comparison and equality
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


# 🧩 Fraction reduction and expansion
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


# 🧩 Fraction from float and decimal
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


# 🧩 Handle edge cases in fraction arithmetic
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


# 🧩 Performance comparison
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


# 🧩 Ratio and proportion calculations
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
