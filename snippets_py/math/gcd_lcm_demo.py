# 🧩 Calculate GCD using Euclidean algorithm
import math


def gcd(a, b):
    """Calculate greatest common divisor using math.gcd."""
    return math.gcd(a, b)


# Basic GCD calculations
print(gcd(48, 18))  # 6
print(gcd(54, 24))  # 6
print(gcd(7, 13))  # 1 (coprime)
print(gcd(0, 5))  # 5
print(gcd(-12, 18))  # 6


# 🧩 Calculate GCD recursively
def gcd_recursive(a, b):
    """Calculate GCD using recursive Euclidean algorithm."""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


# Examples
print(gcd_recursive(48, 18))  # 6
print(gcd_recursive(54, 24))  # 6
print(gcd_recursive(7, 13))  # 1


# 🧩 Calculate LCM
import math


def lcm(a, b):
    """Calculate least common multiple using GCD."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


# Basic LCM calculations
print(lcm(12, 18))  # 36
print(lcm(8, 12))  # 24
print(lcm(5, 7))  # 35
print(lcm(0, 5))  # 0


# 🧩 Calculate GCD for multiple numbers
import math


# See above defined function (lcm)


def gcd_multiple(*numbers):
    """Calculate GCD of multiple numbers."""
    if not numbers:
        raise ValueError("At least one number required")

    result = abs(numbers[0])
    for num in numbers[1:]:
        result = math.gcd(result, abs(num))
    return result


def lcm_multiple(*numbers):
    """Calculate LCM of multiple numbers."""
    if not numbers:
        raise ValueError("At least one number required")

    result = abs(numbers[0])
    for num in numbers[1:]:
        result = lcm(result, abs(num))
    return result


# Examples
print(gcd_multiple(48, 18, 12))  # 6
print(gcd_multiple(24, 36, 60))  # 12
print(lcm_multiple(12, 18, 24))  # 72
print(lcm_multiple(4, 6, 8, 12))  # 24


# 🧩 Extended Euclidean algorithm
def extended_gcd(a, b):
    """Calculate GCD and Bézout coefficients using extended Euclidean algorithm."""
    if b == 0:
        return abs(a), 1, 0

    gcd_val, x, y = extended_gcd(b, a % b)
    return gcd_val, y, x - (a // b) * y


def bezout_coefficients(a, b):
    """Find Bézout coefficients x, y such that ax + by = gcd(a, b)."""
    gcd_val, x, y = extended_gcd(a, b)
    return x, y


def modular_inverse(a, m):
    """Calculate modular multiplicative inverse of a modulo m."""
    if m <= 0:
        raise ValueError("Modulus must be positive")

    gcd_val, x, _ = extended_gcd(a, m)
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist")

    return (x % m + m) % m


# Examples
gcd_val, x, y = extended_gcd(48, 18)
print(f"GCD: {gcd_val}, Coefficients: x={x}, y={y}")  # GCD: 6, x=-1, y=3

x, y = bezout_coefficients(48, 18)
print(f"48*{x} + 18*{y} = {48 * x + 18 * y}")  # 48*(-1) + 18*3 = 6

inv = modular_inverse(3, 11)
print(f"3^(-1) mod 11 = {inv}")  # 4


# 🧩 Binary GCD algorithm
def binary_gcd(a, b):
    """Calculate GCD using binary GCD algorithm (Stein's algorithm)."""
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)

    # Find power of 2 in both numbers
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    # Remove factors of 2 from a
    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        # Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1

        # Now a and b are both odd
        if a > b:
            a, b = b, a
        b -= a

    return a << shift


# Examples
print(binary_gcd(48, 18))  # 6
print(binary_gcd(54, 24))  # 6
print(binary_gcd(7, 13))  # 1


# 🧩 GCD and LCM with prime factorization
def prime_factors(n):
    """Get prime factorization of a number."""
    if n < 2:
        return []

    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


def gcd_prime_factorization(a, b):
    """Calculate GCD using prime factorization."""
    if a == 0 or b == 0:
        return max(abs(a), abs(b))

    factors_a = prime_factors(abs(a))
    factors_b = prime_factors(abs(b))

    # Count prime factors
    count_a = {}
    for factor in factors_a:
        count_a[factor] = count_a.get(factor, 0) + 1

    count_b = {}
    for factor in factors_b:
        count_b[factor] = count_b.get(factor, 0) + 1

    # Find common factors with minimum exponents
    result = 1
    for prime in set(count_a.keys()) & set(count_b.keys()):
        result *= prime ** min(count_a[prime], count_b[prime])

    return result


def lcm_prime_factorization(a, b):
    """Calculate LCM using prime factorization."""
    if a == 0 or b == 0:
        return 0

    factors_a = prime_factors(abs(a))
    factors_b = prime_factors(abs(b))

    # Count prime factors
    count_a = {}
    for factor in factors_a:
        count_a[factor] = count_a.get(factor, 0) + 1

    count_b = {}
    for factor in factors_b:
        count_b[factor] = count_b.get(factor, 0) + 1

    # Find all factors with maximum exponents
    all_primes = set(count_a.keys()) | set(count_b.keys())
    result = 1
    for prime in all_primes:
        result *= prime ** max(count_a.get(prime, 0), count_b.get(prime, 0))

    return result


