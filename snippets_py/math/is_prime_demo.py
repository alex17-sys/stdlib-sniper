# 🧩 Check if number is prime
def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Check odd divisors up to square root
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


# Basic prime checks
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(17))  # True
print(is_prime(25))  # False
print(is_prime(1))  # False
print(is_prime(0))  # False


# 🧩 Get next prime number
# Function is defined in one of the above code block (is_prime)


def next_prime(number):
    """Find the next prime number greater than the given number."""
    if number < 2:
        return 2

    candidate = number + 1
    if candidate % 2 == 0:
        candidate += 1  # Start with odd number

    while not is_prime(candidate):
        candidate += 2  # Only check odd numbers

    return candidate


def previous_prime(number):
    """Find the previous prime number less than the given number."""
    if number <= 2:
        return None

    candidate = number - 1
    if candidate % 2 == 0:
        candidate -= 1  # Start with odd number

    while candidate > 2 and not is_prime(candidate):
        candidate -= 2  # Only check odd numbers

    return candidate if candidate >= 2 else None


# Examples
print(next_prime(10))  # 11
print(next_prime(17))  # 19
print(previous_prime(10))  # 7
print(previous_prime(17))  # 13


# 🧩 Check if number is composite
# Function is defined in one of the above code block (is_prime)


def is_composite(number):
    """Check if number is composite (not prime and not 1)."""
    if number < 2:
        return False
    return not is_prime(number)


def is_prime_or_composite(number):
    """Classify number as prime, composite, or neither."""
    if number < 2:
        return "neither"
    elif is_prime(number):
        return "prime"
    else:
        return "composite"


# Examples
print(is_composite(4))  # True
print(is_composite(6))  # True
print(is_composite(2))  # False
print(is_composite(1))  # False

print(is_prime_or_composite(2))  # "prime"
print(is_prime_or_composite(4))  # "composite"
print(is_prime_or_composite(1))  # "neither"


# 🧩 Optimized prime checking
def is_prime_optimized(number):
    """Optimized prime check with early termination."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    # Check divisors of form 6k ± 1 up to square root
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def is_prime_miller_rabin(number, k=5):
    """Miller-Rabin primality test (probabilistic)."""
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False

    # Write number as 2^r * d + 1
    r, d = 0, number - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test with first few prime bases
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for base in bases[:k]:
        if base >= number:
            continue
        if not _miller_rabin_test(number, base, r, d):
            return False
    return True


def _miller_rabin_test(n, a, r, d):
    """Helper function for Miller-Rabin test."""
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


# Examples
print(is_prime_optimized(1000003))  # True
print(is_prime_miller_rabin(1000003))  # True


# 🧩 Prime factorization
def prime_factors(number):
    """Find prime factorization of a number."""
    if number < 2:
        return []

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    if number > 1:
        factors.append(number)

    return factors


def prime_factorization_dict(number):
    """Get prime factorization as dictionary with exponents."""
    factors = prime_factors(number)
    factorization = {}

    for factor in factors:
        factorization[factor] = factorization.get(factor, 0) + 1

    return factorization


def count_prime_factors(number):
    """Count total number of prime factors (with multiplicity)."""
    return len(prime_factors(number))


def count_distinct_prime_factors(number):
    """Count number of distinct prime factors."""
    return len(set(prime_factors(number)))


# Examples
print(prime_factors(12))  # [2, 2, 3]
print(prime_factorization_dict(12))  # {2: 2, 3: 1}
print(count_prime_factors(12))  # 3
print(count_distinct_prime_factors(12))  # 2


# 🧩 Generate prime numbers
# Function is defined in one of the above code block (is_prime)


def generate_primes_up_to(limit):
    """Generate all prime numbers up to limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []

    # Initialize sieve
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    # Mark non-primes
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    # Collect primes
    return [i for i in range(limit + 1) if sieve[i]]


def generate_n_primes(n):
    """Generate first n prime numbers."""
    if n <= 0:
        return []

    primes = []
    candidate = 2

    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes


def prime_range(start, end):
    """Generate prime numbers in range [start, end]."""
    if start > end:
        return []

    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)

    return primes


