# 🧩 Calculate factorial
def factorial(n):
    """Calculate factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Basic factorial calculations
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(10))  # 3628800


# 🧩 Calculate factorial recursively
def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Examples
print(factorial_recursive(5))  # 120
print(factorial_recursive(6))  # 720
print(factorial_recursive(0))  # 1


# 🧩 Calculate double factorial
def double_factorial(n):
    """Calculate double factorial n!! (n * (n-2) * (n-4) * ...)."""
    if n < 0:
        raise ValueError("Double factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result


# Examples
print(double_factorial(5))  # 15 (5 * 3 * 1)
print(double_factorial(6))  # 48 (6 * 4 * 2)
print(double_factorial(7))  # 105 (7 * 5 * 3 * 1)
print(double_factorial(8))  # 384 (8 * 6 * 4 * 2)


# 🧩 Calculate falling factorial
def falling_factorial(n, k):
    """Calculate falling factorial (n)_k = n * (n-1) * ... * (n-k+1)."""
    if k < 0:
        raise ValueError("k must be non-negative")
    if k > n:
        return 0

    result = 1
    for i in range(k):
        result *= n - i
    return result


def rising_factorial(n, k):
    """Calculate rising factorial n^(k) = n * (n+1) * ... * (n+k-1)."""
    if k < 0:
        raise ValueError("k must be non-negative")

    result = 1
    for i in range(k):
        result *= n + i
    return result


# Examples
print(falling_factorial(5, 3))  # 60 (5 * 4 * 3)
print(falling_factorial(5, 5))  # 120 (5!)
print(rising_factorial(3, 4))  # 360 (3 * 4 * 5 * 6)


# 🧩 Calculate subfactorial
def subfactorial(n):
    """Calculate subfactorial !n (derangement number)."""
    if n < 0:
        raise ValueError("Subfactorial is not defined for negative numbers")
    if n == 0:
        return 1
    if n == 1:
        return 0

    # Use recurrence relation: !n = (n-1) * (!(n-1) + !(n-2))
    prev2, prev1 = 1, 0
    for i in range(2, n + 1):
        current = (i - 1) * (prev1 + prev2)
        prev2, prev1 = prev1, current

    return prev1


# Examples
print(subfactorial(0))  # 1
print(subfactorial(1))  # 0
print(subfactorial(2))  # 1
print(subfactorial(3))  # 2
print(subfactorial(4))  # 9


# 🧩 Calculate factorial with memoization
def factorial_memoized(n, memo=None):
    """Calculate factorial with memoization for efficiency."""
    if memo is None:
        memo = {}

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = n * factorial_memoized(n - 1, memo)
    return memo[n]


def factorial_cache():
    """Create a factorial calculator with persistent cache."""
    cache = {0: 1, 1: 1}

    def calc_factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n in cache:
            return cache[n]

        result = n * calc_factorial(n - 1)
        cache[n] = result
        return result

    return calc_factorial


# Examples
print(factorial_memoized(5))  # 120
print(factorial_memoized(5))  # 120 (from cache)

factorial_calc = factorial_cache()
print(factorial_calc(6))  # 720
print(factorial_calc(7))  # 5040 (uses cached 6!)


# 🧩 Calculate factorial approximation
import math


def factorial(n):
    # Function is defined in one of the above code block
    pass


def factorial_approximation(n):
    """Calculate factorial using Stirling's approximation."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    # Stirling's approximation: n! ≈ √(2πn) * (n/e)^n
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n


def factorial_log(n):
    """Calculate natural logarithm of factorial."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 0

    # Use log(n!) = log(1) + log(2) + ... + log(n)
    return sum(math.log(i) for i in range(1, n + 1))


def factorial_log_optimized(n):
    """Calculate natural logarithm of factorial using math.lgamma."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 0

    # Use math.lgamma(n+1) which is log(Γ(n+1)) = log(n!)
    return math.lgamma(n + 1)


# Examples
print(factorial_approximation(10))  # ~3628800.0 (approximate)
print(factorial(10))  # 3628800 (exact)
print(factorial_log(10))  # ~15.104 (log of 10!)
print(factorial_log_optimized(10))  # ~15.104 (using lgamma)


# 🧩 Handle edge cases in factorial calculations
import math


