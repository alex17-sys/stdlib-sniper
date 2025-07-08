# 🧩 Generate Fibonacci sequence
def fibonacci_sequence(n):
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


# Basic Fibonacci sequences
print(fibonacci_sequence(5))  # [0, 1, 1, 2, 3]
print(fibonacci_sequence(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci_sequence(1))  # [0]


# 🧩 Get nth Fibonacci number
def fibonacci(n):
    """Get the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Examples
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10))  # 55


# 🧩 Generate Fibonacci recursively
def fibonacci_recursive(n):
    """Get nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Examples
print(fibonacci_recursive(5))  # 5
print(fibonacci_recursive(6))  # 8
print(fibonacci_recursive(7))  # 13


# 🧩 Generate Fibonacci with memoization
def fibonacci_memoized(n, memo=None):
    """Get nth Fibonacci number with memoization."""
    if memo is None:
        memo = {0: 0, 1: 1}

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_cache():
    """Create a Fibonacci calculator with persistent cache."""
    cache = {0: 0, 1: 1}

    def calc_fibonacci(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n in cache:
            return cache[n]

        result = calc_fibonacci(n - 1) + calc_fibonacci(n - 2)
        cache[n] = result
        return result

    return calc_fibonacci


# Examples
print(fibonacci_memoized(10))  # 55
print(fibonacci_memoized(10))  # 55 (from cache)

fib_calc = fibonacci_cache()
print(fib_calc(15))  # 610
print(fib_calc(20))  # 6765 (uses cached values)


# 🧩 Generate Fibonacci using matrix exponentiation
def fibonacci_matrix(n):
    """Get nth Fibonacci number using matrix exponentiation."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    def matrix_multiply(a, b):
        """Multiply two 2x2 matrices."""
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def matrix_power(matrix, power):
        """Raise matrix to power using fast exponentiation."""
        if power == 0:
            return [[1, 0], [0, 1]]
        if power == 1:
            return matrix

        half = matrix_power(matrix, power // 2)
        squared = matrix_multiply(half, half)

        if power % 2 == 0:
            return squared
        else:
            return matrix_multiply(squared, matrix)

    # Fibonacci matrix: [[1, 1], [1, 0]]
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)

    return result_matrix[0][0]


# Examples
print(fibonacci_matrix(10))  # 55
print(fibonacci_matrix(20))  # 6765


# 🧩 Generate Fibonacci with Binet's formula
import math


def fibonacci_binet(n):
    """Get nth Fibonacci number using Binet's formula."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0

    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    # Binet's formula: F(n) = (φ^n - ψ^n) / √5
    result = (phi**n - psi**n) / math.sqrt(5)
    return round(result)


def fibonacci_binet_approximation(n):
    """Get approximate nth Fibonacci number using Binet's formula."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0

    # For large n, ψ^n becomes negligible
    phi = (1 + math.sqrt(5)) / 2
    return phi**n / math.sqrt(5)


# Examples
print(fibonacci_binet(10))  # 55
print(fibonacci_binet(20))  # 6765
print(fibonacci_binet_approximation(50))  # ~12586269025


# 🧩 Generate Fibonacci with different starting values
def lucas_sequence(n):
    """Generate Lucas sequence (starts with 2, 1)."""
    if n <= 0:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]

    sequence = [2, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def fibonacci_custom(a, b, n):
    """Generate Fibonacci-like sequence starting with a, b."""
    if n <= 0:
        return []
    if n == 1:
        return [a]
    if n == 2:
        return [a, b]

    sequence = [a, b]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def tribonacci_sequence(n):
    """Generate Tribonacci sequence (each number is sum of previous 3)."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    if n == 3:
        return [0, 1, 1]

    sequence = [0, 1, 1]
    for i in range(3, n):
        sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    return sequence


# Examples
print(lucas_sequence(8))  # [2, 1, 3, 4, 7, 11, 18, 29]
print(fibonacci_custom(1, 3, 6))  # [1, 3, 4, 7, 11, 18]
print(tribonacci_sequence(8))  # [0, 1, 1, 2, 4, 7, 13, 24]


# 🧩 Handle edge cases in Fibonacci calculations
import math


def fibonacci(n):
    # Function is defined in one of the above code block
    pass


def robust_fibonacci(n):
    """Robust Fibonacci calculation with edge case handling."""
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be numeric")

    if math.isnan(n) or math.isinf(n):
        raise ValueError("Input must be finite")

    if isinstance(n, float):
        if n != int(n):
            raise ValueError("Input must be integer")
        n = int(n)

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n > 1000:
        raise ValueError("Input too large for safe calculation")

    return fibonacci(n)


def fibonacci_with_overflow_check(n):
    """Calculate Fibonacci with overflow checking."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        new_b = a + b
        if new_b < b:  # Overflow check
            raise OverflowError(f"Fibonacci overflow at n={i}")
        a, b = b, new_b

    return b


# Test edge cases
try:
    print(robust_fibonacci(10))  # 55
    print(robust_fibonacci(10.0))  # 55
    print(robust_fibonacci(1001))  # ValueError
    print(robust_fibonacci(-1))  # ValueError
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time


def fibonacci(n):
    # Function is defined in one of the above code block
    pass


def fibonacci_recursive(n):
    # Function is defined in one of the above code block
    pass


def fibonacci_memoized(n, memo=None):
    # Function is defined in one of the above code block
    pass


def fibonacci_matrix(n):
    # Function is defined in one of the above code block
    pass


def benchmark_fibonacci_methods():
    """Benchmark different Fibonacci calculation methods."""
    test_values = [10, 20, 30, 35]

    # Method 1: Iterative
    start = time.time()
    _ = [fibonacci(n) for n in test_values]
    time1 = time.time() - start

    # Method 2: Recursive
    start = time.time()
    _ = [fibonacci_recursive(n) for n in test_values[:2]]  # Only small values
    time2 = time.time() - start

    # Method 3: Memoized
    start = time.time()
    _ = [fibonacci_memoized(n) for n in test_values]
    time3 = time.time() - start

    # Method 4: Matrix
    start = time.time()
    _ = [fibonacci_matrix(n) for n in test_values]
    time4 = time.time() - start

    print(f"Iterative: {time1:.6f}s")
    print(f"Recursive: {time2:.6f}s")
    print(f"Memoized: {time3:.6f}s")
    print(f"Matrix: {time4:.6f}s")
    print(f"Matrix speedup: {time1 / time4:.2f}x")


# benchmark_fibonacci_methods()


# 🧩 Fibonacci in nature and art
import math


def fibonacci_sequence(n):
    # Function is defined in one of the above code block
    pass


def fibonacci_spiral_points(n):
    """Generate points for Fibonacci spiral."""
    sequence = fibonacci_sequence(n)
    points = []
    angle = 0

    for i, radius in enumerate(sequence):
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
        angle += math.pi / 2  # 90 degrees

    return points


def fibonacci_rectangle(n):
    """Generate Fibonacci rectangle dimensions."""
    sequence = fibonacci_sequence(n + 1)
    rectangles = []

    for i in range(1, len(sequence)):
        width = sequence[i]
        height = sequence[i - 1]
        rectangles.append((width, height))

    return rectangles


def golden_ratio_approximation(n):
    """Approximate golden ratio using Fibonacci sequence."""
    if n < 2:
        return None

    sequence = fibonacci_sequence(n + 1)
    ratios = []

    for i in range(2, len(sequence)):
        ratio = sequence[i] / sequence[i - 1]
        ratios.append(ratio)

    return ratios


# Examples
spiral_points = fibonacci_spiral_points(8)
print(f"Spiral points: {spiral_points[:5]}")

rectangles = fibonacci_rectangle(5)
print(f"Rectangle dimensions: {rectangles}")

ratios = golden_ratio_approximation(10)
print(f"Golden ratio approximations: {[f'{r:.6f}' for r in ratios[-3:]]}")


# 🧩 Fibonacci in algorithms
def fibonacci_search(arr, target):
    """Search for target in sorted array using Fibonacci search."""
    # Initialize Fibonacci numbers
    fib2 = 0  # (k-2)th Fibonacci number
    fib1 = 1  # (k-1)th Fibonacci number
    fib = fib1 + fib2  # kth Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to len(arr)
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Initialize the offset
    offset = -1

    while fib > 1:
        # Check if fib2 is a valid index
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    # Compare last element
    if fib1 and offset + 1 < len(arr) and arr[offset + 1] == target:
        return offset + 1

    return -1


def fibonacci_heap_operations():
    """Demonstrate Fibonacci heap concepts."""
    # This is a conceptual demonstration
    operations = {
        "insert": "O(1) amortized",
        "extract_min": "O(log n) amortized",
        "decrease_key": "O(1) amortized",
        "delete": "O(log n) amortized",
    }
    return operations


# Example
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
target = 85
result = fibonacci_search(arr, target)
print(f"Found {target} at index: {result}")

heap_ops = fibonacci_heap_operations()
print(f"Fibonacci heap operations: {heap_ops}")
