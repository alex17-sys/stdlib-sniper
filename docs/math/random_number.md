---
title: Random Number Operations
description: Zero-dependency Python snippets for generating random numbers using the standard library.
keywords: benchmarking, boolean, cards, choice, color, constraints, dice, distribution, edge-case, error-handling, exponential, games, generation, lottery, math, modeling, monte-carlo, normal, numbers, optimization, password, performance, permutation, poisson, precision, random, reproducibility, seed, selection, shuffle, simulation, string, validation
---

# Random Number Operations

Zero-dependency Python snippets for generating random numbers using the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Generate random number

`math` `random` `generation` `numbers`

Generate random number between min_val and max_val

```python
import random


def random_number(min_val=0, max_val=1):
    """Generate random number between min_val and max_val."""
    return random.uniform(min_val, max_val)


def random_integer(min_val=0, max_val=100):
    """Generate random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)


# Basic random number generation
print(random_number())  # Random float between 0 and 1
print(random_number(10, 20))  # Random float between 10 and 20
print(random_integer(1, 6))  # Random integer between 1 and 6 (dice)
print(random_integer(-10, 10))  # Random integer between -10 and 10
```

!!! note "Notes"
    - Uses random module
    - Configurable range
    - Float and integer options
    - Simple and effective

<hr class="snippet-divider">

### Generate random choice

`math` `random` `choice` `selection` `numbers`

Choose random item from list or sequence

```python
import random



def random_choice(items):
    """Choose random item from list or sequence."""
    if not items:
        raise ValueError("Cannot choose from empty sequence")
    return random.choice(items)


def random_choices(items, k=1, weights=None):
    """Choose k random items with replacement."""
    if not items:
        raise ValueError("Cannot choose from empty sequence")
    return random.choices(items, k=k, weights=weights)


def random_sample(items, k):
    """Choose k random items without replacement."""
    if k > len(items):
        raise ValueError("Sample size cannot exceed population size")
    return random.sample(items, k)


# Examples
fruits = ["apple", "banana", "orange", "grape"]
print(random_choice(fruits))  # Random fruit
print(random_choices(fruits, k=3))  # 3 random fruits (with replacement)
print(random_sample(fruits, k=2))  # 2 random fruits (without replacement)

# Weighted choice
weights = [0.1, 0.3, 0.4, 0.2]  # Probabilities for each fruit
print(random_choices(fruits, k=1, weights=weights)[0])  # Weighted random choice
```

!!! note "Notes"
    - Multiple selection methods
    - With/without replacement
    - Weighted selection
    - Error handling

<hr class="snippet-divider">

### Shuffle list randomly

`math` `random` `shuffle` `permutation` `numbers`

Shuffle list randomly

```python
import random



def shuffle_list(items):
    """Shuffle list in place."""
    random.shuffle(items)
    return items


def shuffled_copy(items):
    """Return shuffled copy of list."""
    items_copy = items.copy()
    random.shuffle(items_copy)
    return items_copy


def partial_shuffle(items, ratio=0.5):
    """Partially shuffle list by swapping random pairs."""
    items_copy = items.copy()
    n = len(items_copy)
    swaps = int(n * ratio)

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        items_copy[i], items_copy[j] = items_copy[j], items_copy[i]

    return items_copy


# Examples
cards = list(range(1, 11))  # Cards 1-10
print(f"Original: {cards}")
print(f"Shuffled: {shuffle_list(cards.copy())}")
print(f"Partial shuffle: {partial_shuffle(cards, 0.3)}")
```

!!! note "Notes"
    - In-place shuffling
    - Copy preservation
    - Partial shuffling
    - Fisher-Yates algorithm

<hr class="snippet-divider">

## Complex

###  Generate random with specific distributions

`math` `random` `distribution` `normal` `exponential` `poisson` `numbers`

Generate random numbers from specific distributions

```python
import math
import random


def random_normal(mean=0, std_dev=1):
    """Generate random number from normal distribution using Box-Muller transform."""
    u1 = random.random()
    u2 = random.random()

    # Box-Muller transform
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mean + std_dev * z0


def random_exponential(rate=1):
    """Generate random number from exponential distribution."""
    u = random.random()
    return -math.log(1 - u) / rate


def random_poisson(lambda_val):
    """Generate random number from Poisson distribution."""
    L = math.exp(-lambda_val)
    k = 0
    p = 1

    while p > L:
        k += 1
        p *= random.random()

    return k - 1


def random_binomial(n, p):
    """Generate random number from binomial distribution."""
    successes = 0
    for _ in range(n):
        if random.random() < p:
            successes += 1
    return successes


# Examples
print(f"Normal(0,1): {random_normal():.3f}")
print(f"Exponential(2): {random_exponential(2):.3f}")
print(f"Poisson(5): {random_poisson(5)}")
print(f"Binomial(10,0.3): {random_binomial(10, 0.3)}")
```

