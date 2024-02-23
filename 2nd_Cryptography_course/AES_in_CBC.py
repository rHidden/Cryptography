from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.hazmat.primitives.ciphers import algorithms
import os

key = os.urandom(16)
message = b'Hello world, hey'

def encrypt(text):
    iv = os.urandom(16)
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(text) + encryptor.finalize()
    return iv + cipherText

def decrypt(ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()
    decryptedMessage = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedMessage


cipherText = encrypt(message)
print(cipherText)

decipherText = decrypt(cipherText)
print(decipherText)
