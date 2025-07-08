# 🧩 Basic trigonometric functions
import math


def sin(angle, degrees=False):
    """Calculate sine of angle."""
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def cos(angle, degrees=False):
    """Calculate cosine of angle."""
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)


def tan(angle, degrees=False):
    """Calculate tangent of angle."""
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)


# Basic trigonometric calculations
print(sin(30, degrees=True))  # 0.5
print(cos(60, degrees=True))  # 0.5
print(tan(45, degrees=True))  # 1.0
print(sin(math.pi / 6))  # 0.5 (30 degrees in radians)


# 🧩 Inverse trigonometric functions
import math


def asin(value):
    """Calculate arcsine (inverse sine) in radians."""
    return math.asin(value)


def acos(value):
    """Calculate arccosine (inverse cosine) in radians."""
    return math.acos(value)


def atan(value):
    """Calculate arctangent (inverse tangent) in radians."""
    return math.atan(value)


def atan2(y, x):
    """Calculate arctangent of y/x in radians."""
    return math.atan2(y, x)


def to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)


def to_radians(degrees):
    """Convert degrees to radians."""
    return math.radians(degrees)


# Examples
print(to_degrees(asin(0.5)))  # 30.0
print(to_degrees(acos(0.5)))  # 60.0
print(to_degrees(atan(1)))  # 45.0
print(to_degrees(atan2(1, 1)))  # 45.0


# 🧩 Trigonometric identities
import math


def pythagorean_identity(angle, degrees=False):
    """Verify sin²(θ) + cos²(θ) = 1."""
    if degrees:
        angle = math.radians(angle)
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)
    return sin_val**2 + cos_val**2


def double_angle_sin(angle, degrees=False):
    """Calculate sin(2θ) = 2sin(θ)cos(θ)."""
    if degrees:
        angle = math.radians(angle)
    return 2 * math.sin(angle) * math.cos(angle)


def double_angle_cos(angle, degrees=False):
    """Calculate cos(2θ) = cos²(θ) - sin²(θ)."""
    if degrees:
        angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    return cos_val**2 - sin_val**2


def half_angle_sin(angle, degrees=False):
    """Calculate sin(θ/2) = ±√((1-cos(θ))/2)."""
    if degrees:
        angle = math.radians(angle)
    return math.sqrt((1 - math.cos(angle)) / 2)


def half_angle_cos(angle, degrees=False):
    """Calculate cos(θ/2) = ±√((1+cos(θ))/2)."""
    if degrees:
        angle = math.radians(angle)
    return math.sqrt((1 + math.cos(angle)) / 2)


# Examples
angle = 30
print(f"Pythagorean identity: {pythagorean_identity(angle, degrees=True):.10f}")  # ~1.0
print(f"sin(2×{angle}°) = {double_angle_sin(angle, degrees=True):.3f}")
print(f"cos(2×{angle}°) = {double_angle_cos(angle, degrees=True):.3f}")


# 🧩 Trigonometric equations and solving
import math


def to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)


def solve_sin_equation(a, b, c):
    """Solve a*sin(x) + b*cos(x) = c."""
    if a == 0 and b == 0:
        if c == 0:
            return "All real numbers"
        else:
            return "No solution"

    # Convert to R*sin(x + α) form
    R = math.sqrt(a**2 + b**2)
    alpha = math.atan2(b, a)

    if abs(c) > R:
        return "No solution"

    # Solve R*sin(x + α) = c
    phi = math.asin(c / R)
    x1 = phi - alpha
    x2 = math.pi - phi - alpha

    return [x1, x2]


def solve_triangle_sides(a, b, C):
    """Solve triangle given two sides and included angle (SAS)."""
    if C <= 0 or C >= math.pi:
        raise ValueError("Angle must be between 0 and π")

    # Law of cosines: c² = a² + b² - 2ab*cos(C)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))

    # Law of sines to find other angles
    A = math.asin(a * math.sin(C) / c)
    B = math.pi - A - C

    return {"sides": {"a": a, "b": b, "c": c}, "angles": {"A": A, "B": B, "C": C}}


def solve_triangle_angles(A, B, c):
    """Solve triangle given two angles and included side (ASA)."""
    if A <= 0 or B <= 0 or A + B >= math.pi:
        raise ValueError("Invalid angles")

    C = math.pi - A - B

    # Law of sines
    a = c * math.sin(A) / math.sin(C)
    b = c * math.sin(B) / math.sin(C)

    return {"sides": {"a": a, "b": b, "c": c}, "angles": {"A": A, "B": B, "C": C}}


# Examples
solutions = solve_sin_equation(1, 1, 1)
print(f"Solutions to sin(x) + cos(x) = 1: {solutions}")

