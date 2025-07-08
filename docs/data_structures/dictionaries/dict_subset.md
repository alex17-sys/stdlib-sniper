# Dictionary Subset Operations

Zero-dependency Python snippets using only the standard library.

13 snippets available in this sub-category.

---

## Simple

###  Create subset by keys

`dictionary` `subset` `keys` `filter` `data-structures`

Create subset with specified keys

```python
def subset_by_keys(d, keys):
    """Create subset with specified keys."""
    return {k: d[k] for k in keys if k in d}


person = {"name": "Alice", "age": 30, "city": "New York", "occupation": "Engineer", "salary": 75000}

result = subset_by_keys(person, ["name", "age", "city"])
print(result)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

!!! note "Notes"
    - Uses dict comprehension
    - Filters existing keys only
    - Preserves order
    - Simple and efficient

<hr class="snippet-divider">

### Create safe subset with defaults

`dictionary` `subset` `safe` `default` `data-structures`

Create subset with safe key access

```python
def safe_subset(d, keys, default=None):
    """Create subset with safe key access and defaults."""
    return {k: d.get(k, default) for k in keys}


person = {"name": "Alice", "age": 30, "city": "New York"}

result = safe_subset(person, ["name", "age", "nonexistent"], "N/A")
print(result)  # {'name': 'Alice', 'age': 30, 'nonexistent': 'N/A'}
```

!!! note "Notes"
    - Uses get() method
    - Handles missing keys
    - Configurable default value
    - No KeyError exceptions

<hr class="snippet-divider">

### Filter by value type

`dictionary` `subset` `type` `filter` `data-structures`

Create subset with values of specific type

```python
def subset_by_type(d, value_type):
    """Create subset with values of specific type."""
    return {k: v for k, v in d.items() if isinstance(v, value_type)}


mixed_data = {
    "name": "John",
    "age": 25,
    "height": 175.5,
    "is_student": True,
    "grades": [85, 90, 88],
}

string_data = subset_by_type(mixed_data, str)
print(string_data)  # {'name': 'John'}

numeric_data = subset_by_type(mixed_data, (int, float))
print(numeric_data)  # {'age': 25, 'height': 175.5}
```

!!! note "Notes"
    - Type-based filtering
    - Supports multiple types
    - Uses isinstance()
    - Flexible criteria

<hr class="snippet-divider">

## Complex

###  Filter by value conditions

`dictionary` `subset` `condition` `filter` `lambda` `data-structures`

Create subset based on value conditions

```python
def subset_by_condition(d, condition_func):
    """Create subset based on value conditions."""
    return {k: v for k, v in d.items() if condition_func(v)}


person = {"name": "Alice", "age": 30, "salary": 75000, "city": "New York", "experience": 5}

# High salary filter
high_salary = subset_by_condition(person, lambda v: isinstance(v, int) and v > 50000)
print(high_salary)  # {'age': 30, 'salary': 75000}

# String values only
strings_only = subset_by_condition(person, lambda v: isinstance(v, str))
print(strings_only)  # {'name': 'Alice', 'city': 'New York'}
```

!!! note "Notes"
    - Function-based filtering
    - Flexible conditions
    - Lambda expressions
    - Complex criteria support

<hr class="snippet-divider">

### Filter by key patterns

`dictionary` `subset` `pattern` `key-filter` `data-structures`

Create subset based on key patterns

```python
def subset_by_key_pattern(d, pattern_func):
    """Create subset based on key patterns."""
    return {k: v for k, v in d.items() if pattern_func(k)}


config = {
    "app_name": "MyApp",
    "app_version": "1.0.0",
    "db_host": "localhost",
    "db_port": 5432,
    "api_key": "secret123",
    "api_url": "https://api.example.com",
}

# Keys starting with 'app_'
app_config = subset_by_key_pattern(config, lambda k: k.startswith("app_"))
print(app_config)  # {'app_name': 'MyApp', 'app_version': '1.0.0'}

