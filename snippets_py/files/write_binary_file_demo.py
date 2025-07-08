# 🧩 Write binary file
with open("file.bin", "wb") as f:
    f.write(b"Hello, World!")


# 🧩 Write binary file from string
text = "Hello, World!"
with open("file.bin", "wb") as f:
    f.write(text.encode("utf-8"))


# 🧩 Write binary file with structured data
import struct


def write_binary_structure(filename, data_type, data):
    """Write structured binary data to file."""
    with open(filename, "wb") as f:
        if data_type == "string":
            data_bytes = data.encode("utf-8")
            length = len(data_bytes)
            # Write header: length (4 bytes) + type (4 bytes)
            f.write(struct.pack(">II", length, 1))
            f.write(data_bytes)
        elif data_type == "integer":
            f.write(struct.pack(">II", 4, 2))  # length=4, type=2
            f.write(struct.pack(">I", data))
        elif data_type == "float":
            f.write(struct.pack(">II", 4, 3))  # length=4, type=3
            f.write(struct.pack(">f", data))


# Write different data types
write_binary_structure("data.bin", "string", "Hello, World!")
write_binary_structure("data.bin", "integer", 42)
write_binary_structure("data.bin", "float", 3.14)


# 🧩 Write binary file with checksum
import hashlib
import struct


def write_binary_with_checksum(filename, data):
    """Write binary data to file with checksum for integrity."""
    checksum = hashlib.md5(data).hexdigest()
    with open(filename, "wb") as f:
        # Write checksum length and checksum
        checksum_bytes = checksum.encode("utf-8")
        f.write(struct.pack(">I", len(checksum_bytes)))
        f.write(checksum_bytes)
        # Write data length and data
        f.write(struct.pack(">I", len(data)))
        f.write(data)


write_binary_with_checksum("data_with_checksum.bin", b"important binary data")
