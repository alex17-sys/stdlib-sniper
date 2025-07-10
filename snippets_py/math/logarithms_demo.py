# 🧩 Basic logarithmic functions
import math


def log(x, base=math.e):
    """Calculate logarithm of x with given base."""
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")

    return math.log(x, base)


def ln(x):
    """Calculate natural logarithm (base e)."""
    if x <= 0:
        raise ValueError("Natural logarithm is not defined for non-positive numbers")
    return math.log(x)


def log10(x):
    """Calculate common logarithm (base 10)."""
    if x <= 0:
        raise ValueError("Common logarithm is not defined for non-positive numbers")
    return math.log10(x)


def log2(x):
    """Calculate binary logarithm (base 2)."""
    if x <= 0:
        raise ValueError("Binary logarithm is not defined for non-positive numbers")
    return math.log2(x)


# Basic logarithmic calculations
print(ln(math.e))  # 1.0
print(log10(100))  # 2.0
print(log2(8))  # 3.0
print(log(27, 3))  # 3.0


# 🧩 Logarithmic properties and identities
import math


# Function is defined in one of the above code block (log)


def log_product(x, y, base=math.e):
    """Calculate log(x*y) = log(x) + log(y)."""
    return log(x, base) + log(y, base)


def log_quotient(x, y, base=math.e):
    """Calculate log(x/y) = log(x) - log(y)."""
    return log(x, base) - log(y, base)


def log_power(x, n, base=math.e):
    """Calculate log(x^n) = n*log(x)."""
    return n * log(x, base)


def log_root(x, n, base=math.e):
    """Calculate log(ⁿ√x) = log(x)/n."""
    return log(x, base) / n


def change_of_base(x, old_base, new_base):
    """Change logarithm base: log_new(x) = log_old(x) / log_old(new_base)."""
    return log(x, old_base) / log(new_base, old_base)


# Examples
print(f"log(6) = log(2*3) = {log_product(2, 3):.3f}")
print(f"log(2) = {log(2):.3f}")
print(f"log(3) = {log(3):.3f}")
print(f"Sum: {log(2) + log(3):.3f}")

print(f"log(8) = log(2³) = {log_power(2, 3):.3f}")
print(f"3*log(2) = {3 * log(2):.3f}")


# 🧩 Exponential functions
import math


# Function is defined in one of the above code block (log10)


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def exp_base(x, base=math.e):
    """Calculate base^x."""
    if base <= 0:
        raise ValueError("Base must be positive")
    return base**x


def exp_series(x, terms=10):
    """Calculate e^x using Taylor series: 1 + x + x²/2! + x³/3! + ..."""
    result = 0
    for n in range(terms):
        result += (x**n) / math.factorial(n)
    return result


def exp_approx(x):
    """Fast approximation of e^x for small x."""
    if abs(x) < 0.1:
        return 1 + x + (x**2) / 2 + (x**3) / 6
    return math.exp(x)


# Examples
print(exp(1))  # e ≈ 2.718
print(exp(0))  # 1.0
print(exp(-1))  # 1/e ≈ 0.368
print(exp_base(3, 2))  # 2³ = 8


# 🧩 Logarithmic equations and solving
import math


# Function is defined in one of the above code block (log)


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def solve_log_equation(base, result):
    """Solve log_b(x) = result for x."""
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")

    return base**result


def solve_exp_equation(base, result):
    """Solve base^x = result for x."""
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if result <= 0:
        raise ValueError("Result must be positive")

    return log(result, base)


def solve_log_inequality(base, result, direction=">"):
    """Solve log_b(x) direction result for x."""
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")

    if direction == ">":
        return base**result
    elif direction == "<":
        return base**result
    elif direction == ">=":
        return base**result
    elif direction == "<=":
        return base**result
    else:
        raise ValueError("Invalid direction")


def compound_interest(principal, rate, time, compounds_per_year=1):
    """Calculate compound interest: A = P(1 + r/n)^(nt)."""
    if principal <= 0 or rate < 0 or time < 0:
        raise ValueError("Invalid parameters")

    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    return amount


