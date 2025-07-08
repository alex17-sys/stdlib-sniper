# 🧩 Read binary file
with open("file.bin", "rb") as f:
    data = f.read()
print(f"Read {len(data)} bytes")


# 🧩 Read binary file in chunks
with open("file.bin", "rb") as f:
    chunk = f.read(1024)  # Read 1KB at a time
    while chunk:
        print(f"Read {len(chunk)} bytes")
        chunk = f.read(1024)


# 🧩 Read binary file with specific encoding
def read_binary_as_text(filename, encoding="utf-8"):
    """Read binary file and decode as text."""
    try:
        with open(filename, "rb") as f:
            data = f.read()
            return data.decode(encoding)
    except UnicodeDecodeError:
        print(f"Cannot decode file with {encoding} encoding")
        return None


text = read_binary_as_text("file.bin", "utf-8")
if text:
    print(text)


# 🧩 Read binary file with structure parsing
import struct


def read_binary_structure(filename):
    """Read binary file with structured data parsing."""
    with open(filename, "rb") as f:
        # Read header (4 bytes for length, 4 bytes for type)
        header = f.read(8)
        if len(header) < 8:
            return None

        # Unpack header using struct
        length, data_type = struct.unpack(">II", header)

        # Read data based on type
        if data_type == 1:  # String
            data = f.read(length).decode("utf-8")
        elif data_type == 2:  # Integer
            data = struct.unpack(">I", f.read(4))[0]
        elif data_type == 3:  # Float
            data = struct.unpack(">f", f.read(4))[0]
        else:
            data = f.read(length)

        return {"length": length, "type": data_type, "data": data}


result = read_binary_structure("structured.bin")
if result:
    print(f"Type: {result['type']}, Data: {result['data']}")
