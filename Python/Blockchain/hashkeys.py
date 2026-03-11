import hashlib

# Input string
input_string = "Hello, world!"

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the bytes of the input string
hash_object.update(input_string.encode('utf-8'))

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

print("SHA-256 Hash:", hex_dig)