def continuous_compound_interest(principal, rate, time):
    """Calculate continuous compound interest: A = Pe^(rt)."""
    if principal <= 0 or rate < 0 or time < 0:
        raise ValueError("Invalid parameters")

    rate_decimal = rate / 100
    amount = principal * exp(rate_decimal * time)
    return amount


# Examples
x = solve_log_equation(2, 3)
print(f"log₂(x) = 3 → x = {x}")

x = solve_exp_equation(2, 8)
print(f"2^x = 8 → x = {x}")

amount = compound_interest(1000, 5, 10)  # 5% for 10 years
print(f"Compound interest: ${amount:.2f}")

amount = continuous_compound_interest(1000, 5, 10)
print(f"Continuous compound: ${amount:.2f}")


# 🧩 Logarithmic scales and transformations
import math


# Function is defined in one of the above code block (log)


# Function is defined in one of the above code block (ln)


def to_log_scale(values, base=10):
    """Convert values to logarithmic scale."""
    return [log(x, base) for x in values]


def from_log_scale(log_values, base=10):
    """Convert logarithmic scale back to original values."""
    return [base**x for x in log_values]


def log_normalize(values):
    """Normalize values using logarithmic transformation."""
    if not values:
        return []

    min_val = min(values)
    if min_val <= 0:
        # Shift all values to make them positive
        shift = abs(min_val) + 1
        values = [x + shift for x in values]

    log_values = [ln(x) for x in values]
    min_log = min(log_values)
    max_log = max(log_values)

    if max_log == min_log:
        return [0.5] * len(values)

    return [(x - min_log) / (max_log - min_log) for x in log_values]


def log_interpolate(x, x_values, y_values, base=10):
    """Interpolate using logarithmic scale."""
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have same length")

    # Convert to log scale
    log_x_values = [log(xi, base) for xi in x_values]
    log_y_values = [log(yi, base) for yi in y_values]

    # Find interpolation interval
    for i in range(len(log_x_values) - 1):
        if log_x_values[i] <= log(x, base) <= log_x_values[i + 1]:
            # Linear interpolation in log space
            t = (log(x, base) - log_x_values[i]) / (log_x_values[i + 1] - log_x_values[i])
            log_y = log_y_values[i] + t * (log_y_values[i + 1] - log_y_values[i])
            return base**log_y

    raise ValueError("x is outside the interpolation range")


# Examples
values = [1, 10, 100, 1000]
log_values = to_log_scale(values)
print(f"Original: {values}")
print(f"Log scale: {log_values}")

normalized = log_normalize([0.1, 1, 10, 100])
print(f"Log normalized: {normalized}")

interpolated = log_interpolate(50, [10, 100], [1, 2])
print(f"Log interpolated at 50: {interpolated:.3f}")


# 🧩 Logarithmic series and approximations
import math


# Function is defined in one of the above code block (log)


def log_power(x, n, base=math.e):
    """Calculate log(x^n) = n*log(x)."""
    return n * log(x, base)


def log_quotient(x, y, base=math.e):
    """Calculate log(x/y) = log(x) - log(y)."""
    return log(x, base) - log(y, base)


def log_product(x, y, base=math.e):
    """Calculate log(x*y) = log(x) + log(y)."""
    return log(x, base) + log(y, base)


def ln_series(x, terms=10):
    """Calculate ln(1+x) using Taylor series: x - x²/2 + x³/3 - ..."""
    if x <= -1:
        raise ValueError("Series converges only for x > -1")

    result = 0
    for n in range(1, terms + 1):
        term = ((-1) ** (n + 1)) * (x**n) / n
        result += term
    return result


def ln_continued_fraction(x, terms=10):
    """Calculate ln(x) using continued fraction approximation."""
    if x <= 0:
        raise ValueError("Input must be positive")

    # Use ln(x) = 2*arctanh((x-1)/(x+1)) for x > 0
    if x == 1:
        return 0

    y = (x - 1) / (x + 1)
    result = 0

    for i in range(terms, 0, -1):
        if i == 1:
            result = y
        else:
            result = y / (1 + result)

    return 2 * result


