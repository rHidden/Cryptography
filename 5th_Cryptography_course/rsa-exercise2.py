def decrypt(ciphertext, private_key, modulus):
    return pow(ciphertext, private_key, modulus)

def encrypt(plaintext, public_key, modulus):
    return pow(plaintext, public_key, modulus)

n = 2537
e = 13
d = 937

plaintext1 = 64
plaintext2 = 900

ciphertext1 = encrypt(plaintext1, e, n)
ciphertext2 = encrypt(plaintext2, e, n)

res = (ciphertext1 * ciphertext2) % n

print('Ciphertext 1: ',ciphertext1)
print('Ciphertext 2: ',ciphertext2)
print('Decryption of multiplication: ',decrypt(res, d, n))


