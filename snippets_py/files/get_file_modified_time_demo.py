# 🧩 Get file modification time
import os

mtime = os.path.getmtime("file.txt")
print(f"Modified: {mtime}")


# 🧩 Get file modification time safely
import os

try:
    mtime = os.path.getmtime("file.txt")
    print(f"Modified: {mtime}")
except FileNotFoundError:
    print("File does not exist")


# 🧩 Get file modification time as datetime
import os
from datetime import datetime


def get_file_modified_datetime(filename):
    """Get file modification time as datetime object."""
    if not os.path.exists(filename):
        return None

    mtime = os.path.getmtime(filename)
    return datetime.fromtimestamp(mtime)


mtime_dt = get_file_modified_datetime("file.txt")
if mtime_dt:
    print(f"Modified: {mtime_dt}")
    print(f"Date: {mtime_dt.strftime('%Y-%m-%d')}")
    print(f"Time: {mtime_dt.strftime('%H:%M:%S')}")


# 🧩 Get file age in human readable format
import os
from datetime import datetime


def get_file_age(filename):
    """Get file age in human readable format."""
    if not os.path.exists(filename):
        return "File does not exist"

    mtime = os.path.getmtime(filename)
    file_time = datetime.fromtimestamp(mtime)
    now = datetime.now()
    age = now - file_time

    # Convert to appropriate unit
    if age.days > 365:
        years = age.days // 365
        return f"{years} year{'s' if years != 1 else ''} ago"
    elif age.days > 30:
        months = age.days // 30
        return f"{months} month{'s' if months != 1 else ''} ago"
    elif age.days > 0:
        return f"{age.days} day{'s' if age.days != 1 else ''} ago"
    elif age.seconds > 3600:
        hours = age.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif age.seconds > 60:
        minutes = age.seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    else:
        return "Just now"


age = get_file_age("file.txt")
print(f"File age: {age}")
