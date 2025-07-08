# Number Conversion

Zero-dependency Python snippets for converting between number bases and types using the standard library.

## Simple

### 🧩 Integer to binary, octal, hexadecimal strings

```python
def int_to_bin(n):
    """Convert integer to binary string."""
    return bin(n)


def int_to_oct(n):
    """Convert integer to octal string."""
    return oct(n)


def int_to_hex(n):
    """Convert integer to hexadecimal string."""
    return hex(n)


# Examples
print(int_to_bin(42))  # '0b101010'
print(int_to_oct(42))  # '0o52'
print(int_to_hex(42))  # '0x2a'
```

📂 Convert integer to binary, octal, hex

🏷️ Tags: math, conversion, int, bin, oct, hex
📝 Notes:
- Prefixes: 0b, 0o, 0x
- Output is a string

### 🧩 String to integer (any base)

```python
def str_to_int(s, base=10):
    """Convert string in given base to integer."""
    return int(s, base)


# Examples
print(str_to_int("101010", 2))  # 42
print(str_to_int("52", 8))  # 42
print(str_to_int("2a", 16))  # 42
```

📂 Convert string to integer (any base)

🏷️ Tags: math, conversion, str, int, base
📝 Notes:
- No prefix needed in string
- Handles ValueError for invalid input

### 🧩 Integer to/from bytes

```python
def int_to_bytes(n, length, byteorder="big"):
    """Convert integer to bytes."""
    return n.to_bytes(length, byteorder)


def bytes_to_int(b, byteorder="big"):
    """Convert bytes to integer."""
    return int.from_bytes(b, byteorder)


# Examples
b = int_to_bytes(1024, 2)
print(b)  # b'\x04\x00'
print(bytes_to_int(b))  # 1024
```

📂 Convert integer to/from bytes

🏷️ Tags: math, conversion, int, bytes
📝 Notes:
- Specify byteorder: 'big' or 'little'
- Useful for binary protocols

### 🧩 Float to string and back

```python
def float_to_str(f, precision=6):
    """Convert float to string with given precision."""
    return f"{f:.{precision}f}"


def str_to_float(s):
    """Convert string to float."""
    return float(s)


# Examples
print(float_to_str(3.14159, 2))  # '3.14'
print(str_to_float("2.718"))  # 2.718
```

📂 Convert float to string and back

🏷️ Tags: math, conversion, float, str
📝 Notes:
- Handles ValueError for invalid input
- Precision for formatting

## Complex

### 🧩 Base conversion between arbitrary bases

```python
def base_convert(n, from_base, to_base):
    """Convert string n from from_base to to_base."""
    # Convert to integer
    num = int(n, from_base)
    # Convert to target base
    if to_base == 2:
        return bin(num)[2:]
    elif to_base == 8:
        return oct(num)[2:]
    elif to_base == 16:
        return hex(num)[2:]
    else:
        # General case
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            result = digits[num % to_base] + result
            num //= to_base
        return result


# Examples
print(base_convert("101010", 2, 16))  # '2a'
print(base_convert("2a", 16, 2))  # '101010'
print(base_convert("42", 10, 5))  # '132'
```

📂 Convert between arbitrary bases

🏷️ Tags: math, conversion, base, arbitrary, complex
📝 Notes:
- Supports bases up to 36
- Input as string

### 🧩 Type conversion: int, float, complex, fraction, decimal

```python
from fractions import Fraction
from decimal import Decimal


def to_int(x):
    """Convert to integer."""
    return int(x)


def to_float(x):
    """Convert to float."""
    return float(x)


def to_complex(x):
    """Convert to complex."""
    return complex(x)


def to_fraction(x):
    """Convert to Fraction."""
    return Fraction(x)


def to_decimal(x):
    """Convert to Decimal."""
    return Decimal(str(x))


# Examples
print(to_int(3.7))  # 3
print(to_float("2.5"))  # 2.5
print(to_complex("1+2j"))  # (1+2j)
print(to_fraction("3/4"))  # 3/4
print(to_decimal(2.718))  # Decimal('2.718')
```

📂 Convert between numeric types

🏷️ Tags: math, conversion, type, int, float, complex, fraction, decimal
📝 Notes:
- Use str for Fraction and Decimal for best results
- Handles ValueError for invalid input

## Edge Cases

### 🧩 Handle invalid conversions

```python
def safe_int(s, base=10):
    """Convert string to int, return None on error."""
    try:
        return int(s, base)
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_float(s):
    """Convert string to float, return None on error."""
    try:
        return float(s)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Examples
print(safe_int("notanumber"))  # Error, returns None
print(safe_float("abc"))  # Error, returns None
```

📂 Robust conversion with error handling

🏷️ Tags: math, conversion, error-handling, edge-case
📝 Notes:
- Handles invalid input gracefully
- Useful for user input

### 🧩 Performance comparison

```python
import time


def benchmark_conversion():
    """Benchmark int/float conversions."""
    n = 1000000
    s = "123456"
    f = "3.14159"

    start = time.time()
    for _ in range(n):
        int(s)
    int_time = time.time() - start

    start = time.time()
    for _ in range(n):
        float(f)
    float_time = time.time() - start

    print(f"int: {int_time:.6f}s, float: {float_time:.6f}s")


# benchmark_conversion()
```

📂 Benchmark number conversions

🏷️ Tags: math, conversion, performance, benchmarking
📝 Notes:
- Conversions are fast
- Useful for performance-critical code

## Practical Examples

### 🧩 Parsing user input and config

```python
def parse_config_value(s):
    """Parse config value as int, float, or leave as string."""
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


# Examples
print(parse_config_value("42"))  # 42
print(parse_config_value("3.14"))  # 3.14
print(parse_config_value("hello"))  # 'hello'
```

📂 Parse user input/config values

🏷️ Tags: math, conversion, parsing, config, user-input
📝 Notes:
- Useful for config files, CLI, user input
- Tries int, then float, then string

## 🔗 Cross-References

- **Reference**: See [📂 Bit Operations](bit_operations.md)
- **Reference**: See [📂 Fraction Math](fraction_math.md)

## 🏷️ Tags

`math`, `conversion`, `base`, `type`, `int`, `float`, `complex`, `fraction`, `decimal`, `parsing`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Number Conversion is Essential for Data Processing
- Supports All Standard Numeric Types and Bases
- Handles Edge Cases and Invalid Input
- Fast and Reliable for Most Applications
