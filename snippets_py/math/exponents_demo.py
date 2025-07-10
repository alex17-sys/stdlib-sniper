# 🧩 Basic exponential functions
import math


def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def square(x):
    """Calculate x squared."""
    return x**2


def cube(x):
    """Calculate x cubed."""
    return x**3


def nth_power(x, n):
    """Calculate x raised to the nth power."""
    return x**n


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


# Basic exponential calculations
print(power(2, 3))  # 8
print(square(5))  # 25
print(cube(3))  # 27
print(nth_power(2, 10))  # 1024
print(exp(1))  # e ≈ 2.718


# 🧩 Exponential properties and identities
def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def power_of_product(a, b, n):
    """Calculate (a*b)^n = a^n * b^n."""
    return power(a, n) * power(b, n)


def power_of_quotient(a, b, n):
    """Calculate (a/b)^n = a^n / b^n."""
    return power(a, n) / power(b, n)


def power_of_power(a, m, n):
    """Calculate (a^m)^n = a^(m*n)."""
    return power(a, m * n)


def product_of_powers(a, m, n):
    """Calculate a^m * a^n = a^(m+n)."""
    return power(a, m + n)


def quotient_of_powers(a, m, n):
    """Calculate a^m / a^n = a^(m-n)."""
    return power(a, m - n)


def negative_power(a, n):
    """Calculate a^(-n) = 1/a^n."""
    return 1 / power(a, n)


def zero_power(a):
    """Calculate a^0 = 1 (for any a ≠ 0)."""
    if a == 0:
        raise ValueError("0^0 is undefined")
    return 1


# Examples
print(f"(2*3)² = {power_of_product(2, 3, 2)}")
print(f"2² * 3² = {power(2, 2) * power(3, 2)}")

print(f"(2³)² = {power_of_power(2, 3, 2)}")
print(f"2^(3*2) = {power(2, 3 * 2)}")

print(f"2³ * 2² = {product_of_powers(2, 3, 2)}")
print(f"2^(3+2) = {power(2, 3 + 2)}")


# 🧩 Exponential growth and decay
import math


def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def exponential_growth(initial, rate, time):
    """Calculate exponential growth: P = P₀ * e^(rt)."""
    return initial * exp(rate * time)


def exponential_decay(initial, rate, time):
    """Calculate exponential decay: P = P₀ * e^(-rt)."""
    return initial * exp(-rate * time)


def compound_growth(initial, rate, time, periods=1):
    """Calculate compound growth: P = P₀ * (1 + r/n)^(nt)."""
    return initial * power(1 + rate / periods, periods * time)


def half_life_decay(initial, time, half_life):
    """Calculate decay using half-life: P = P₀ * (1/2)^(t/T)."""
    return initial * power(0.5, time / half_life)


def doubling_time(rate):
    """Calculate doubling time: T = log(2)/r."""
    return math.log(2) / rate


def half_life_from_rate(rate):
    """Calculate half-life from decay rate: T = log(2)/r."""
    return math.log(2) / rate


# Examples
population = exponential_growth(1000, 0.05, 10)  # 5% growth for 10 years
print(f"Population: {population:.0f}")

remaining = exponential_decay(100, 0.1, 5)  # 10% decay rate for 5 years
print(f"Remaining: {remaining:.1f}")

amount = compound_growth(1000, 0.05, 10, 12)  # Monthly compounding
print(f"Compound amount: {amount:.2f}")

doubling = doubling_time(0.05)  # 5% growth rate
print(f"Doubling time: {doubling:.1f} years")


# 🧩 Exponential equations and solving
import math


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def solve_exponential_equation(base, result):
    """Solve base^x = result for x."""
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if result <= 0:
        raise ValueError("Result must be positive")

    return math.log(result, base)


def solve_natural_exponential(result):
    """Solve e^x = result for x."""
    if result <= 0:
        raise ValueError("Result must be positive")

    return math.log(result)


def solve_power_equation(base, exponent, result):
    """Solve base^x = result for x when base and exponent are known."""
    if base <= 0:
        raise ValueError("Base must be positive")
    if result <= 0:
        raise ValueError("Result must be positive")

    return math.log(result, base)


def solve_exponential_inequality(base, result, direction=">"):
    """Solve base^x direction result for x."""
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if result <= 0:
        raise ValueError("Result must be positive")

    x = math.log(result, base)

    if direction == ">":
        return x
    elif direction == "<":
        return x
    elif direction == ">=":
        return x
    elif direction == "<=":
        return x
    else:
        raise ValueError("Invalid direction")