# Keys containing 'api'
api_config = subset_by_key_pattern(config, lambda k: "api" in k)
print(api_config)  # {'api_key': 'secret123', 'api_url': 'https://api.example.com'}
```

!!! note "Notes"
    - Pattern-based filtering
    - String operations
    - Regular expressions possible
    - Flexible key matching

<hr class="snippet-divider">

### Nested dictionary subset

`dictionary` `subset` `nested` `deep-access` `data-structures`

Create subset using nested key paths

```python
def subset_nested(d, key_paths):
    """Create subset using nested key paths."""
    result = {}
    for path in key_paths:
        keys = path.split(".")
        value = d
        try:
            for key in keys:
                value = value[key]
            result[path] = value
        except (KeyError, TypeError):
            continue
    return result


nested_data = {
    "user": {
        "profile": {"name": "Alice", "age": 30},
        "settings": {"theme": "dark", "notifications": True},
    },
    "app": {"version": "1.0.0"},
}

paths = ["user.profile.name", "user.settings.theme", "app.version"]
result = subset_nested(nested_data, paths)
print(
    result
)  # {'user.profile.name': 'Alice', 'user.settings.theme': 'dark', 'app.version': '1.0.0'}
```

!!! note "Notes"
    - Dot notation paths
    - Deep key access
    - Error handling
    - Flexible depth

<hr class="snippet-divider">

### Subset by value range

`dictionary` `subset` `range` `numeric` `data-structures`

Create subset with values within range

```python
def subset_by_range(d, min_val=None, max_val=None):
    """Create subset with values within specified range."""
    result = {}
    for k, v in d.items():
        if not isinstance(v, (int, float)):
            continue
        if min_val is not None and v < min_val:
            continue
        if max_val is not None and v > max_val:
            continue
        result[k] = v
    return result


scores = {"alice": 85, "bob": 92, "charlie": 78, "diana": 95, "eve": 88}

high_scores = subset_by_range(scores, min_val=90)
print(high_scores)  # {'bob': 92, 'diana': 95}

medium_scores = subset_by_range(scores, min_val=80, max_val=90)
print(medium_scores)  # {'alice': 85, 'eve': 88}
```

!!! note "Notes"
    - Numeric value filtering
    - Configurable bounds
    - Inclusive ranges
    - Type checking

<hr class="snippet-divider">

### Extract public data

`dictionary` `subset` `security` `public-data` `data-structures`

Extract only public/safe data fields

```python
def extract_public_data(data, public_keys):
    """Extract only public/safe data fields."""
    return {k: v for k, v in data.items() if k in public_keys}


user_data = {
    "user_id": 12345,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "secret123",
    "api_key": "key123",
}

public_keys = {"username", "first_name", "last_name"}
public_profile = extract_public_data(user_data, public_keys)
print(public_profile)  # {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe'}
```

!!! note "Notes"
    - Security-focused filtering
    - Whitelist approach
    - Data privacy
    - Safe data sharing

<hr class="snippet-divider">

### Filter sensitive data

`dictionary` `subset` `security` `blacklist` `data-structures`

Remove sensitive fields from data

```python
def filter_sensitive_data(data, sensitive_keys):
    """Remove sensitive fields from data."""
    return {k: v for k, v in data.items() if k not in sensitive_keys}


user_data = {
    "user_id": 12345,
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secret123",
    "api_key": "key123",
    "token": "token123",
}

sensitive_keys = {"password", "api_key", "token"}
safe_data = filter_sensitive_data(user_data, sensitive_keys)
print(safe_data)  # {'user_id': 12345, 'username': 'john_doe', 'email': 'john@example.com'}
```

!!! note "Notes"
    - Blacklist approach
    - Security filtering
    - Data sanitization
    - Safe logging

<hr class="snippet-divider">

## Edge Cases

###  Handle empty dictionaries

`dictionary` `subset` `error-handling` `edge-case` `data-structures`

Create subset with robust error handling

```python
def robust_subset(d, keys, default=None):
    """Create subset with robust error handling."""
    if not isinstance(d, dict):
        return {}
    if not keys:
        return {}
    return {k: d.get(k, default) for k in keys}


# Test with empty dictionary
empty_dict = {}
result = robust_subset(empty_dict, ["a", "b", "c"])
print(result)  # {}

