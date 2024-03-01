from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
from os import urandom

#Exercise 2
plaintext = b'Hello darkness my old friend'
key_base64 = b'WXvqxbAEEM08snXbYgu8bg=='
nonce_base64 = b'ZmRqZW1ma3Jtc2thbXNuZA=='

key = base64.b64decode(key_base64)
nonce = base64.b64decode(nonce_base64)

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))

encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

print("cipher:", ciphertext)

modifiedCipherText = ciphertext[0:4] + b'2' + ciphertext[5:]

decryptor = cipher.decryptor()
compromisedPlaintext = decryptor.update(modifiedCipherText) + decryptor.finalize()

print('compromisedPlaintext:', compromisedPlaintext)

#Exercise 3
randomCiphertext = urandom(16)
print(decryptor.update(randomCiphertext)+ decryptor.finalize()) #Not working - Why? - It was already finalized before