def newton_raphson_exponential(target, initial_guess=1, tolerance=1e-10, max_iterations=100):
    """Solve e^x = target using Newton-Raphson method."""
    x = initial_guess

    for _ in range(max_iterations):
        fx = exp(x) - target
        f_prime = exp(x)

        if abs(f_prime) < tolerance:
            break

        x_new = x - fx / f_prime

        if abs(x_new - x) < tolerance:
            return x_new

        x = x_new

    return x


# Examples
x = solve_exponential_equation(2, 8)
print(f"2^x = 8 → x = {x}")

x = solve_natural_exponential(math.e)
print(f"e^x = e → x = {x}")

x = newton_raphson_exponential(100)
print(f"e^x = 100 → x = {x:.6f}")
print(f"Verification: e^{x:.6f} = {exp(x):.6f}")


# 🧩 Exponential series and approximations
import math


def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def exp_series(x, terms=10):
    """Calculate e^x using Taylor series: 1 + x + x²/2! + x³/3! + ..."""
    result = 0
    for n in range(terms):
        result += (x**n) / math.factorial(n)
    return result


def exp_continued_fraction(x, terms=10):
    """Calculate e^x using continued fraction approximation."""
    if x == 0:
        return 1

    # Use e^x = 1 + x/(1 - x/(2 + x/(3 - x/(2 + x/(5 - x/(2 + ...))))))
    result = 0
    for i in range(terms, 0, -1):
        if i == 1:
            result = 1
        elif i % 2 == 0:
            result = i + x / result
        else:
            result = i - x / result

    return 1 + x / result


def exp_approx(x):
    """Fast approximation of e^x for small x."""
    if abs(x) < 0.1:
        return 1 + x + (x**2) / 2 + (x**3) / 6 + (x**4) / 24
    elif x > 0:
        # For positive x, use e^x = (e^(x/2))^2
        half = exp_approx(x / 2)
        return half * half
    else:
        # For negative x, use e^x = 1/e^(-x)
        return 1 / exp_approx(-x)


def exp_identity_check(x, y):
    """Verify exponential identities."""
    identities = {
        "e^(x+y) = e^x * e^y": abs(exp(x + y) - exp(x) * exp(y)),
        "e^(x-y) = e^x / e^y": abs(exp(x - y) - exp(x) / exp(y)),
        "(e^x)^y = e^(x*y)": abs(power(exp(x), y) - exp(x * y)),
    }
    return identities


def exp_error_analysis(x, terms_range=range(1, 11)):
    """Analyze error in exponential series approximation."""
    exact = exp(x)
    errors = []

    for terms in terms_range:
        approx = exp_series(x, terms)
        error = abs(exact - approx)
        errors.append((terms, error))

    return errors


# Examples
x = 1.5
print(f"e^{x} = {exp_series(x):.6f} (series)")
print(f"e^{x} = {exp(x):.6f} (exact)")

x = 0.5
approx = exp_approx(x)
print(f"e^{x} ≈ {approx:.6f} (approximation)")
print(f"e^{x} = {exp(x):.6f} (exact)")

identities = exp_identity_check(2, 3)
for identity, error in identities.items():
    print(f"{identity}: error = {error:.10f}")


# 🧩 Exponential interpolation and smoothing
def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def exp_interpolate(x, x_values, y_values):
    """Interpolate using exponential function."""
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have same length")

    if len(x_values) < 2:
        raise ValueError("Need at least 2 points for interpolation")

    # Find the two closest points
    distances = [abs(x - xi) for xi in x_values]
    min_idx = distances.index(min(distances))

    if min_idx == 0:
        idx1, idx2 = 0, 1
    elif min_idx == len(x_values) - 1:
        idx1, idx2 = len(x_values) - 2, len(x_values) - 1
    else:
        if distances[min_idx - 1] < distances[min_idx + 1]:
            idx1, idx2 = min_idx - 1, min_idx
        else:
            idx1, idx2 = min_idx, min_idx + 1

    # Exponential interpolation
    x1, x2 = x_values[idx1], x_values[idx2]
    y1, y2 = y_values[idx1], y_values[idx2]

    if x1 == x2:
        return y1

    if y1 <= 0 or y2 <= 0:
        # Fall back to linear interpolation for non-positive values
        t = (x - x1) / (x2 - x1)
        return y1 + t * (y2 - y1)

    # Use exponential interpolation: y = y1 * (y2/y1)^((x-x1)/(x2-x1))
    t = (x - x1) / (x2 - x1)
    ratio = y2 / y1
    return y1 * power(ratio, t)


