# 🧩 Write list of lines to file
lines = ["Line 1", "Line 2", "Line 3"]
with open("file.txt", "w") as f:
    f.writelines(lines)


# 🧩 Write lines with newlines
lines = ["Line 1", "Line 2", "Line 3"]
with open("file.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")


# 🧩 Write lines with numbering
def write_lines_with_numbers(filename, lines, start_number=1):
    """Write lines to file with line numbers."""
    with open(filename, "w") as f:
        for i, line in enumerate(lines, start_number):
            f.write(f"{i:3d}: {line}\n")


lines = ["First line", "Second line", "Third line"]
write_lines_with_numbers("numbered.txt", lines)


# 🧩 Write lines with filtering
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