# Test with None input
result2 = robust_subset(None, ["a", "b"])
print(result2)  # {}
```

!!! note "Notes"
    - Input validation
    - Type checking
    - Empty input handling
    - Safe defaults

<hr class="snippet-divider">

### Performance optimization

`dictionary` `subset` `performance` `optimization` `data-structures`

Efficient subset creation for large dictionaries

```python
def efficient_subset(d, keys):
    """Efficient subset creation for large dictionaries."""
    key_set = set(keys)  # O(1) lookup
    return {k: v for k, v in d.items() if k in key_set}


# Benchmark comparison
import time

large_dict = {f"key_{i}": f"value_{i}" for i in range(100000)}
keys_to_extract = [f"key_{i}" for i in range(0, 100000, 1000)]

# Method 1: List comprehension
start = time.time()
result1 = {k: large_dict[k] for k in keys_to_extract}
time1 = time.time() - start

# Method 2: Set-based lookup
start = time.time()
result2 = efficient_subset(large_dict, keys_to_extract)
time2 = time.time() - start

print(f"List method: {time1:.6f}s")
print(f"Set method: {time2:.6f}s")
print(f"Speedup: {time1 / time2:.2f}x")
```

!!! note "Notes"
    - Set-based lookup
    - O(1) key checking
    - Large dataset optimization
    - Benchmarking included

<hr class="snippet-divider">

## Practical Examples

###  Configuration management

`dictionary` `subset` `configuration` `environment` `data-structures`

Extract environment-specific configuration

```python
def extract_env_config(full_config, environment):
    """Extract environment-specific configuration."""
    env_prefix = f"{environment}_"
    return {
        k: v
        for k, v in full_config.items()
        if k.startswith(env_prefix) or k in ["app_name", "debug"]
    }


config = {
    "app_name": "MyApp",
    "debug": True,
    "dev_host": "localhost",
    "dev_port": 8000,
    "prod_host": "api.myapp.com",
    "prod_port": 443,
    "database_url": "postgresql://localhost/mydb",
}

dev_config = extract_env_config(config, "dev")
print(dev_config)  # {'app_name': 'MyApp', 'debug': True, 'dev_host': 'localhost', 'dev_port': 8000}
```

!!! note "Notes"
    - Environment-based filtering
    - Prefix matching
    - Configuration management
    - Deployment specific

<hr class="snippet-divider">

### Data analytics filtering

`dictionary` `subset` `analytics` `data-processing` `data-structures`

Extract data suitable for analytics

```python
def extract_analytics_data(user_data):
    """Extract data suitable for analytics."""
    return {
        k: v
        for k, v in user_data.items()
        if isinstance(v, (int, float))
        or "date" in k.lower()
        or "created" in k.lower()
        or "count" in k.lower()
    }


user_data = {
    "user_id": 12345,
    "username": "john_doe",
    "age": 30,
    "created_at": "2023-01-15",
    "last_login": "2024-01-20",
    "login_count": 150,
    "preferences": {"theme": "dark"},
}

analytics_data = extract_analytics_data(user_data)
print(
    analytics_data
)  # {'user_id': 12345, 'age': 30, 'created_at': '2023-01-15', 'last_login': '2024-01-20', 'login_count': 150}
```

!!! note "Notes"
    - Analytics-focused filtering
    - Pattern-based selection
    - Metric extraction
    - Data science ready

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Dict Comprehension](dict_comprehension.md)
- **Reference**: See [📂 Dict Merge](merge_dicts.md)
- **Reference**: See [📂 Dict Invert](invert_dict.md)
- **Reference**: See [📂 Dict Sort](sort_dict.md)
- **Reference**: See [📂 Dict Nested](nested_dict_access.md)



## 🏷️ Tags

`dictionary`, `subset`, `filtering`, `data-processing`, `python`, `dict-comprehension`, `key-filtering`, `value-filtering`, `nested-dictionaries`, `performance`, `best-practices`

## 📝 Notes

- Subset Functions Simplify Reusable Patterns
- Filtering by Keys, Values, or Patterns Offers Precision
- Support for Nested Access Increases Utility
