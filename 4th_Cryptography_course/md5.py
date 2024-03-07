from cryptography.hazmat.primitives import hashes

text = input('Enter string:')

encoded_text = text.encode()

md5Hash = hashes.Hash(hashes.MD5())
md5Hash.update(encoded_text)
md5Digest = md5Hash.finalize()
print(md5Digest.hex())