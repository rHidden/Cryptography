from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

message = input('Enter text to encrypt: ')

key = ''
while True:
    print('Optional - enter a key of length 16. If nothing is passed, the program generates the key.')
    optionalKey = input('Enter a key: ')
    if len(optionalKey) > 0 and len(optionalKey) % 16 == 0:
        key = bytes(optionalKey, 'UTF-8')
        break
    elif len(optionalKey) == 0:
        key = os.urandom(16)
        break
    else:
        print("Invalid key length. Please enter a key of length 16 or leave it empty to generate a random key.")

def pad(message):
    padding_len = 16 - (len(message) % 16)
    padding = bytes([padding_len] * padding_len)
    return message + padding

def unpad(message):
    padding_len = message[-1]
    return message[:-padding_len]

def encrypt(text):
    iv = os.urandom(16)
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(pad(text)) + encryptor.finalize()
    return iv + cipherText

def decrypt(ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
    decryptor = cipher.decryptor()
    decryptedMessage = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad(decryptedMessage)

cipherText = encrypt(message.encode('utf-8'))
print(cipherText)

decipherText = decrypt(cipherText)
print(decipherText.decode('utf-8'))
