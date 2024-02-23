import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# nonce = os.urandom(8)
nonce = b'\xeb\xb3\x18\x94\xfe\xa8v@'
# key = os.urandom(32)
key = b'\xee\x82\xeeg\x96H\xe3\xadHt\x9a\xe4\xa7[4\xed\x90A\\T\xdce\xb1\x8c4\xbcJ\xfev\x82\xf7\xbe'
counter = 0

cipher = Cipher(algorithm = algorithms.ChaCha20(key, struct.pack("<Q", counter) + nonce), mode=None)

encryptor = cipher.encryptor()
ct = encryptor.update(b"Hello world")
print(ct)

decryptor = cipher.decryptor()
print(decryptor.update(ct))