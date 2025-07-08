# Bit Operations

Zero-dependency Python snippets using only the standard library.

8 snippets available in this sub-category.

---

## Simple

###  Basic bitwise operations

`math` `bit` `bitwise` `and` `or` `xor` `not`

Perform basic bitwise operations

```python
def bitwise_and(a, b):
    """Bitwise AND of two integers."""
    return a & b


def bitwise_or(a, b):
    """Bitwise OR of two integers."""
    return a | b


def bitwise_xor(a, b):
    """Bitwise XOR of two integers."""
    return a ^ b


def bitwise_not(a, bits=8):
    """Bitwise NOT (invert all bits, limited to 'bits' bits)."""
    return (~a) & ((1 << bits) - 1)


# Examples
print(bitwise_and(6, 3))  # 2
print(bitwise_or(6, 3))  # 7
print(bitwise_xor(6, 3))  # 5
print(bitwise_not(6, 4))  # 9 (0110 -> 1001)
```

!!! note "Notes"
    - Works for integers
    - NOT is limited to a fixed number of bits

<hr class="snippet-divider">

### Bit shifts and masks

`math` `bit` `shift` `mask` `left-shift` `right-shift`

Perform bit shifts and apply masks

```python
def left_shift(a, n):
    """Left shift a by n bits."""
    return a << n


def right_shift(a, n):
    """Right shift a by n bits."""
    return a >> n


def bit_mask(n):
    """Create a mask with n least significant bits set to 1."""
    return (1 << n) - 1


def apply_mask(a, mask):
    """Apply bit mask to integer."""
    return a & mask


# Examples
print(left_shift(3, 2))  # 12
print(right_shift(12, 2))  # 3
print(bit_mask(4))  # 15 (0b1111)
print(apply_mask(13, 7))  # 5 (1101 & 0111 = 0101)
```

!!! note "Notes"
    - Useful for low-level operations
    - Masking for extracting bits

<hr class="snippet-divider">

### Bit counting and tests

`math` `bit` `count` `get` `set` `clear` `toggle`

Count and manipulate individual bits

```python
def count_bits(a):
    """Count number of set bits (1s) in integer."""
    return bin(a).count("1")


def is_power_of_two(a):
    """Check if integer is a power of two."""
    return a > 0 and (a & (a - 1)) == 0


def get_bit(a, n):
    """Get the nth bit (0-indexed from right)."""
    return (a >> n) & 1


def set_bit(a, n):
    """Set the nth bit to 1."""
    return a | (1 << n)


def clear_bit(a, n):
    """Clear the nth bit to 0."""
    return a & ~(1 << n)


def toggle_bit(a, n):
    """Toggle the nth bit."""
    return a ^ (1 << n)


# Examples
print(count_bits(13))  # 3 (1101)
print(is_power_of_two(8))  # True
print(get_bit(13, 2))  # 1
print(set_bit(8, 1))  # 10
print(clear_bit(10, 1))  # 8
print(toggle_bit(10, 1))  # 8
```

!!! note "Notes"
    - Bitwise manipulation
    - Useful for flags, masks, and encoding

<hr class="snippet-divider">

## Complex

###  Bitwise rotation and reversal

`math` `bit` `rotate` `reverse` `complex`

Rotate and reverse bits

```python
def rotate_left(a, n, bits=8):
    """Rotate bits left by n positions (within 'bits' bits)."""
    n = n % bits
    return ((a << n) | (a >> (bits - n))) & ((1 << bits) - 1)


def rotate_right(a, n, bits=8):
    """Rotate bits right by n positions (within 'bits' bits)."""
    n = n % bits
    return ((a >> n) | (a << (bits - n))) & ((1 << bits) - 1)


def reverse_bits(a, bits=8):
    """Reverse the order of bits in integer (within 'bits' bits)."""
    result = 0
    for i in range(bits):
        if (a >> i) & 1:
            result |= 1 << (bits - 1 - i)
    return result


# Examples
print(rotate_left(13, 2, 4))  # 11 (1101 -> 1011)
print(rotate_right(13, 2, 4))  # 7  (1101 -> 0111)
print(reverse_bits(13, 4))  # 11 (1101 -> 1011)
```

