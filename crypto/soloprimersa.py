from Crypto.Util.number import inverse, long_to_bytes

""" reverse modular arithmetic for cases where rsa was set up with only 1 factor for n"""

# Given values
n = # big prime number (not product)
e =   # Public exponent
c =   # Ciphertext

# Calculate the modular inverse of e modulo n
d = inverse(e, n-1)

# Decrypt the ciphertext
m = pow(c, d, n)

# Convert the decrypted message to bytes
plaintext = long_to_bytes(m)

print("Decrypted plaintext:", plaintext)
