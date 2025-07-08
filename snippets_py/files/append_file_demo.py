# 🧩 Append string to file
with open("file.txt", "a") as f:
    f.write("New line\n")


# 🧩 Append with newline
with open("file.txt", "a") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")


# 🧩 Append with timestamp
from datetime import datetime


def append_with_timestamp(filename, message):
    """Append message with timestamp to file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


append_with_timestamp("log.txt", "User logged in")


# 🧩 Append with rotation
import os
from datetime import datetime


def append_with_rotation(filename, content, max_size_mb=10):
    """Append content with file size rotation."""
    # Check if file exists and get its size
    if os.path.exists(filename):
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        if size_mb > max_size_mb:
            # Create backup with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{filename}.{timestamp}"
            os.rename(filename, backup_name)

    # Append content
    with open(filename, "a") as f:
        f.write(content + "\n")


append_with_rotation("app.log", "New log entry")
