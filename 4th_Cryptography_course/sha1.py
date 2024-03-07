from cryptography.hazmat.primitives import hashes

text = input('Enter string:')

encoded_text = text.encode()

sha1Hash = hashes.Hash(hashes.SHA1())
sha1Hash.update(encoded_text)
sha1Digest = sha1Hash.finalize()
print(sha1Digest.hex())