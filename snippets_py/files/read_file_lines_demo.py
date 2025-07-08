# 🧩 Read file as list of lines
with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)


# 🧩 Read lines without newlines
with open("file.txt", "r") as f:
    lines = f.read().splitlines()
print(lines)


# 🧩 Read lines with line numbers
def read_lines_with_numbers(filename):
    """Read file lines with line numbers."""
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, 1):
            yield line_num, line.rstrip()


# Print lines with numbers
for num, line in read_lines_with_numbers("file.txt"):
    print(f"{num:3d}: {line}")


# 🧩 Read lines with filtering
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
