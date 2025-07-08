# Round Number Operations

Zero-dependency Python snippets using only the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Round to decimal places

`math` `rounding` `decimal` `precision` `numbers`

Round number to specified decimal places

```python
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
```

!!! note "Notes"
    - Uses built-in round() function
    - Supports negative decimal places
    - Handles both integers and floats
    - Simple and efficient

<hr class="snippet-divider">

### Round with different strategies

`math` `rounding` `ceil` `floor` `trunc` `numbers`

Round with different strategies (up, down, towards zero)

```python
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
```

!!! note "Notes"
    - Uses math module functions
    - ceil() for rounding up
    - floor() for rounding down
    - trunc() for rounding towards zero
    - Useful for financial calculations

<hr class="snippet-divider">

### Round to significant figures

`math` `rounding` `significant-figures` `precision` `numbers`

Round number to specified significant figures

```python
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
```

!!! note "Notes"
    - Uses logarithmic calculation
    - Handles very small and large numbers
    - Preserves meaningful digits
    - Useful for scientific notation

<hr class="snippet-divider">

## Complex

###  Round with custom rounding function

`math` `rounding` `custom` `banker-rounding` `numbers`

Round number using custom rounding function

```python
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
```

!!! note "Notes"
    - Supports custom rounding strategies
    - Banker's rounding example
    - Flexible rounding function parameter
    - Useful for financial applications

<hr class="snippet-divider">

### Round currency amounts

`math` `rounding` `currency` `finance` `numbers`

Round currency amount to appropriate decimal places

```python
def round_currency(amount, currency="USD"):
    """Round currency amount to appropriate decimal places."""
    currency_decimals = {"USD": 2, "EUR": 2, "GBP": 2, "JPY": 0, "BTC": 8, "ETH": 8, "XRP": 6}
    places = currency_decimals.get(currency, 2)
    return round(amount, places)


# Examples
print(round_currency(123.4567, "USD"))  # 123.46
print(round_currency(123.4567, "JPY"))  # 123
print(round_currency(0.12345678, "BTC"))  # 0.12345678
```

!!! note "Notes"
    - Currency-specific decimal places
    - Supports major currencies
    - Cryptocurrency support
    - Financial calculations

<hr class="snippet-divider">

### Round with precision control

`math` `rounding` `decimal` `precision` `float-arithmetic` `numbers`

Round number with precise decimal arithmetic

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN


def round_decimal_precise(number, places=0, rounding_mode=ROUND_HALF_UP):
    """Round number with precise decimal arithmetic."""
    decimal_num = Decimal(str(number))
    return float(decimal_num.quantize(Decimal("0.1") ** places, rounding=rounding_mode))


# Examples
print(round_decimal_precise(2.675, 2))  # 2.68 (precise)
print(round_decimal_precise(2.675, 2, ROUND_HALF_DOWN))  # 2.67
print(round_decimal_precise(0.1 + 0.2, 1))  # 0.3 (handles float precision issues)
```

!!! note "Notes"
    - Uses Decimal for precision
    - Handles float arithmetic issues
    - Multiple rounding modes
    - Financial-grade precision

<hr class="snippet-divider">

### Round to nearest multiple

`math` `rounding` `multiple` `intervals` `numbers`

Round number to nearest multiple

```python
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
```

!!! note "Notes"
    - Useful for time intervals
    - Price rounding
    - Grid alignment
    - Custom intervals

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in rounding

`math` `rounding` `error-handling` `edge-case` `validation` `numbers`

Robust rounding with edge case handling

```python
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
```

!!! note "Notes"
    - Input validation
    - NaN and infinity handling
    - Type checking
    - Error messages

<hr class="snippet-divider">

### Performance comparison

`math` `rounding` `performance` `benchmarking` `optimization` `numbers`

Benchmark different rounding methods

```python
import time
from decimal import ROUND_HALF_UP


def round_decimal_precise(number, places=0, rounding_mode=ROUND_HALF_UP):
    # Function is defined in one of the above code block
    pass


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
```

!!! note "Notes"
    - Performance comparison
    - Built-in vs Decimal
    - Large dataset testing
    - Optimization insights

<hr class="snippet-divider">

## Practical Examples

###  Financial calculations

`math` `rounding` `finance` `interest` `compound` `numbers`

Calculate compound interest with proper rounding

```python
def round_currency(amount, currency="USD"):
    # Function is defined in one of the above code block
    pass


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
```

!!! note "Notes"
    - Financial calculations
    - Currency rounding
    - Compound interest
    - Real-world application

<hr class="snippet-divider">

### Scientific measurements

`math` `rounding` `scientific` `measurement` `uncertainty` `numbers`

Round measurement with uncertainty to appropriate precision

```python
def round_to_sig_figs(number, sig_figs):
    # Function is defined in one of the above code block
    pass


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
```

!!! note "Notes"
    - Scientific notation
    - Uncertainty propagation
    - Significant figures
    - Measurement precision

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Decimal Precision](decimal_precision.md)
- **Reference**: See [📂 Statistics Basic](statistics_basic.md)
- **Reference**: See [📂 Percentage](percentage.md)
- **Reference**: See [📂 Clamp Number](clamp_number.md)

## 🏷️ Tags

`math`, `rounding`, `decimal`, `precision`, `numbers`, `finance`, `scientific`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Rounding Functions Provide Precision Control
- Different Strategies Suit Different Applications
- Edge Case Handling Ensures Robustness
- Performance Considerations for Large Datasets
