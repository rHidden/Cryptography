from cryptography.hazmat.primitives import hashes, hmac
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def computeTag(message, key):
    mac = hmac.HMAC(key, hashes.SHA256())
    tag = mac.update(message)
    tag = mac.finalize()
    return tag

def verifyTag(message, key, tag):
    computedTag = computeTag(message, key)
    return tag == computedTag

def decryptThenMac(ciphertext, enc_key, mac_key, nonce, tag):
    mac = hmac.HMAC(mac_key, hashes.SHA256)
    mac.update(ciphertext)
    computedTag = mac.finalize()
    if computedTag == tag:
        decryptor = cipher.decryptor()
        decryptedPlaintext = decryptor.update(ciphertext)
        decryptedPlaintext += decryptor.finalize()

message = b'This is a test.'

key_base64 = b'WXvqxbAEEM08snXbYgu8bg=='
nonce_base64 = b'ZmRqZW1ma3Jtc2thbXNuZA=='
key = base64.b64decode(key_base64)
nonce = base64.b64decode(nonce_base64)
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

key = urandom(16)
tag = computeTag(ciphertext, key)
print('MAC Tag: ', tag.hex())

result = verifyTag(ciphertext, key, tag)
print('MAC Verified: ', result)
print('Decrypted message: ', decryptor.update(ciphertext))