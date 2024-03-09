from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from hashlib import sha256

"""
given access to some values during a diffy helman key exchange, this
program uses the little and big step algorithm to find a matching
a in order to create another working key for decryption
"""
# Provided values (update these)
p = 0x
g = 0x
A = 0x
B = 0x
ciphertext = b'goes here'

# Brute-force loop for a
def baby_step_giant_step(g, A, p):
    N = int(p ** 0.5) + 1

    # Precompute baby steps
    baby_steps = {pow(g, b, p): b for b in range(N)}

    # Compute factor used for giant steps
    g_inv = pow(g, -N, p)

    # Take giant steps
    for j in range(N):
        candidate = (A * pow(g_inv, j, p)) % p
        if candidate in baby_steps:
            return j * N + baby_steps[candidate]

    return None  # No solution found

# Use the baby-step giant-step algorithm to find a
a = baby_step_giant_step(g, A, p)
print(f"Found a: {a}")
# Calculate shared secret
C = pow(B, a, p)

# Derive key from shared secret
hash = sha256()
hash.update(long_to_bytes(C))
key = hash.digest()[:16]

# Decrypt ciphertext
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), 16)

print("Decrypted plaintext:", plaintext.decode())
