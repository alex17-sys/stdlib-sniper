# 🧩 Calculate MD5 checksum
import hashlib

with open("file.txt", "rb") as f:
    data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
print(f"MD5: {md5_hash}")


# 🧩 Calculate SHA-256 checksum
import hashlib

with open("file.txt", "rb") as f:
    data = f.read()
    sha256_hash = hashlib.sha256(data).hexdigest()
print(f"SHA-256: {sha256_hash}")


# 🧩 Calculate checksum for large files
import hashlib


def calculate_file_checksum(filename, algorithm="md5"):
    """Calculate checksum for large files in chunks."""
    if algorithm == "md5":
        hash_obj = hashlib.md5()
    elif algorithm == "sha256":
        hash_obj = hashlib.sha256()
    elif algorithm == "sha1":
        hash_obj = hashlib.sha1()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)  # Read 8KB chunks
            if not chunk:
                break
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


# Calculate different checksums
md5_hash = calculate_file_checksum("large_file.txt", "md5")
sha256_hash = calculate_file_checksum("large_file.txt", "sha256")
print(f"MD5: {md5_hash}")
print(f"SHA-256: {sha256_hash}")


# 🧩 Verify file integrity with checksum
import hashlib
import os


def verify_file_integrity(filename, expected_checksum, algorithm="md5"):
    """Verify file integrity against expected checksum."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        return False

    # Calculate actual checksum
    if algorithm == "md5":
        hash_obj = hashlib.md5()
    elif algorithm == "sha256":
        hash_obj = hashlib.sha256()
    else:
        print(f"Unsupported algorithm: {algorithm}")
        return False

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hash_obj.update(chunk)

    actual_checksum = hash_obj.hexdigest()

    # Compare checksums
    if actual_checksum.lower() == expected_checksum.lower():
        print(f"✓ File integrity verified ({algorithm})")
        return True
    else:
        print("✗ File integrity check failed!")
        print(f"Expected: {expected_checksum}")
        print(f"Actual:   {actual_checksum}")
        return False


# Verify file integrity
expected_md5 = "d41d8cd98f00b204e9800998ecf8427e"
verify_file_integrity("file.txt", expected_md5, "md5")
