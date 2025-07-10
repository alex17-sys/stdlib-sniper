# 🧩 Round to decimal places
def round_to_places(number, places=0):
    """Round number to specified decimal places."""
    return round(number, places)


# Basic rounding
print(round_to_places(3.14159, 2))  # 3.14
print(round_to_places(3.14159, 0))  # 3
print(round_to_places(3.14159, 4))  # 3.1416

# Negative places (round to tens, hundreds, etc.)
print(round_to_places(1234.5678, -2))  # 1200.0
print(round_to_places(1234.5678, -1))  # 1230.0


# 🧩 Round with different strategies
import math


def round_up(number, places=0):
    """Round number up to specified decimal places."""
    multiplier = 10**places
    return math.ceil(number * multiplier) / multiplier


def round_down(number, places=0):
    """Round number down to specified decimal places."""
    multiplier = 10**places
    return math.floor(number * multiplier) / multiplier


def round_towards_zero(number, places=0):
    """Round number towards zero to specified decimal places."""
    multiplier = 10**places
    return math.trunc(number * multiplier) / multiplier


# Examples
print(round_up(3.14159, 2))  # 3.15
print(round_down(3.14159, 2))  # 3.14
print(round_towards_zero(-3.7))  # -3.0


# 🧩 Round to significant figures
import math


def round_to_sig_figs(number, sig_figs):
    """Round number to specified significant figures."""
    if number == 0:
        return 0
    return round(number, sig_figs - 1 - int(math.floor(math.log10(abs(number)))))


# Examples
print(round_to_sig_figs(123.456, 3))  # 123.0
print(round_to_sig_figs(0.001234, 2))  # 0.0012
print(round_to_sig_figs(1234.56, 2))  # 1200.0
print(round_to_sig_figs(0.0001234, 3))  # 0.000123


# 🧩 Round with custom rounding function
def round_custom(number, places=0, rounding_func=round):
    """Round number using custom rounding function."""
    multiplier = 10**places
    return rounding_func(number * multiplier) / multiplier


# Banker's rounding (round to even)
def banker_round(number):
    """Banker's rounding: round to even when exactly halfway."""
    if number - int(number) == 0.5:
        return int(number) if int(number) % 2 == 0 else int(number) + 1
    return round(number)


# Examples
print(round_custom(2.5, 0, banker_round))  # 2 (rounds to even)
print(round_custom(3.5, 0, banker_round))  # 4 (rounds to even)
print(round_custom(2.6, 0, banker_round))  # 3 (normal rounding)


# 🧩 Round currency amounts
def round_currency(amount, currency="USD"):
    """Round currency amount to appropriate decimal places."""
    currency_decimals = {"USD": 2, "EUR": 2, "GBP": 2, "JPY": 0, "BTC": 8, "ETH": 8, "XRP": 6}
    places = currency_decimals.get(currency, 2)
    return round(amount, places)


# Examples
print(round_currency(123.4567, "USD"))  # 123.46
print(round_currency(123.4567, "JPY"))  # 123
print(round_currency(0.12345678, "BTC"))  # 0.12345678


# 🧩 Round with precision control
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN


def round_decimal_precise(number, places=0, rounding_mode=ROUND_HALF_UP):
    """Round number with precise decimal arithmetic."""
    decimal_num = Decimal(str(number))
    return float(decimal_num.quantize(Decimal("0.1") ** places, rounding=rounding_mode))


# Examples
print(round_decimal_precise(2.675, 2))  # 2.68 (precise)
print(round_decimal_precise(2.675, 2, ROUND_HALF_DOWN))  # 2.67
print(round_decimal_precise(0.1 + 0.2, 1))  # 0.3 (handles float precision issues)


# 🧩 Round to nearest multiple
import math


def round_to_multiple(number, multiple):
    """Round number to nearest multiple."""
    return round(number / multiple) * multiple


def round_up_to_multiple(number, multiple):
    """Round number up to nearest multiple."""
    return math.ceil(number / multiple) * multiple


def round_down_to_multiple(number, multiple):
    """Round number down to nearest multiple."""
    return math.floor(number / multiple) * multiple


# Examples
print(round_to_multiple(17, 5))  # 15
print(round_to_multiple(23, 5))  # 25
print(round_up_to_multiple(17, 5))  # 20
print(round_down_to_multiple(23, 5))  # 20


# 🧩 Handle edge cases in rounding
import math


def robust_round(number, places=0):
    """Robust rounding with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be int or float")

    if places < 0:
        raise ValueError("Decimal places must be non-negative")

    if math.isnan(number) or math.isinf(number):
        return number

    return round(number, places)


# Test edge cases
try:
    print(robust_round(float("inf")))  # inf
    print(robust_round(float("nan")))  # nan
    print(robust_round(0.0, 2))  # 0.0
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time
from decimal import ROUND_HALF_UP


# Function is defined in one of the above code block (round_decimal_precise)


def benchmark_rounding():
    """Benchmark different rounding methods."""
    numbers = [3.14159] * 1000000

    # Method 1: Built-in round
    start = time.time()
    _ = [round(n, 2) for n in numbers]
    time1 = time.time() - start

    # Method 2: Decimal rounding
    start = time.time()
    _ = [round_decimal_precise(n, 2) for n in numbers]
    time2 = time.time() - start

    print(f"Built-in round: {time1:.6f}s")
    print(f"Decimal round: {time2:.6f}s")
    print(f"Speedup: {time2 / time1:.2f}x")


# benchmark_rounding()


# 🧩 Financial calculations
# Function is defined in one of the above code block (round_currency)


def calculate_interest(principal, rate, time, compound_periods=12):
    """Calculate compound interest with proper rounding."""
    amount = principal * (1 + rate / compound_periods) ** (compound_periods * time)
    return round_currency(amount, "USD")


# Example
principal = 1000
rate = 0.05  # 5% annual rate
time = 2  # 2 years

interest = calculate_interest(principal, rate, time)
print(f"Final amount: ${interest}")  # $1104.94


# 🧩 Scientific measurements
# Function is defined in one of the above code block (round_to_sig_figs)


def round_measurement(value, uncertainty, sig_figs=2):
    """Round measurement with uncertainty to appropriate precision."""
    # Round uncertainty to 1-2 significant figures
    rounded_uncertainty = round_to_sig_figs(uncertainty, sig_figs)

    # Round value to same decimal places as uncertainty
    uncertainty_places = (
        len(str(rounded_uncertainty).split(".")[-1]) if "." in str(rounded_uncertainty) else 0
    )
    rounded_value = round(value, uncertainty_places)

    return rounded_value, rounded_uncertainty


# Example
value = 3.14159265359
uncertainty = 0.001234

rounded_val, rounded_unc = round_measurement(value, uncertainty)
print(f"{rounded_val} ± {rounded_unc}")  # 3.142 ± 0.001
