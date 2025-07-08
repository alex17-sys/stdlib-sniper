# 🧩 Reverse string with slicing
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)


# 🧩 Reverse string with reversed()
text = "Hello, World!"
reversed_text = "".join(reversed(text))
print(reversed_text)


# 🧩 Reverse string with word preservation
def reverse_string_preserve_words(text):
    """Reverse string while preserving word order."""
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


text = "Hello World Python"
result = reverse_string_preserve_words(text)
print(result)  # "olleH dlroW nohtyP"


# 🧩 Reverse string with custom characters
def reverse_string_custom(text, reverse_chars=None):
    """Reverse string with option to reverse only specific characters."""
    if reverse_chars is None:
        return text[::-1]

    result = []
    for char in text:
        if char in reverse_chars:
            result.append(char)
        else:
            result.append(char)

    return "".join(result[::-1])


# Reverse only letters, keep punctuation in place
text = "Hello, World! How are you?"
result = reverse_string_custom(text, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(result)  # "uoy era woH !dlroW ,olleH"
