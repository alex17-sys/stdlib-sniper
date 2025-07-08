# 🧩 Basic anagram check
def is_anagram(text1, text2):
    """Check if two strings are anagrams."""
    return sorted(text1.lower()) == sorted(text2.lower())


text1 = "listen"
text2 = "silent"
result = is_anagram(text1, text2)
print(result)  # True


# 🧩 Anagram check with character counting
from collections import Counter


def is_anagram_counter(text1, text2):
    """Check if two strings are anagrams using character counting."""
    return Counter(text1.lower()) == Counter(text2.lower())


text1 = "listen"
text2 = "silent"
result = is_anagram_counter(text1, text2)
print(result)  # True


# 🧩 Anagram check with punctuation removal
import re
from collections import Counter


def is_anagram_clean(text1, text2):
    """Check if two strings are anagrams after removing punctuation and spaces."""
    # Remove punctuation and spaces, convert to lowercase
    clean1 = re.sub(r"[^a-zA-Z0-9]", "", text1.lower())
    clean2 = re.sub(r"[^a-zA-Z0-9]", "", text2.lower())

    return Counter(clean1) == Counter(clean2)


text1 = "A gentleman"
text2 = "Elegant man"
result = is_anagram_clean(text1, text2)
print(result)  # True


# 🧩 Anagram check with custom character filtering
from collections import Counter


def is_anagram_custom_filter(text1, text2, filter_chars=""):
    """Check if two strings are anagrams with custom character filtering."""
    # Remove specified characters and convert to lowercase
    clean1 = "".join(c.lower() for c in text1 if c not in filter_chars)
    clean2 = "".join(c.lower() for c in text2 if c not in filter_chars)

    return Counter(clean1) == Counter(clean2)


text1 = "Madam, I'm Adam"
text2 = "Adam, I'm Madam"
result = is_anagram_custom_filter(text1, text2, " ,'")
print(result)  # True


# 🧩 Anagram check with word boundaries
from collections import Counter


def is_anagram_words(text1, text2):
    """Check if two strings are anagrams at word level."""
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    return Counter(words1) == Counter(words2)


text1 = "fall leaves after leaves fall"
text2 = "leaves fall after fall leaves"
result = is_anagram_words(text1, text2)
print(result)  # True


# 🧩 Anagram check with character frequency analysis
from collections import Counter


def is_anagram_frequency_analysis(text1, text2):
    """Check if two strings are anagrams with detailed frequency analysis."""
    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    count1 = Counter(clean1)
    count2 = Counter(clean2)

    # Check if character frequencies match
    if count1 != count2:
        return False, count1, count2

    return True, count1, count2


text1 = "listen"
text2 = "silent"
result, freq1, freq2 = is_anagram_frequency_analysis(text1, text2)
print(result)  # True
print(freq1)  # Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})


# 🧩 Anagram check with minimum length requirement
from collections import Counter


def is_anagram_min_length(text1, text2, min_length=1):
    """Check if two strings are anagrams with minimum length requirement."""
    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    if len(clean1) < min_length or len(clean2) < min_length:
        return False

    return Counter(clean1) == Counter(clean2)


text1 = "a"
text2 = "a"
result = is_anagram_min_length(text1, text2, 3)
print(result)  # False

text3 = "listen"
text4 = "silent"
result2 = is_anagram_min_length(text3, text4, 3)
print(result2)  # True


# 🧩 Anagram check with performance optimization
from collections import Counter


def is_anagram_optimized(text1, text2):
    """Optimized anagram check for large strings."""
    # Early length check
    if len(text1) != len(text2):
        return False

    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    # Early length check after cleaning
    if len(clean1) != len(clean2):
        return False

    return Counter(clean1) == Counter(clean2)


text1 = "supercalifragilisticexpialidocious"
text2 = "supercalifragilisticexpialidocious"
result = is_anagram_optimized(text1, text2)
print(result)  # True


# 🧩 Anagram check with Unicode support
from collections import Counter
import unicodedata


def is_anagram_unicode(text1, text2):
    """Check if two strings are anagrams with proper Unicode handling."""
    # Normalize Unicode characters
    norm1 = unicodedata.normalize("NFD", text1)
    norm2 = unicodedata.normalize("NFD", text2)

    # Remove combining characters and convert to lowercase
    clean1 = "".join(c.lower() for c in norm1 if not unicodedata.combining(c) and c.isalnum())
    clean2 = "".join(c.lower() for c in norm2 if not unicodedata.combining(c) and c.isalnum())

    return Counter(clean1) == Counter(clean2)


text1 = "café"
text2 = "face"
result = is_anagram_unicode(text1, text2)
print(result)  # False (but handles Unicode properly)


# 🧩 Anagram check with custom comparison
from collections import Counter


def is_anagram_custom_compare(text1, text2, compare_func=None):
    """Check if two strings are anagrams with custom comparison function."""
    if compare_func is None:

        def compare_func(x, y):
            return x == y

    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    count1 = Counter(clean1)
    count2 = Counter(clean2)

    # Use custom comparison
    return compare_func(count1, count2)


# Case-sensitive comparison
def case_sensitive_compare(count1, count2):
    return count1 == count2


text1 = "Listen"
text2 = "silent"
result = is_anagram_custom_compare(text1, text2, case_sensitive_compare)
print(result)  # False (case-sensitive)


# 🧩 Anagram check with multiple strings
from collections import Counter


def are_all_anagrams(*texts):
    """Check if all provided strings are anagrams of each other."""
    if len(texts) < 2:
        return True

    # Clean and count characters for first text
    clean1 = "".join(c.lower() for c in texts[0] if c.isalnum())
    count1 = Counter(clean1)

    # Compare with all other texts
    for text in texts[1:]:
        clean = "".join(c.lower() for c in text if c.isalnum())
        if Counter(clean) != count1:
            return False

    return True


texts = ["listen", "silent", "enlist", "tinsel"]
result = are_all_anagrams(*texts)
print(result)  # True
