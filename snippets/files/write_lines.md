# Write Lines

Zero-dependency Python snippets for writing lines to files using the standard library.

## Simple

### 🧩 Write list of lines to file

```python
lines = ["Line 1", "Line 2", "Line 3"]
with open("file.txt", "w") as f:
    f.writelines(lines)
```

📂 Write a list of strings to file without newlines

🏷️ Tags: file, write, lines, list, writelines
📝 Notes:
- Writes strings without adding newlines
- Overwrites existing file
- Each string becomes one line

### 🧩 Write lines with newlines

```python
lines = ["Line 1", "Line 2", "Line 3"]
with open("file.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
```

📂 Write lines to file with explicit newlines

🏷️ Tags: file, write, lines, newline, loop
📝 Notes:
- Adds newline after each line
- More explicit than writelines()
- Easy to customize line endings

## Complex

### 🧩 Write lines with numbering

```python
def write_lines_with_numbers(filename, lines, start_number=1):
    """Write lines to file with line numbers."""
    with open(filename, "w") as f:
        for i, line in enumerate(lines, start_number):
            f.write(f"{i:3d}: {line}\n")


lines = ["First line", "Second line", "Third line"]
write_lines_with_numbers("numbered.txt", lines)
```

📂 Write lines to file with automatic line numbering

🏷️ Tags: file, write, lines, enumerate
📝 Notes:
- Adds line numbers to each line
- Configurable starting number
- Right-aligned line numbers
- Useful for debugging and logs

### 🧩 Write lines with filtering

```python
def write_lines_filtered(filename, lines, filter_func=None):
    """Write lines to file with optional filtering."""
    with open(filename, "w") as f:
        for line in lines:
            if filter_func is None or filter_func(line):
                f.write(line + "\n")


lines = ["Line 1", "", "Line 3", "  ", "Line 5"]

# Write only non-empty lines
write_lines_filtered("filtered.txt", lines, lambda x: x.strip())

# Write only lines starting with 'Line'
write_lines_filtered("filtered2.txt", lines, lambda x: x.startswith("Line"))
```

📂 Write lines to file with custom filtering function

🏷️ Tags: file, write, lines, filter, lambda, custom
📝 Notes:
- Applies filter function to each line
- Skips lines that don't pass filter
- Flexible filtering criteria
- Useful for data cleaning

## 🔗 Cross-References

- **Reference**: See [📂 Write File](./write_file.md)
- **Reference**: See [📂 Read File Lines](./read_file_lines.md)

## 🏷️ Tags

`file`, `write`, `lines`, `text`, `io`

## 📝 Notes

- Use writelines() to write multiple lines to a file
- Add newlines manually if needed
- Useful for logs, reports, and batch output
