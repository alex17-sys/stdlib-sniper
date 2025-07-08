# Read File Lines

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Read file as list of lines

`file` `read` `lines` `list`

Read all lines from file into a list

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)
```

!!! note "Notes"
    - Each line includes the newline character
    - Returns empty list if file is empty
    - Loads entire file into memory

<hr class="snippet-divider">

### Read lines without newlines

`file` `read` `lines` `splitlines`

Read lines and remove newline characters

```python
with open("file.txt", "r") as f:
    lines = f.read().splitlines()
print(lines)
```

!!! note "Notes"
    - Removes trailing newlines from each line
    - Alternative to readlines() + strip()
    - More memory efficient than readlines()

<hr class="snippet-divider">

## Complex

###  Read lines with line numbers

`file` `read` `lines` `enumerate` `generator`

Read file with line numbers for debugging or processing

```python
def read_lines_with_numbers(filename):
    """Read file lines with line numbers."""
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, 1):
            yield line_num, line.rstrip()


# Print lines with numbers
for num, line in read_lines_with_numbers("file.txt"):
    print(f"{num:3d}: {line}")
```

!!! note "Notes"
    - Uses enumerate to get line numbers
    - Starts numbering from 1 (not 0)
    - Strips trailing whitespace
    - Memory efficient for large files

<hr class="snippet-divider">

### Read lines with filtering

`file` `read` `lines` `filter` `generator`

Read lines with custom filtering function

```python
def read_lines_filtered(filename, filter_func=None):
    """Read and filter lines from file."""
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            if filter_func is None or filter_func(line):
                yield line


# Read only non-empty lines
non_empty = list(read_lines_filtered("file.txt", lambda x: x.strip()))

# Read only lines starting with '#'
comments = list(read_lines_filtered("file.txt", lambda x: x.startswith("#")))
```

!!! note "Notes"
    - Flexible filtering with custom functions
    - Memory efficient for large files
    - Can filter by any condition
    - Useful for processing log files or config files

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Write Lines](./write_lines.md)
- **Reference**: See [📂 Read File](./read_file.md)

## 🏷️ Tags

`file`, `read`, `lines`, `text`, `io`

## 📝 Notes

- Use readlines() to read all lines from a file
- Returns a list of strings (one per line)
- Useful for processing line-based data
