# 🧩 Check if number is even
def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


# Basic even checks
print(is_even(2))  # True
print(is_even(3))  # False
print(is_even(0))  # True
print(is_even(-4))  # True
print(is_even(-5))  # False


# 🧩 Check if number is odd
def is_odd(number):
    """Check if number is odd."""
    return number % 2 == 1


# Basic odd checks
print(is_odd(1))  # True
print(is_odd(2))  # False
print(is_odd(0))  # False
print(is_odd(-3))  # True
print(is_odd(-4))  # False


# 🧩 Get number parity
def get_parity(number):
    """Get number parity (0 for even, 1 for odd)."""
    return number % 2


def get_parity_string(number):
    """Get number parity as string."""
    return "even" if number % 2 == 0 else "odd"


# Examples
print(get_parity(4))  # 0 (even)
print(get_parity(7))  # 1 (odd)
print(get_parity_string(4))  # "even"
print(get_parity_string(7))  # "odd"


# 🧩 Check even/odd with bitwise operations
def is_even_bitwise(number):
    """Check if number is even using bitwise AND."""
    return (number & 1) == 0


def is_odd_bitwise(number):
    """Check if number is odd using bitwise AND."""
    return (number & 1) == 1


# Examples
print(is_even_bitwise(6))  # True
print(is_even_bitwise(7))  # False
print(is_odd_bitwise(6))  # False
print(is_odd_bitwise(7))  # True


# 🧩 Check even/odd for floating point
def is_even_float(number):
    """Check if float number is even (whole number and even)."""
    if not isinstance(number, (int, float)):
        return False

    # Check if it's a whole number
    if number != int(number):
        return False

    return int(number) % 2 == 0


def is_odd_float(number):
    """Check if float number is odd (whole number and odd)."""
    if not isinstance(number, (int, float)):
        return False

    # Check if it's a whole number
    if number != int(number):
        return False

    return int(number) % 2 == 1


# Examples
print(is_even_float(4.0))  # True
print(is_even_float(4.5))  # False (not whole)
print(is_even_float(3.0))  # False (odd)
print(is_odd_float(3.0))  # True
print(is_odd_float(3.5))  # False (not whole)


# 🧩 Check even/odd with tolerance
def is_even_tolerance(number, tolerance=1e-10):
    """Check if number is even with tolerance for floating point errors."""
    if not isinstance(number, (int, float)):
        return False

    # Round to nearest integer if very close
    rounded = round(number)
    if abs(number - rounded) <= tolerance:
        number = rounded

    # Check if it's a whole number
    if abs(number - int(number)) > tolerance:
        return False

    return int(number) % 2 == 0


def is_odd_tolerance(number, tolerance=1e-10):
    """Check if number is odd with tolerance for floating point errors."""
    if not isinstance(number, (int, float)):
        return False

    # Round to nearest integer if very close
    rounded = round(number)
    if abs(number - rounded) <= tolerance:
        number = rounded

    # Check if it's a whole number
    if abs(number - int(number)) > tolerance:
        return False

    return int(number) % 2 == 1


# Examples
print(is_even_tolerance(4.0000000001))  # True (within tolerance)
print(is_even_tolerance(4.1))  # False (not whole)
print(is_odd_tolerance(3.9999999999))  # True (within tolerance)


# 🧩 Check even/odd for sequences
def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def is_odd(number):
    """Check if number is odd."""
    return number % 2 == 1


def count_even_odd(numbers):
    """Count even and odd numbers in sequence."""
    even_count = sum(1 for n in numbers if is_even(n))
    odd_count = len(numbers) - even_count
    return even_count, odd_count


def filter_even_odd(numbers, keep_even=True):
    """Filter sequence to keep even or odd numbers."""
    if keep_even:
        return [n for n in numbers if is_even(n)]
    else:
        return [n for n in numbers if is_odd(n)]


def partition_even_odd(numbers):
    """Partition sequence into even and odd numbers."""
    even = []
    odd = []
    for n in numbers:
        if is_even(n):
            even.append(n)
        else:
            odd.append(n)
    return even, odd


# Examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(numbers)
print(f"Even: {even_count}, Odd: {odd_count}")  # Even: 5, Odd: 5

