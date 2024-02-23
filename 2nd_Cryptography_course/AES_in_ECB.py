from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.hazmat.primitives.ciphers import algorithms
import os


key = os.urandom(16)
message = b'Hello world, hey'
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())

def encrypt(text):
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(text)
    cipherText += encryptor.finalize()
    return cipherText

cipherText = encrypt(message)
print(cipherText)

def decrypt(ciphertext):
    decryptor = cipher.decryptor()
    decryptedMessage = decryptor.update(ciphertext)
    decryptedMessage += decryptor.finalize()
    return decryptedMessage

decipherText = decrypt(cipherText)
print(decipherText)