def log_approximation(x, base=10):
    """Fast approximation of logarithm."""
    if x <= 0:
        raise ValueError("Input must be positive")

    # Use ln(x) ≈ (x-1) - (x-1)²/2 + (x-1)³/3 for x near 1
    if abs(x - 1) < 0.1:
        y = x - 1
        ln_x = y - y**2 / 2 + y**3 / 3
    else:
        ln_x = math.log(x)

    if base == math.e:
        return ln_x
    else:
        return ln_x / math.log(base)


def log_identity_check(x, y, base=math.e):
    """Verify logarithmic identities."""
    identities = {
        "log(x*y) = log(x) + log(y)": abs(log_product(x, y, base) - log(x * y, base)),
        "log(x/y) = log(x) - log(y)": abs(log_quotient(x, y, base) - log(x / y, base)),
        "log(x^n) = n*log(x)": abs(log_power(x, 2, base) - log(x**2, base)),
    }
    return identities


# Examples
x = 0.5
print(f"ln(1+{x}) = {ln_series(x):.6f} (series)")
print(f"ln(1+{x}) = {math.log(1 + x):.6f} (exact)")

x = 2
print(f"ln({x}) = {ln_continued_fraction(x):.6f} (continued fraction)")
print(f"ln({x}) = {math.log(x):.6f} (exact)")

identities = log_identity_check(2, 3)
for identity, error in identities.items():
    print(f"{identity}: error = {error:.10f}")


# 🧩 Handle edge cases in logarithmic calculations
import math


def robust_log(x, base=math.e):
    """Robust logarithm calculation with edge case handling."""
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("Inputs must be numeric")

    if math.isnan(x) or math.isnan(base) or math.isinf(x) or math.isinf(base):
        raise ValueError("Inputs must be finite")

    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")

    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")

    return math.log(x, base)


def safe_log(x, base=math.e, default=None):
    """Safe logarithm that returns default for invalid inputs."""
    try:
        return robust_log(x, base)
    except (ValueError, TypeError):
        return default


def log_with_precision(x, base=math.e, precision=10):
    """Calculate logarithm with specified precision."""
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid inputs for logarithm")

    result = math.log(x, base)
    return round(result, precision)


def log_range_check(x, base=math.e, min_val=-100, max_val=100):
    """Check if logarithm result is within acceptable range."""
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid inputs for logarithm")

    result = math.log(x, base)
    if result < min_val or result > max_val:
        raise ValueError(f"Logarithm result {result} outside range [{min_val}, {max_val}]")

    return result


# Test edge cases
try:
    print(robust_log(1))  # 0.0
    print(robust_log(0.5))  # -0.693
    print(safe_log(-1, default="invalid"))  # "invalid"
    print(log_with_precision(2, 2, 5))  # 1.0
    print(log_range_check(1e-50))  # -115.13
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time
import math


# Function is defined in one of the above code block (log_approximation)


# Function is defined in one of the above code block (ln_series)


def benchmark_log_methods():
    """Benchmark different logarithmic calculation methods."""
    test_values = [0.1, 0.5, 1, 2, 10, 100]
    iterations = 100000

    # Method 1: Direct math.log
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            _ = math.log(x)
    time1 = time.time() - start

    # Method 2: Series approximation
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            if x > 0:
                _ = ln_series(x - 1, 5)
    time2 = time.time() - start

    # Method 3: Fast approximation
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            if x > 0:
                _ = log_approximation(x)
    time3 = time.time() - start

    print(f"Direct math.log: {time1:.6f}s")
    print(f"Series (5 terms): {time2:.6f}s")
    print(f"Fast approximation: {time3:.6f}s")
    print(f"Series overhead: {time2 / time1:.2f}x")
    print(f"Approximation speedup: {time1 / time3:.2f}x")


# benchmark_log_methods()


