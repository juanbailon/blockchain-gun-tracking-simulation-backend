import hashlib

def calculate_sha256_bytes(input_string: str) -> bytes:
    # Encode the input string to bytes before hashing
    encoded_string = input_string.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the encoded string
    sha256_hash.update(encoded_string)

    # Get the hash result as bytes
    hash_bytes = sha256_hash.digest()

    # Convert bytes to bits
    #hash_bits = ''.join(format(byte, '08b') for byte in hash_bytes)

    return hash_bytes


def bytes_to_unsigned_int(hash_bytes: bytes) -> int:
    # Convert bytes to integer
    hash_integer = int.from_bytes(hash_bytes, byteorder='big', signed=False)
    return hash_integer



if __name__ == "__main__":
    # Example usage when running the script directly
    input_string = "Hello, world!"
    hash_bytes_result = calculate_sha256_bytes(input_string)
    hash_integer_result = bytes_to_unsigned_int(hash_bytes_result)

    print(f"Input String: {input_string}")
    print(f"SHA-256 Hash as Bytes: {hash_bytes_result}")
    print(f"SHA-256 Hash as Integer: {hash_integer_result}")