!!! note "Notes"
    - Statistical distributions
    - Box-Muller transform
    - Monte Carlo methods
    - Simulation applications

<hr class="snippet-divider">

### Generate random with custom seed

`math` `random` `seed` `reproducibility` `numbers`

Generate random numbers with specific seed

```python
import random


def random_number(min_val=0, max_val=1):
    # See above defined function
    pass

def set_random_seed(seed):
    """Set random seed for reproducible results."""
    random.seed(seed)


def random_with_seed(seed, min_val=0, max_val=1):
    """Generate random number with specific seed."""
    random.seed(seed)
    return random.uniform(min_val, max_val)


def random_sequence(seed, count=10, min_val=0, max_val=1):
    """Generate sequence of random numbers with specific seed."""
    random.seed(seed)
    return [random.uniform(min_val, max_val) for _ in range(count)]


def reset_random_state():
    """Reset random state to use system time."""
    random.seed()


# Examples
set_random_seed(42)
print(f"Seeded random: {random_number()}")  # Same result every time

sequence1 = random_sequence(123, 5)
sequence2 = random_sequence(123, 5)
print(f"Same seed sequences: {sequence1 == sequence2}")  # True

reset_random_state()
print(f"System random: {random_number()}")  # Different each time
```

!!! note "Notes"
    - Reproducible results
    - Testing applications
    - Debugging support
    - State management

<hr class="snippet-divider">

### Generate random with constraints

`math` `random` `constraints` `precision` `boolean` `numbers`

Generate random numbers with specific constraints

```python
import random



def random_with_constraints(min_val, max_val, exclude_values=None):
    """Generate random number excluding specific values."""
    if exclude_values is None:
        exclude_values = []

    while True:
        value = random.uniform(min_val, max_val)
        if value not in exclude_values:
            return value


def random_with_precision(min_val, max_val, precision=2):
    """Generate random number with specific decimal precision."""
    value = random.uniform(min_val, max_val)
    return round(value, precision)


def random_in_range_with_step(min_val, max_val, step=1):
    """Generate random number in range with specific step size."""
    steps = int((max_val - min_val) / step) + 1
    step_index = random.randint(0, steps - 1)
    return min_val + step_index * step


def random_boolean(probability=0.5):
    """Generate random boolean with specified probability of True."""
    return random.random() < probability


# Examples
print(random_with_constraints(1, 10, [5, 7]))  # Random number excluding 5 and 7
print(random_with_precision(0, 1, 3))  # Random with 3 decimal places
print(random_in_range_with_step(0, 10, 0.5))  # Random in 0, 0.5, 1.0, ..., 10.0
print(random_boolean(0.7))  # 70% chance of True
```

!!! note "Notes"
    - Value exclusion
    - Precision control
    - Step-based generation
    - Probability control

<hr class="snippet-divider">

### Generate random sequences and patterns

`math` `random` `string` `password` `color` `generation` `numbers`

Generate random sequences and patterns

```python
import random


def random_string(length=10, charset=None):
    """Generate random string of specified length."""
    if charset is None:
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    return "".join(random.choice(charset) for _ in range(length))


def random_password(length=12, include_symbols=True):
    """Generate random password with specified requirements."""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if include_symbols else ""

    # Ensure at least one character from each category
    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits)]

    if include_symbols:
        password.append(random.choice(symbols))

    # Fill remaining length
    all_chars = lowercase + uppercase + digits + symbols
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Shuffle the password
    random.shuffle(password)
    return "".join(password)


def random_color_rgb():
    """Generate random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_color_hex():
    """Generate random hex color."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"


# Examples
print(random_string(8))  # Random 8-character string
print(random_password(16))  # Random 16-character password
print(random_color_rgb())  # Random RGB color
print(random_color_hex())  # Random hex color
```

!!! note "Notes"
    - String generation
    - Password creation
    - Color generation
    - Pattern creation

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in random generation

`math` `random` `error-handling` `edge-case` `validation` `numbers`

Robust random generation with edge case handling

```python
import random
import math


def robust_random_number(min_val=0, max_val=1):
    """Robust random number generation with edge case handling."""
    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
        raise TypeError("Bounds must be numeric")

    if math.isnan(min_val) or math.isnan(max_val) or math.isinf(min_val) or math.isinf(max_val):
        raise ValueError("Bounds must be finite")

    if min_val > max_val:
        min_val, max_val = max_val, min_val

    if min_val == max_val:
        return min_val

    return random.uniform(min_val, max_val)


def robust_random_choice(items):
    """Robust random choice with edge case handling."""
    if not items:
        raise ValueError("Cannot choose from empty sequence")

    if len(items) == 1:
        return items[0]

    return random.choice(items)


def safe_random_seed(seed):
    """Set random seed with validation."""
    if not isinstance(seed, (int, str, bytes, bytearray)):
        raise TypeError("Seed must be int, str, bytes, or bytearray")

    random.seed(seed)


# Test edge cases
try:
    print(robust_random_number(5, 5))  # 5.0 (same bounds)
    print(robust_random_number(10, 5))  # Random between 5 and 10 (swapped)
    print(robust_random_choice([42]))  # 42 (single item)
    safe_random_seed("test_seed")  # String seed
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Input validation
    - Bounds checking
    - Type checking
    - Error messages

<hr class="snippet-divider">

### Performance optimization

`math` `random` `performance` `benchmarking` `optimization` `numbers`

Benchmark different random generation methods

```python
import time
import random


