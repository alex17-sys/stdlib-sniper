# Copy File

Zero-dependency Python snippets for copying files using the standard library.

## Simple

### 🧩 Copy file with shutil

```python
import shutil

shutil.copy("source.txt", "destination.txt")
```

📂 Copy a file to a new location

🏷️ Tags: file, copy, shutil
📝 Notes:
- Copies file content and permissions
- Overwrites destination if it exists
- Preserves file metadata

### 🧩 Copy file with metadata

```python
import shutil

shutil.copy2("source.txt", "destination.txt")
```

📂 Copy file with all metadata (timestamps, permissions)

🏷️ Tags: file, copy, metadata, shutil
📝 Notes:
- Preserves timestamps and permissions
- More complete than copy()
- Useful for backup operations

## Complex

### 🧩 Copy file with progress

```python
import os


def copy_file_with_progress(src, dst, buffer_size=8192):
    """Copy file with progress indication."""
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    file_size = os.path.getsize(src)
    copied = 0

    try:
        with open(src, "rb") as fsrc:
            with open(dst, "wb") as fdst:
                while True:
                    buf = fsrc.read(buffer_size)
                    if not buf:
                        break
                    fdst.write(buf)
                    copied += len(buf)
                    progress = (copied / file_size) * 100
                    print(f"\rProgress: {progress:.1f}%", end="", flush=True)

        print(f"\nFile copied successfully: {src} -> {dst}")
        return True
    except Exception as e:
        print(f"\nError copying file: {e}")
        return False


copy_file_with_progress("large_file.txt", "backup.txt")
```

📂 Copy large files with progress indication

🏷️ Tags: file, copy, progress, buffer, large-files
📝 Notes:
- Shows copy progress as percentage
- Uses buffer for memory efficiency
- Handles large files gracefully
- Provides detailed error messages

### 🧩 Copy file with verification

```python
import os
import shutil
import hashlib


def copy_file_verified(src, dst):
    """Copy file and verify integrity with checksum."""
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    # Calculate source file checksum
    with open(src, "rb") as f:
        src_hash = hashlib.md5(f.read()).hexdigest()

    # Copy the file
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        print(f"Error copying file: {e}")
        return False

    # Verify destination file checksum
    with open(dst, "rb") as f:
        dst_hash = hashlib.md5(f.read()).hexdigest()

    if src_hash == dst_hash:
        print("File copied and verified successfully")
        print(f"MD5: {src_hash}")
        return True
    else:
        print("Copy verification failed!")
        return False


copy_file_verified("important.txt", "backup.txt")
```

📂 Copy file with MD5 checksum verification

🏷️ Tags: file, copy, verify, checksum, md5, integrity
📝 Notes:
- Verifies file integrity after copying
- Uses MD5 checksum for verification
- Ensures data integrity
- Useful for critical file operations

## 🔗 Cross-References

- **Reference**: See [📂 Move File](./move_file.md)
- **Reference**: See [📂 Delete File](./delete_file.md)

## 🏷️ Tags

`file`, `copy`, `shutil`, `os`, `io`

## 📝 Notes

- Use shutil.copy2() to copy files with metadata
- Useful for backups and file management
- Always check destination path for overwrites