def exp_smooth(values, alpha=0.5):
    """Apply exponential smoothing to time series."""
    if not values:
        return []

    smoothed = [values[0]]
    for i in range(1, len(values)):
        smoothed_value = alpha * values[i] + (1 - alpha) * smoothed[i - 1]
        smoothed.append(smoothed_value)

    return smoothed


def exp_weighted_average(values, weights):
    """Calculate exponential weighted average."""
    if len(values) != len(weights):
        raise ValueError("Values and weights must have same length")

    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Sum of weights cannot be zero")

    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight


# Examples
x_points = [0, 1, 2, 3, 4]
y_points = [1, 2, 4, 8, 16]  # Exponential growth

interpolated = exp_interpolate(1.5, x_points, y_points)
print(f"Exponential interpolated at 1.5: {interpolated:.3f}")

data = [10, 12, 11, 13, 12, 14, 13, 15]
smoothed = exp_smooth(data, 0.3)
print(f"Exponentially smoothed: {smoothed}")


# 🧩 Handle edge cases in exponential calculations
import math


def robust_power(base, exponent):
    """Robust power calculation with edge case handling."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Inputs must be numeric")

    if math.isnan(base) or math.isnan(exponent) or math.isinf(base) or math.isinf(exponent):
        raise ValueError("Inputs must be finite")

    if base == 0 and exponent <= 0:
        raise ValueError("0^0 and 0^(-n) are undefined")

    if base < 0 and not isinstance(exponent, int):
        raise ValueError("Negative base requires integer exponent")

    return base**exponent


def safe_exp(x):
    """Safe exponential calculation avoiding overflow."""
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be numeric")

    if math.isnan(x) or math.isinf(x):
        raise ValueError("Input must be finite")

    # Check for overflow
    if x > 700:  # Approximate limit for double precision
        raise OverflowError("Result would overflow")

    if x < -700:  # Approximate limit for underflow
        return 0

    return math.exp(x)


def exp_with_precision(x, precision=10):
    """Calculate exponential with specified precision."""
    if x <= 0 or x > 700:
        raise ValueError("Input out of valid range")

    result = math.exp(x)
    return round(result, precision)


def exp_range_check(x, min_val=1e-100, max_val=1e100):
    """Check if exponential result is within acceptable range."""
    if x < -700 or x > 700:
        raise ValueError(f"Exponent {x} outside safe range")

    result = math.exp(x)
    if result < min_val or result > max_val:
        raise ValueError(f"Exponential result {result} outside range [{min_val}, {max_val}]")

    return result


# Test edge cases
try:
    print(robust_power(2, 3))  # 8
    print(robust_power(0, 5))  # 0
    print(safe_exp(1))  # e
    print(exp_with_precision(1, 5))  # 2.71828
    print(exp_range_check(0))  # 1.0
    print(robust_power(0, 0))  # ValueError
except (TypeError, ValueError, OverflowError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time
import math


# Function is defined in one of the above code block (exp_approx)


# Function is defined in one of the above code block (exp_series)


def benchmark_exp_methods():
    """Benchmark different exponential calculation methods."""
    test_values = [-1, 0, 0.5, 1, 2, 5]
    iterations = 100000

    # Method 1: Direct math.exp
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            _ = math.exp(x)
    time1 = time.time() - start

    # Method 2: Series approximation
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            _ = exp_series(x, 5)
    time2 = time.time() - start

    # Method 3: Fast approximation
    start = time.time()
    for _ in range(iterations):
        for x in test_values:
            _ = exp_approx(x)
    time3 = time.time() - start

    print(f"Direct math.exp: {time1:.6f}s")
    print(f"Series (5 terms): {time2:.6f}s")
    print(f"Fast approximation: {time3:.6f}s")
    print(f"Series overhead: {time2 / time1:.2f}x")
    print(f"Approximation speedup: {time1 / time3:.2f}x")


# benchmark_exp_methods()


# 🧩 Financial and economic applications
import math


def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def compound_interest(principal, rate, time, compounds_per_year=1):
    """Calculate compound interest: A = P(1 + r/n)^(nt)."""
    if principal <= 0 or rate < 0 or time < 0:
        raise ValueError("Invalid parameters")

    rate_decimal = rate / 100
    amount = principal * power(1 + rate_decimal / compounds_per_year, compounds_per_year * time)
    return amount


def continuous_compound_interest(principal, rate, time):
    """Calculate continuous compound interest: A = Pe^(rt)."""
    if principal <= 0 or rate < 0 or time < 0:
        raise ValueError("Invalid parameters")

    rate_decimal = rate / 100
    amount = principal * exp(rate_decimal * time)
    return amount


def present_value(future_value, rate, time):
    """Calculate present value: PV = FV / (1 + r)^t."""
    if future_value <= 0 or rate < 0 or time < 0:
        raise ValueError("Invalid parameters")

    rate_decimal = rate / 100
    return future_value / power(1 + rate_decimal, time)


def inflation_adjustment(amount, inflation_rate, years):
    """Adjust amount for inflation: adjusted = amount / (1 + inflation)^years."""
    if amount <= 0 or inflation_rate < 0 or years < 0:
        raise ValueError("Invalid parameters")

    inflation_decimal = inflation_rate / 100
    return amount / power(1 + inflation_decimal, years)


def rule_of_72(rate):
    """Estimate doubling time using rule of 72: years ≈ 72/rate."""
    if rate <= 0:
        raise ValueError("Rate must be positive")

    return 72 / rate


# Examples
amount = compound_interest(1000, 5, 10)  # 5% for 10 years
print(f"Compound interest: ${amount:.2f}")

amount = continuous_compound_interest(1000, 5, 10)
print(f"Continuous compound: ${amount:.2f}")

pv = present_value(1000, 5, 10)  # Future value of $1000 in 10 years at 5%
print(f"Present value: ${pv:.2f}")

adjusted = inflation_adjustment(1000, 2, 10)  # $1000 in 10 years with 2% inflation
print(f"Inflation adjusted: ${adjusted:.2f}")

doubling = rule_of_72(6)  # 6% growth rate
print(f"Doubling time (rule of 72): {doubling:.1f} years")


# 🧩 Scientific and engineering applications
import math


def power(base, exponent):
    """Calculate base raised to exponent."""
    return base**exponent


def exp(x):
    """Calculate e^x (natural exponential)."""
    return math.exp(x)


def radioactive_decay(initial_amount, time, half_life):
    """Calculate radioactive decay: N = N₀ * (1/2)^(t/T)."""
    if initial_amount <= 0 or time < 0 or half_life <= 0:
        raise ValueError("Invalid parameters")

    return initial_amount * power(0.5, time / half_life)


def population_growth(initial_population, growth_rate, time):
    """Calculate population growth: P = P₀ * e^(rt)."""
    if initial_population <= 0 or time < 0:
        raise ValueError("Invalid parameters")

    return initial_population * exp(growth_rate * time)


def temperature_cooling(initial_temp, ambient_temp, time, cooling_constant):
    """Calculate Newton's law of cooling: T = Tₐ + (T₀ - Tₐ) * e^(-kt)."""
    if time < 0 or cooling_constant < 0:
        raise ValueError("Invalid parameters")

    return ambient_temp + (initial_temp - ambient_temp) * exp(-cooling_constant * time)


