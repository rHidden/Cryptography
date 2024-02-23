from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

key_base64 = b'WXvqxbAEEM08snXbYgu8bg=='
nonce_base64 = b'ZmRqZW1ma3Jtc2thbXNuZA=='
ciphertext_base64 = b'M8owlYB5ewJJ2YFcdLdXJu0DHlv4+9iqUpdpJeRyH3SRqg=='

key = base64.b64decode(key_base64)
nonce = base64.b64decode(nonce_base64)
ciphertext = base64.b64decode(ciphertext_base64)

cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))

decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print("Decrypted plaintext:", plaintext.decode())