# Examples
print(gcd_prime_factorization(48, 18))  # 6
print(lcm_prime_factorization(12, 18))  # 36


# 🧩 Handle edge cases in GCD/LCM calculations
import math


# See above defined function (lcm)


def robust_gcd(a, b):
    """Robust GCD calculation with edge case handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")

    if math.isnan(a) or math.isnan(b) or math.isinf(a) or math.isinf(b):
        raise ValueError("Inputs must be finite")

    if isinstance(a, float):
        if a != int(a):
            raise ValueError("Inputs must be integers")
        a = int(a)

    if isinstance(b, float):
        if b != int(b):
            raise ValueError("Inputs must be integers")
        b = int(b)

    return math.gcd(a, b)


def robust_lcm(a, b):
    """Robust LCM calculation with edge case handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")

    if math.isnan(a) or math.isnan(b) or math.isinf(a) or math.isinf(b):
        raise ValueError("Inputs must be finite")

    if isinstance(a, float):
        if a != int(a):
            raise ValueError("Inputs must be integers")
        a = int(a)

    if isinstance(b, float):
        if b != int(b):
            raise ValueError("Inputs must be integers")
        b = int(b)

    return lcm(a, b)


# Test edge cases
try:
    print(robust_gcd(48, 18))  # 6
    print(robust_gcd(48.0, 18.0))  # 6
    print(robust_gcd(0, 5))  # 5
    print(robust_gcd(-12, 18))  # 6
    print(robust_lcm(12, 18))  # 36
    print(robust_lcm(0, 5))  # 0
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time
import math


# Function is defined in one of the above code block (binary_gcd)

# Function is defined in one of the above code block (gcd_prime_factorization)


def benchmark_gcd_methods():
    """Benchmark different GCD calculation methods."""
    test_pairs = [(48, 18), (123456, 789), (999999, 111111), (123456789, 987654321)]

    # Method 1: Euclidean algorithm
    start = time.time()
    _ = [math.gcd(a, b) for a, b in test_pairs]
    time1 = time.time() - start

    # Method 2: Binary GCD
    start = time.time()
    _ = [binary_gcd(a, b) for a, b in test_pairs]
    time2 = time.time() - start

    # Method 3: Prime factorization
    start = time.time()
    _ = [gcd_prime_factorization(a, b) for a, b in test_pairs]
    time3 = time.time() - start

    print(f"Euclidean: {time1:.6f}s")
    print(f"Binary: {time2:.6f}s")
    print(f"Prime factorization: {time3:.6f}s")
    print(f"Binary speedup: {time1 / time2:.2f}x")


# 🧩 Fraction simplification
import math


# Function is defined in one of the above code block (lcm)


def simplify_fraction(numerator, denominator):
    """Simplify fraction to lowest terms."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    gcd_val = math.gcd(numerator, denominator)
    return numerator // gcd_val, denominator // gcd_val


def add_fractions(a_num, a_den, b_num, b_den):
    """Add two fractions and return simplified result."""
    if a_den == 0 or b_den == 0:
        raise ValueError("Denominators cannot be zero")

    # Find common denominator
    lcm_val = lcm(a_den, b_den)

    # Convert to common denominator
    new_a_num = a_num * (lcm_val // a_den)
    new_b_num = b_num * (lcm_val // b_den)

    # Add numerators
    result_num = new_a_num + new_b_num
    result_den = lcm_val

    # Simplify
    return simplify_fraction(result_num, result_den)


# Examples
simplified = simplify_fraction(48, 18)
print(f"48/18 simplified: {simplified[0]}/{simplified[1]}")  # 8/3

result = add_fractions(1, 4, 1, 6)
print(f"1/4 + 1/6 = {result[0]}/{result[1]}")  # 5/12


# 🧩 Cryptography applications
import math


# See above defined function (modular_inverse)


def rsa_key_generation(p, q):
    """Generate RSA key pair using two prime numbers."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose public exponent e
    e = 65537  # Common choice
    while math.gcd(e, phi_n) != 1:
        e += 2

    # Calculate private exponent d
    d = modular_inverse(e, phi_n)

    return {"public_key": (n, e), "private_key": (n, d), "modulus": n, "phi": phi_n}


def rsa_encrypt(message, public_key):
    """Encrypt message using RSA public key."""
    n, e = public_key
    return pow(message, e, n)


def rsa_decrypt(ciphertext, private_key):
    """Decrypt message using RSA private key."""
    n, d = private_key
    return pow(ciphertext, d, n)


# Example (using small primes for demonstration)
def is_prime(n):
    """Simple prime check for demonstration."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Generate keys (using small primes for demo)
p, q = 61, 53
keys = rsa_key_generation(p, q)
print(f"Public key: {keys['public_key']}")
print(f"Private key: {keys['private_key']}")

# Encrypt and decrypt
message = 123
encrypted = rsa_encrypt(message, keys["public_key"])
decrypted = rsa_decrypt(encrypted, keys["private_key"])
print(f"Message: {message}, Encrypted: {encrypted}, Decrypted: {decrypted}")
