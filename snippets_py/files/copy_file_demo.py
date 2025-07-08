# 🧩 Copy file with shutil
import shutil

shutil.copy("source.txt", "destination.txt")


# 🧩 Copy file with metadata
import shutil

shutil.copy2("source.txt", "destination.txt")


# 🧩 Copy file with progress
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


# 🧩 Copy file with verification
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
