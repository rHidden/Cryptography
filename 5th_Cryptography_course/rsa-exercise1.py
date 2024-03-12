def decrypt(ciphertext, private_key, modulus):
    return pow(ciphertext, private_key, modulus)

def encrypt(plaintext, public_key, modulus):
    return pow(plaintext, public_key, modulus)

n = 2537
e = 13
d = 937
ciphertext = 2222

# (a) Modulus
print("(a) Modulus:", n)

# (b) Decryption
plaintext = decrypt(ciphertext, d, n)
print("(b) Decryption:", plaintext)

# (c) Encryption
new_ciphertext = encrypt(plaintext, e, n)
print("(c) Encryption:", new_ciphertext)