triangle = solve_triangle_sides(3, 4, math.pi / 3)  # 60 degrees
print(f"Triangle sides: {triangle['sides']}")
print(f"Triangle angles: {[to_degrees(angle) for angle in triangle['angles'].values()]}")


# 🧩 Trigonometric series and approximations
import math


def sin_series(x, terms=10):
    """Calculate sine using Taylor series: x - x³/3! + x⁵/5! - ..."""
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


def cos_series(x, terms=10):
    """Calculate cosine using Taylor series: 1 - x²/2! + x⁴/4! - ..."""
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result


def tan_series(x, terms=10):
    """Calculate tangent using series approximation."""
    if abs(x) >= math.pi / 2:
        raise ValueError("Series converges only for |x| < π/2")

    # Use tan(x) = sin(x)/cos(x) with series
    sin_val = sin_series(x, terms)
    cos_val = cos_series(x, terms)
    return sin_val / cos_val


def sinc_function(x):
    """Calculate sinc function: sin(x)/x."""
    if x == 0:
        return 1
    return math.sin(x) / x


# Examples
x = math.pi / 6  # 30 degrees
print(f"sin({x:.3f}) = {sin_series(x):.6f} (series)")
print(f"sin({x:.3f}) = {math.sin(x):.6f} (exact)")
print(f"cos({x:.3f}) = {cos_series(x):.6f} (series)")
print(f"sinc({x:.3f}) = {sinc_function(x):.6f}")


# 🧩 Trigonometric interpolation and smoothing
import math


def interpolate_sine(x, x_values, y_values):
    """Interpolate using sine function."""
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

    # Linear interpolation with sine weighting
    x1, x2 = x_values[idx1], x_values[idx2]
    y1, y2 = y_values[idx1], y_values[idx2]

    if x1 == x2:
        return y1

    # Use sine interpolation
    t = (x - x1) / (x2 - x1)
    weight = math.sin(t * math.pi / 2)
    return y1 + weight * (y2 - y1)


def smooth_sine_wave(frequency, amplitude, phase=0, samples=100):
    """Generate smooth sine wave."""
    wave = []
    for i in range(samples):
        t = i / samples * 2 * math.pi
        value = amplitude * math.sin(frequency * t + phase)
        wave.append(value)
    return wave


def fourier_series_coefficients(signal, num_terms=10):
    """Calculate Fourier series coefficients."""
    N = len(signal)
    coefficients = []

    for k in range(num_terms):
        real_part = 0
        imag_part = 0

        for n in range(N):
            angle = 2 * math.pi * k * n / N
            real_part += signal[n] * math.cos(angle)
            imag_part += signal[n] * math.sin(angle)

        real_part /= N
        imag_part /= N
        coefficients.append((real_part, imag_part))

    return coefficients


# Examples
x_points = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
y_points = [0, 0.707, 1, 0.707, 0]

interpolated = interpolate_sine(math.pi / 6, x_points, y_points)
print(f"Interpolated value at π/6: {interpolated:.3f}")

wave = smooth_sine_wave(2, 1, 0, 50)
print(f"Sine wave samples: {wave[:5]}...")


# 🧩 Handle edge cases in trigonometric calculations
import math


def robust_sin(angle, degrees=False):
    """Robust sine calculation with edge case handling."""
    if not isinstance(angle, (int, float)):
        raise TypeError("Angle must be numeric")

    if math.isnan(angle) or math.isinf(angle):
        raise ValueError("Angle must be finite")

    if degrees:
        angle = math.radians(angle)

    # Normalize angle to [-2π, 2π]
    angle = angle % (2 * math.pi)

    return math.sin(angle)


