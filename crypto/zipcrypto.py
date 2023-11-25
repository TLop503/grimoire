# Zip crypto encryption reverser
# set up for 12 bytes, jerry rig as needed
# fill buffer with encrypted bytes

# TODO: make this more readable

import zlib

def crc32(ch, crc):
    return ~zlib.crc32(bytes([ch]), ~crc) & 0xffffffff

def update_keys(keys, char):
    key0 = keys[0]
    key1 = keys[1]
    key2 = keys[2]
    # Update Key(0) using CRC32
    key0 = crc32(char, key0) & 0xFFFFFFFF

    # Update Key(1)
    key1 = (key1 + (key0 & 0xFF)) & 0xFFFFFFFF
    key1 = (key1 * 134775813 + 1) & 0xFFFFFFFF

    # Update Key(2) using CRC32
    key2 = crc32(key1 >> 24, key2) & 0xFFFFFFFF

    return (key0, key1, key2)

def decrypt_byte(keys):
    temp = (keys[2] | 2) & 0xFFFF
    return ((temp * (temp ^ 1)) >> 8) & 0xFF

# Read the 12-byte encryption header into Buffer
buffer = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]  # Initialize Buffer as a list of 12 zeros

# Replace this with your actual encrypted header data
# Example: buffer = [0x12, 0x34, 0x56, 0x78, 0x90, 0xAB, 0xCD, 0xEF, 0x12, 0x34, 0x56, 0x78]

# Initialize the keys with the provided values
keys = [305419896, 591751049, 878082192]

password = b'test'

for c in password:
    keys =  update_keys(keys, c)

# Decrypt the header and update keys
for i in range(12):
    C = buffer[i] ^ decrypt_byte(keys)
    keys = update_keys(keys, C)
    buffer[i] = C

# The updated keys can n w be used for further decryption
print("Updated Keys:", keys)
print(bytes(buffer))