def capacitor_charging(voltage, resistance, capacitance, time):
    """Calculate capacitor charging: V = V₀ * (1 - e^(-t/RC))."""
    if voltage <= 0 or resistance <= 0 or capacitance <= 0 or time < 0:
        raise ValueError("Invalid parameters")

    tau = resistance * capacitance  # Time constant
    return voltage * (1 - exp(-time / tau))


def capacitor_discharging(initial_voltage, resistance, capacitance, time):
    """Calculate capacitor discharging: V = V₀ * e^(-t/RC)."""
    if initial_voltage <= 0 or resistance <= 0 or capacitance <= 0 or time < 0:
        raise ValueError("Invalid parameters")

    tau = resistance * capacitance  # Time constant
    return initial_voltage * exp(-time / tau)


# Examples
remaining = radioactive_decay(100, 10, 5)  # 10 years, 5-year half-life
print(f"Remaining radioactive material: {remaining:.1f}")

population = population_growth(1000, 0.02, 20)  # 2% growth for 20 years
print(f"Population: {population:.0f}")

temp = temperature_cooling(100, 20, 5, 0.1)  # Cooling from 100°C to 20°C
print(f"Temperature after 5 minutes: {temp:.1f}°C")

voltage = capacitor_charging(12, 1000, 0.001, 0.005)  # 12V, 1kΩ, 1mF, 5ms
print(f"Capacitor voltage: {voltage:.2f}V")