# Examples
print(generate_primes_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(generate_n_primes(5))  # [2, 3, 5, 7, 11]
print(prime_range(10, 30))  # [11, 13, 17, 19, 23, 29]


# 🧩 Prime number properties
# Function is defined in one of the above code block (is_prime)


def is_twin_prime(number):
    """Check if number is part of a twin prime pair."""
    return is_prime(number) and (is_prime(number - 2) or is_prime(number + 2))


def is_safe_prime(number):
    """Check if number is a safe prime (p = 2q + 1 where q is prime)."""
    if not is_prime(number):
        return False
    return is_prime((number - 1) // 2)


def is_mersenne_prime(number):
    """Check if number is a Mersenne prime (2^p - 1 where p is prime)."""
    if number <= 1:
        return False

    # Check if number + 1 is a power of 2
    mersenne_form = number + 1
    if mersenne_form & (mersenne_form - 1) != 0:
        return False

    # Find the exponent
    exponent = 0
    temp = mersenne_form
    while temp > 1:
        temp >>= 1
        exponent += 1

    return is_prime(exponent)


def is_fibonacci_prime(number):
    """Check if number is both Fibonacci and prime."""
    if not is_prime(number):
        return False

    # Check if it's a Fibonacci number
    def is_fibonacci(n):
        if n < 0:
            return False
        if n == 0:
            return True

        # Check if 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
        val = 5 * n * n
        return _is_perfect_square(val + 4) or _is_perfect_square(val - 4)

    def _is_perfect_square(n):
        if n < 0:
            return False
        root = int(n**0.5)
        return root * root == n

    return is_fibonacci(number)


# Examples
print(is_twin_prime(5))  # True (3, 5, 7)
print(is_safe_prime(7))  # True (7 = 2*3 + 1)
print(is_mersenne_prime(7))  # True (2^3 - 1 = 7)
print(is_fibonacci_prime(2))  # True (2 is both Fibonacci and prime)


# 🧩 Handle edge cases in prime checking
import math


# Function is defined in one of the above code block (is_prime)


def robust_is_prime(number):
    """Robust prime check with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")

    if math.isnan(number):
        return False

    if math.isinf(number):
        return False

    # Convert to integer
    if isinstance(number, float):
        if number != int(number):
            return False
        number = int(number)

    if number < 0:
        return False

    return is_prime(number)


def validate_prime_input(number):
    """Validate input for prime number operations."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")

    if math.isnan(number) or math.isinf(number):
        raise ValueError("Number must be finite")

    if isinstance(number, float) and number != int(number):
        raise ValueError("Number must be integer")

    return int(number)


# Test edge cases
try:
    print(robust_is_prime(float("nan")))  # False
    print(robust_is_prime(float("inf")))  # False
    print(robust_is_prime(-5))  # False
    print(robust_is_prime(2.0))  # True
    print(robust_is_prime(2.5))  # False
except TypeError as e:
    print(f"Error: {e}")


# 🧩 Performance optimization
import time


# Function is defined in one of the above code block (is_prime)


# Function is defined in one of the above code block (is_prime_optimized)


# Function is defined in one of the above code block (is_prime_miller_rabin)


def benchmark_prime_methods():
    """Benchmark different prime checking methods."""
    test_numbers = [1000003, 1000007, 1000009, 1000013, 1000019]

    # Method 1: Basic prime check
    start = time.time()
    _ = [is_prime(n) for n in test_numbers]
    time1 = time.time() - start

    # Method 2: Optimized prime check
    start = time.time()
    _ = [is_prime_optimized(n) for n in test_numbers]
    time2 = time.time() - start

    # Method 3: Miller-Rabin test
    start = time.time()
    _ = [is_prime_miller_rabin(n) for n in test_numbers]
    time3 = time.time() - start

    print(f"Basic: {time1:.6f}s")
    print(f"Optimized: {time2:.6f}s")
    print(f"Miller-Rabin: {time3:.6f}s")
    print(f"Optimized speedup: {time1 / time2:.2f}x")


# benchmark_prime_methods()


# 🧩 Cryptographic applications
import math


# Function is defined in one of the above code block (is_prime_miller_rabin)


def generate_large_prime(bits=256):
    """Generate a large prime number for cryptographic use."""
    import random

    def random_odd_number(bits):
        """Generate random odd number with specified bit length."""
        number = random.getrandbits(bits)
        # Ensure it's odd and has the right bit length
        number |= 1  # Make odd
        number |= 1 << (bits - 1)  # Set highest bit
        return number

    while True:
        candidate = random_odd_number(bits)
        if is_prime_miller_rabin(candidate, k=10):
            return candidate


def is_probable_prime(number, confidence=0.99):
    """Check if number is probably prime with given confidence."""
    if number < 2:
        return False

    # Calculate number of Miller-Rabin tests needed
    # For confidence 0.99, we need about 5 tests
    k = max(5, int(-math.log(1 - confidence) / math.log(4)))

    return is_prime_miller_rabin(number, k)


# Example
large_prime = generate_large_prime(64)  # 64-bit prime
print(f"Generated prime: {large_prime}")
print(f"Is probable prime: {is_probable_prime(large_prime)}")


# 🧩 Mathematical research
# Function is defined in one of the above code block (generate_primes_up_to)


# Function is defined in one of the above code block (is_twin_prime)


def analyze_prime_distribution(limit):
    """Analyze distribution of prime numbers up to limit."""
    primes = generate_primes_up_to(limit)

    analysis = {
        "total_primes": len(primes),
        "density": len(primes) / limit,
        "largest_prime": max(primes) if primes else None,
        "twin_primes": sum(1 for p in primes if is_twin_prime(p)),
        "gaps": [primes[i + 1] - primes[i] for i in range(len(primes) - 1)],
    }

    if analysis["gaps"]:
        analysis["avg_gap"] = sum(analysis["gaps"]) / len(analysis["gaps"])
        analysis["max_gap"] = max(analysis["gaps"])
        analysis["min_gap"] = min(analysis["gaps"])

    return analysis


def find_prime_patterns(limit):
    """Find interesting patterns in prime numbers."""
    primes = generate_primes_up_to(limit)
    patterns = {"consecutive_pairs": [], "arithmetic_sequences": [], "palindromic_primes": []}

    # Find consecutive prime pairs
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            patterns["consecutive_pairs"].append((primes[i], primes[i + 1]))

    # Find palindromic primes
    for prime in primes:
        if str(prime) == str(prime)[::-1]:
            patterns["palindromic_primes"].append(prime)

    return patterns


# Example
analysis = analyze_prime_distribution(1000)
print(f"Primes up to 1000: {analysis['total_primes']}")
print(f"Prime density: {analysis['density']:.4f}")
print(f"Twin primes: {analysis['twin_primes']}")

patterns = find_prime_patterns(1000)
print(f"Twin prime pairs: {len(patterns['consecutive_pairs'])}")
print(f"Palindromic primes: {patterns['palindromic_primes']}")