# 🧩 Information theory and entropy
# Function is defined in one of the above code block (log2)


def shannon_entropy(probabilities):
    """Calculate Shannon entropy: -Σ(p * log2(p))."""
    if not probabilities:
        return 0

    # Normalize probabilities
    total = sum(probabilities)
    if total == 0:
        return 0

    normalized = [p / total for p in probabilities]

    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * log2(p)

    return entropy


def cross_entropy(probabilities, predicted_probabilities):
    """Calculate cross-entropy: -Σ(p * log2(q))."""
    if len(probabilities) != len(predicted_probabilities):
        raise ValueError("Probability arrays must have same length")

    entropy = 0
    for p, q in zip(probabilities, predicted_probabilities):
        if p > 0 and q > 0:
            entropy -= p * log2(q)

    return entropy


def kl_divergence(p, q):
    """Calculate KL divergence: Σ(p * log2(p/q))."""
    if len(p) != len(q):
        raise ValueError("Probability arrays must have same length")

    divergence = 0
    for pi, qi in zip(p, q):
        if pi > 0 and qi > 0:
            divergence += pi * log2(pi / qi)

    return divergence


def mutual_information(joint_prob, marginal_p, marginal_q):
    """Calculate mutual information between two variables."""
    mi = 0
    for i, p_xy in enumerate(joint_prob):
        for j, p_xy_val in enumerate(p_xy):
            if p_xy_val > 0 and marginal_p[i] > 0 and marginal_q[j] > 0:
                mi += p_xy_val * log2(p_xy_val / (marginal_p[i] * marginal_q[j]))

    return mi


# Examples
prob = [0.25, 0.25, 0.25, 0.25]  # Uniform distribution
entropy = shannon_entropy(prob)
print(f"Shannon entropy: {entropy:.3f} bits")

p = [0.5, 0.3, 0.2]
q = [0.4, 0.4, 0.2]
kl = kl_divergence(p, q)
print(f"KL divergence: {kl:.3f}")


# 🧩 Scientific and engineering applications
import math


# Function is defined in one of the above code block (log10)


# Function is defined in one of the above code block (ln)


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def ph_calculation(hydrogen_concentration):
    """Calculate pH from hydrogen ion concentration."""
    if hydrogen_concentration <= 0:
        raise ValueError("Hydrogen concentration must be positive")

    return -log10(hydrogen_concentration)


def decibel_calculation(power_ratio):
    """Calculate decibels from power ratio."""
    if power_ratio <= 0:
        raise ValueError("Power ratio must be positive")

    return 10 * log10(power_ratio)


def magnitude_scale(brightness_ratio):
    """Calculate magnitude difference in astronomy."""
    if brightness_ratio <= 0:
        raise ValueError("Brightness ratio must be positive")

    return -2.5 * log10(brightness_ratio)


def half_life_decay(initial_amount, time, half_life):
    """Calculate remaining amount after radioactive decay."""
    if initial_amount <= 0 or time < 0 or half_life <= 0:
        raise ValueError("Invalid parameters")

    decay_constant = ln(2) / half_life
    remaining = initial_amount * exp(-decay_constant * time)
    return remaining


def earthquake_magnitude(amplitude, reference_amplitude=1):
    """Calculate Richter scale magnitude."""
    if amplitude <= 0 or reference_amplitude <= 0:
        raise ValueError("Amplitudes must be positive")

    return log10(amplitude / reference_amplitude)


# Examples
ph = ph_calculation(1e-7)  # Pure water
print(f"pH: {ph:.1f}")

db = decibel_calculation(100)  # 100x power increase
print(f"Decibels: {db:.1f} dB")

magnitude = magnitude_scale(100)  # 100x brighter
print(f"Magnitude difference: {magnitude:.1f}")

remaining = half_life_decay(100, 10, 5)  # 10 years, 5-year half-life
print(f"Remaining amount: {remaining:.1f}")

magnitude = earthquake_magnitude(1000)  # 1000x reference amplitude
print(f"Earthquake magnitude: {magnitude:.1f}")
