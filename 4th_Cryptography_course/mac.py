from cryptography.hazmat.primitives import hashes, hmac
from os import urandom

def computeTag(message, key):
    mac = hmac.HMAC(key, hashes.SHA256())
    tag = mac.update(message)
    tag = mac.finalize()
    return tag

def verifyTag(message, key, tag):
    computedTag = computeTag(message, key)
    return tag == computedTag

key = urandom(16)
message = b'This is a test.'

tag = computeTag(message, key)
print(tag.hex())

result = verifyTag(message, key, tag)
print(result)