def factorial(n):
    # Function is defined in one of the above code block
    pass


def robust_factorial(n):
    """Robust factorial calculation with edge case handling."""
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be numeric")

    if math.isnan(n) or math.isinf(n):
        raise ValueError("Input must be finite")

    if isinstance(n, float):
        if n != int(n):
            raise ValueError("Input must be integer")
        n = int(n)

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n > 20:
        raise ValueError("Factorial too large for exact calculation")

    return factorial(n)


def factorial_with_overflow_check(n):
    """Calculate factorial with overflow checking."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        new_result = result * i
        if new_result < result:  # Overflow check
            raise OverflowError(f"Factorial overflow at n={i}")
        result = new_result

    return result


# Test edge cases
try:
    print(robust_factorial(5))  # 120
    print(robust_factorial(5.0))  # 120
    print(robust_factorial(21))  # ValueError
    print(robust_factorial(-1))  # ValueError
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time


def factorial(n):
    # Function is defined in one of the above code block
    pass


def factorial_memoized(n, memo=None):
    # Function is defined in one of the above code block
    pass


def factorial_recursive(n):
    # Function is defined in one of the above code block
    pass


def benchmark_factorial_methods():
    """Benchmark different factorial calculation methods."""
    test_values = [5, 10, 15, 20]

    # Method 1: Iterative
    start = time.time()
    _ = [factorial(n) for n in test_values]
    time1 = time.time() - start

    # Method 2: Recursive
    start = time.time()
    _ = [factorial_recursive(n) for n in test_values]
    time2 = time.time() - start

    # Method 3: Memoized
    start = time.time()
    _ = [factorial_memoized(n) for n in test_values]
    time3 = time.time() - start

    print(f"Iterative: {time1:.6f}s")
    print(f"Recursive: {time2:.6f}s")
    print(f"Memoized: {time3:.6f}s")
    print(f"Recursive overhead: {time2 / time1:.2f}x")


# benchmark_factorial_methods()


# 🧩 Combinatorial calculations
def factorial(n):
    # Function is defined in one of the above code block
    pass


def falling_factorial(n, k):
    # Function is defined in one of the above code block
    pass


def combination(n, k):
    """Calculate combination C(n,k) = n! / (k! * (n-k)!)."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Use falling factorial for efficiency
    return falling_factorial(n, k) // factorial(k)


def permutation(n, k):
    """Calculate permutation P(n,k) = n! / (n-k)!."""
    if k < 0 or k > n:
        return 0

    return falling_factorial(n, k)


def multinomial_coefficient(n, *k_values):
    """Calculate multinomial coefficient n! / (k1! * k2! * ... * km!)."""
    if sum(k_values) != n:
        raise ValueError("Sum of k values must equal n")

    denominator = 1
    for k in k_values:
        denominator *= factorial(k)

    return factorial(n) // denominator


# Examples
print(combination(5, 2))  # 10
print(permutation(5, 2))  # 20
print(multinomial_coefficient(6, 2, 2, 2))  # 90


# 🧩 Probability calculations
def combination(n, k):
    # Function is defined in one of the above code block
    pass


def probability_exact_k_successes(n, k, p):
    """Calculate probability of exactly k successes in n trials (binomial)."""
    if k < 0 or k > n:
        return 0

    # P(X = k) = C(n,k) * p^k * (1-p)^(n-k)
    return combination(n, k) * (p**k) * ((1 - p) ** (n - k))


def probability_at_most_k_successes(n, k, p):
    """Calculate probability of at most k successes in n trials."""
    return sum(probability_exact_k_successes(n, i, p) for i in range(k + 1))


def expected_value_binomial(n, p):
    """Calculate expected value of binomial distribution."""
    return n * p


def variance_binomial(n, p):
    """Calculate variance of binomial distribution."""
    return n * p * (1 - p)


# Examples
n, p = 10, 0.3
print(f"P(X = 3): {probability_exact_k_successes(n, 3, p):.4f}")
print(f"P(X ≤ 3): {probability_at_most_k_successes(n, 3, p):.4f}")
print(f"E[X]: {expected_value_binomial(n, p)}")
print(f"Var[X]: {variance_binomial(n, p):.2f}")