even_numbers = filter_even_odd(numbers, keep_even=True)
odd_numbers = filter_even_odd(numbers, keep_even=False)
print(f"Even: {even_numbers}")  # Even: [2, 4, 6, 8, 10]
print(f"Odd: {odd_numbers}")  # Odd: [1, 3, 5, 7, 9]

even, odd = partition_even_odd(numbers)
print(f"Even: {even}, Odd: {odd}")


# 🧩 Handle edge cases in even/odd checks
import math


def robust_is_even(number):
    """Robust even check with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")

    if math.isnan(number):
        return False

    if math.isinf(number):
        return False

    # Handle floating point numbers
    if isinstance(number, float):
        if number != int(number):
            return False
        number = int(number)

    return number % 2 == 0


def robust_is_odd(number):
    """Robust odd check with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")

    if math.isnan(number):
        return False

    if math.isinf(number):
        return False

    # Handle floating point numbers
    if isinstance(number, float):
        if number != int(number):
            return False
        number = int(number)

    return number % 2 == 1


# Test edge cases
try:
    print(robust_is_even(float("nan")))  # False
    print(robust_is_even(float("inf")))  # False
    print(robust_is_even(4.0))  # True
    print(robust_is_even(4.5))  # False
except TypeError as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def benchmark_even_odd():
    """Benchmark different even/odd checking methods."""
    numbers = list(range(-10000, 10000))

    # Method 1: Modulo operator
    start = time.time()
    _ = [n % 2 == 0 for n in numbers]
    time1 = time.time() - start

    # Method 2: Bitwise AND
    start = time.time()
    _ = [(n & 1) == 0 for n in numbers]
    time2 = time.time() - start

    # Method 3: Function call
    start = time.time()
    _ = [is_even(n) for n in numbers]
    time3 = time.time() - start

    print(f"Modulo: {time1:.6f}s")
    print(f"Bitwise: {time2:.6f}s")
    print(f"Function: {time3:.6f}s")
    print(f"Bitwise speedup: {time1 / time2:.2f}x")


# benchmark_even_odd()


# 🧩 Alternating pattern generation
def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def is_odd(number):
    """Check if number is odd."""
    return number % 2 == 1


def generate_alternating_pattern(length, start_even=True):
    """Generate alternating even/odd pattern."""
    pattern = []
    current = 0 if start_even else 1

    for _ in range(length):
        pattern.append(current)
        current = 2 if current == 1 else 1  # Alternate between 1 and 2

    return pattern


def generate_even_odd_sequence(start, end):
    """Generate sequence with even and odd numbers separated."""
    even = [n for n in range(start, end + 1) if is_even(n)]
    odd = [n for n in range(start, end + 1) if is_odd(n)]
    return even, odd


# Examples
pattern = generate_alternating_pattern(10, start_even=True)
print(f"Pattern: {pattern}")  # Pattern: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

even, odd = generate_even_odd_sequence(1, 10)
print(f"Even: {even}")  # Even: [2, 4, 6, 8, 10]
print(f"Odd: {odd}")  # Odd: [1, 3, 5, 7, 9]


# 🧩 Mathematical operations
def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def is_odd(number):
    """Check if number is odd."""
    return number % 2 == 1


def sum_even_odd(numbers):
    """Calculate sum of even and odd numbers separately."""
    even_sum = sum(n for n in numbers if is_even(n))
    odd_sum = sum(n for n in numbers if is_odd(n))
    return even_sum, odd_sum


def product_even_odd(numbers):
    """Calculate product of even and odd numbers separately."""
    even_product = 1
    odd_product = 1

    for n in numbers:
        if is_even(n):
            even_product *= n
        else:
            odd_product *= n

    return even_product, odd_product


def average_even_odd(numbers):
    """Calculate average of even and odd numbers separately."""
    even_numbers = [n for n in numbers if is_even(n)]
    odd_numbers = [n for n in numbers if is_odd(n)]

    even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
    odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

    return even_avg, odd_avg


# Examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = sum_even_odd(numbers)
print(f"Even sum: {even_sum}, Odd sum: {odd_sum}")  # Even sum: 30, Odd sum: 25

even_avg, odd_avg = average_even_odd(numbers)
print(f"Even average: {even_avg}, Odd average: {odd_avg}")  # Even average: 6.0, Odd average: 5.0