def robust_atan2(y, x):
    """Robust arctangent calculation with edge case handling."""
    if not isinstance(y, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("Coordinates must be numeric")

    if math.isnan(y) or math.isnan(x) or math.isinf(y) or math.isinf(x):
        raise ValueError("Coordinates must be finite")

    if x == 0 and y == 0:
        raise ValueError("Undefined at origin (0,0)")

    return math.atan2(y, x)


def safe_tan(angle, degrees=False):
    """Safe tangent calculation avoiding undefined values."""
    if degrees:
        angle = math.radians(angle)

    # Check for undefined values (π/2 + nπ)
    if abs(math.cos(angle)) < 1e-10:
        raise ValueError("Tangent is undefined at this angle")

    return math.tan(angle)


def normalize_angle(angle, degrees=False):
    """Normalize angle to [0, 2π) or [0°, 360°)."""
    if degrees:
        return angle % 360
    else:
        return angle % (2 * math.pi)


# Test edge cases
try:
    print(robust_sin(720, degrees=True))  # 0.0 (normalized)
    print(robust_atan2(1, 0))  # π/2
    print(safe_tan(90, degrees=True))  # ValueError
    print(normalize_angle(450, degrees=True))  # 90°
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Performance comparison
import time
import math


def sin_series(x, terms=10):
    # Function is defined in one of the above code block
    pass


def sin(angle, degrees=False):
    # Function is defined in one of the above code block
    pass


def benchmark_trig_methods():
    """Benchmark different trigonometric calculation methods."""
    angles = [0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, math.pi]
    iterations = 100000

    # Method 1: Direct math functions
    start = time.time()
    for _ in range(iterations):
        for angle in angles:
            _ = math.sin(angle)
    time1 = time.time() - start

    # Method 2: Series approximation
    start = time.time()
    for _ in range(iterations):
        for angle in angles:
            _ = sin_series(angle, 5)
    time2 = time.time() - start

    # Method 3: With degree conversion
    start = time.time()
    for _ in range(iterations):
        for angle in [0, 30, 45, 60, 90, 180]:
            _ = sin(angle, degrees=True)
    time3 = time.time() - start

    print(f"Direct math: {time1:.6f}s")
    print(f"Series (5 terms): {time2:.6f}s")
    print(f"With conversion: {time3:.6f}s")
    print(f"Series overhead: {time2 / time1:.2f}x")


# benchmark_trig_methods()


# 🧩 Geometry and physics applications
import math


def to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)


def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_angle_between_points(x1, y1, x2, y2):
    """Calculate angle between two points from origin."""
    return math.atan2(y2 - y1, x2 - x1)


def rotate_point(x, y, angle, degrees=False):
    """Rotate point around origin by given angle."""
    if degrees:
        angle = math.radians(angle)

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    new_x = x * cos_a - y * sin_a
    new_y = x * sin_a + y * cos_a

    return new_x, new_y


def projectile_motion(initial_velocity, angle, time, g=9.81):
    """Calculate projectile position at given time."""
    if angle <= 0 or angle >= 90:
        raise ValueError("Angle must be between 0 and 90 degrees")

    angle_rad = math.radians(angle)
    v0x = initial_velocity * math.cos(angle_rad)
    v0y = initial_velocity * math.sin(angle_rad)

    x = v0x * time
    y = v0y * time - 0.5 * g * time**2

    return x, y


def pendulum_period(length, g=9.81):
    """Calculate period of simple pendulum."""
    return 2 * math.pi * math.sqrt(length / g)


# Examples
distance = calculate_distance(0, 0, 3, 4)
print(f"Distance: {distance}")

angle = calculate_angle_between_points(0, 0, 1, 1)
print(f"Angle: {to_degrees(angle):.1f}°")

rotated = rotate_point(1, 0, 90, degrees=True)
print(f"Rotated point: {rotated}")

position = projectile_motion(50, 45, 2)
print(f"Projectile position: {position}")

period = pendulum_period(1.0)
print(f"Pendulum period: {period:.3f}s")


# 🧩 Signal processing and waves
import math


def to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)


def generate_sine_wave(frequency, amplitude, duration, sample_rate=44100):
    """Generate sine wave for audio processing."""
    samples = int(duration * sample_rate)
    wave = []

    for i in range(samples):
        t = i / sample_rate
        value = amplitude * math.sin(2 * math.pi * frequency * t)
        wave.append(value)

    return wave


def add_waves(wave1, wave2):
    """Add two waves together."""
    if len(wave1) != len(wave2):
        raise ValueError("Waves must have same length")

    return [a + b for a, b in zip(wave1, wave2)]


def calculate_rms(wave):
    """Calculate root mean square of wave."""
    if not wave:
        return 0

    sum_squares = sum(sample**2 for sample in wave)
    return math.sqrt(sum_squares / len(wave))


def calculate_phase_difference(wave1, wave2):
    """Calculate phase difference between two waves."""
    if len(wave1) != len(wave2):
        raise ValueError("Waves must have same length")

    # Cross-correlation to find phase difference
    max_correlation = 0
    best_shift = 0

    for shift in range(len(wave1)):
        correlation = sum(wave1[i] * wave2[(i + shift) % len(wave2)] for i in range(len(wave1)))
        if correlation > max_correlation:
            max_correlation = correlation
            best_shift = shift

    # Convert shift to phase difference
    phase_diff = 2 * math.pi * best_shift / len(wave1)
    return phase_diff


# Examples
wave1 = generate_sine_wave(440, 1.0, 0.1)  # A4 note
wave2 = generate_sine_wave(880, 0.5, 0.1)  # A5 note

combined = add_waves(wave1, wave2)
rms = calculate_rms(combined)
print(f"Combined wave RMS: {rms:.3f}")

phase_diff = calculate_phase_difference(wave1, wave2)
print(f"Phase difference: {to_degrees(phase_diff):.1f}°")