!!! note "Notes"
    - Bit rotation for cryptography, encoding
    - Bit reversal for algorithms

<hr class="snippet-divider">

### Bit field extraction and packing

`math` `bit` `extract` `pack` `field` `complex`

Extract and pack bit fields

```python
def extract_bits(a, start, length):
    """Extract a bit field from integer."""
    mask = (1 << length) - 1
    return (a >> start) & mask


def pack_bits(*bits):
    """Pack a sequence of bits into an integer."""
    result = 0
    for i, bit in enumerate(reversed(bits)):
        result |= (bit & 1) << i
    return result


# Examples
value = 0b11011010
print(extract_bits(value, 2, 3))  # 6 (110)
print(pack_bits(1, 0, 1, 1))  # 13 (1101)
```

!!! note "Notes"
    - Useful for binary protocols
    - Bit field manipulation

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in bit operations

`math` `bit` `error-handling` `edge-case` `validation`

Robust bit operations with error handling

```python
def safe_bitwise_and(a, b):
    """Safe bitwise AND with error handling."""
    try:
        return a & b
    except Exception as e:
        print(f"Error: {e}")
        return None


def safe_shift(a, n):
    """Safe shift with error handling."""
    try:
        return a << n
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test edge cases
print(safe_bitwise_and(5, "a"))  # Error, returns None
print(safe_shift(5, -1))  # Error, returns None
```

!!! note "Notes"
    - Handles invalid types and negative shifts
    - Error messages for user input

<hr class="snippet-divider">

### Performance comparison

`math` `bit` `performance` `benchmarking`

Benchmark bitwise operations

```python
import time


def benchmark_bitwise_operations():
    """Benchmark bitwise AND, OR, XOR."""
    a, b = 123456, 654321
    n = 1000000

    start = time.time()
    for _ in range(n):
        a & b
    and_time = time.time() - start

    start = time.time()
    for _ in range(n):
        a | b
    or_time = time.time() - start

    start = time.time()
    for _ in range(n):
        a ^ b
    xor_time = time.time() - start

    print(f"AND: {and_time:.6f}s, OR: {or_time:.6f}s, XOR: {xor_time:.6f}s")


# benchmark_bitwise_operations()
```

!!! note "Notes"
    - Bitwise operations are extremely fast
    - Useful for performance-critical code

<hr class="snippet-divider">

## Practical Examples

###  Permissions, flags, and encoding

`math` `bit` `permissions` `flags` `encoding`

Use bit operations for permissions and flags

```python
def has_permission(flags, mask):
    """Check if permission bit(s) are set."""
    return (flags & mask) == mask


def set_permission(flags, mask):
    """Set permission bit(s)."""
    return flags | mask


def clear_permission(flags, mask):
    """Clear permission bit(s)."""
    return flags & ~mask


def toggle_permission(flags, mask):
    """Toggle permission bit(s)."""
    return flags ^ mask


# Examples
READ, WRITE, EXEC = 0b100, 0b010, 0b001
flags = 0b101
print(has_permission(flags, READ))  # True
print(set_permission(flags, WRITE))  # 0b111
print(clear_permission(flags, READ))  # 0b001
print(toggle_permission(flags, EXEC))  # 0b100
```

!!! note "Notes"
    - Permissions and flags in systems
    - Encoding/decoding values
    - Useful for config and protocols

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Number Conversion](number_conversion.md)
- **Reference**: See [📂 Linear Algebra](linear_algebra.md)

## 🏷️ Tags

`math`, `bit`, `bitwise`, `mask`, `shift`, `flags`, `permissions`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Bit Operations Support Low-Level and Performance-Critical Code
- Use for Flags, Permissions, and Encoding
- Edge Case Handling Ensures Robustness
- Extremely Fast for Integer Operations