def benchmark_random_methods():
    """Benchmark different random generation methods."""
    count = 100000

    # Method 1: Basic random
    start = time.time()
    _ = [random.random() for _ in range(count)]
    time1 = time.time() - start

    # Method 2: Random with range
    start = time.time()
    _ = [random.uniform(0, 100) for _ in range(count)]
    time2 = time.time() - start

    # Method 3: Random integers
    start = time.time()
    _ = [random.randint(0, 100) for _ in range(count)]
    time3 = time.time() - start

    print(f"Basic random: {time1:.6f}s")
    print(f"Uniform range: {time2:.6f}s")
    print(f"Integer range: {time3:.6f}s")
    print(f"Integer overhead: {time3 / time1:.2f}x")


# benchmark_random_methods()
```

!!! note "Notes"
    - Performance comparison
    - Method efficiency
    - Large dataset testing
    - Optimization insights

<hr class="snippet-divider">

## Practical Examples

###  Simulation and modeling

`math` `random` `simulation` `monte-carlo` `modeling` `numbers`

Use random numbers in simulations and modeling

```python
import random

def monte_carlo_pi(iterations=10000):
    """Estimate π using Monte Carlo method."""
    inside_circle = 0

    for _ in range(iterations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside_circle += 1

    return 4 * inside_circle / iterations


def random_walk(steps=100, step_size=1):
    """Generate 1D random walk."""
    position = 0
    positions = [position]

    for _ in range(steps):
        step = random.choice([-step_size, step_size])
        position += step
        positions.append(position)

    return positions


def coin_flip_simulation(flips=1000):
    """Simulate coin flips and analyze results."""
    results = [random.choice(["H", "T"]) for _ in range(flips)]

    heads = results.count("H")
    tails = results.count("T")

    return {
        "heads": heads,
        "tails": tails,
        "heads_ratio": heads / flips,
        "tails_ratio": tails / flips,
        "results": results,
    }


# Examples
pi_estimate = monte_carlo_pi(10000)
print(f"π estimate: {pi_estimate:.6f}")

walk = random_walk(50)
print(f"Final position: {walk[-1]}")

coin_results = coin_flip_simulation(1000)
print(f"Heads: {coin_results['heads']}, Tails: {coin_results['tails']}")
print(f"Heads ratio: {coin_results['heads_ratio']:.3f}")
```

!!! note "Notes"
    - Monte Carlo methods
    - Random walk simulation
    - Probability simulation
    - Statistical analysis

<hr class="snippet-divider">

### Game and entertainment

`math` `random` `games` `dice` `cards` `lottery` `numbers`

Use random numbers in games and entertainment

```python
import random

def roll_dice(sides=6, count=1):
    """Roll dice with specified number of sides."""
    if count == 1:
        return random.randint(1, sides)
    return [random.randint(1, sides) for _ in range(count)]


def draw_cards(deck_size=52, count=5):
    """Draw random cards from deck."""
    deck = list(range(1, deck_size + 1))
    return random.sample(deck, count)


def random_lottery_numbers(max_number=49, count=6):
    """Generate random lottery numbers."""
    return sorted(random.sample(range(1, max_number + 1), count))


def random_name_generator():
    """Generate random name from components."""
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]

    return f"{random.choice(first_names)} {random.choice(last_names)}"


# Examples
print(f"Dice roll: {roll_dice(6, 2)}")  # Roll 2 six-sided dice
print(f"Poker hand: {draw_cards(52, 5)}")  # Draw 5 cards
print(f"Lottery numbers: {random_lottery_numbers()}")  # 6 lottery numbers
print(f"Random name: {random_name_generator()}")  # Random full name
```

!!! note "Notes"
    - Dice rolling
    - Card games
    - Lottery simulation
    - Name generation

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Percentage](percentage.md)
- **Reference**: See [📂 Clamp Number](clamp_number.md)
- **Reference**: See [📂 Statistics Basic](statistics_basic.md)

## 🏷️ Tags

`math`, `random`, `generation`, `simulation`, `games`, `optimization`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Random Number Functions Support Simulation and Gaming Applications
- Multiple Generation Methods Offer Flexibility
- Edge Case Handling Ensures Robustness
- Real-World Applications in Modeling and Entertainment
