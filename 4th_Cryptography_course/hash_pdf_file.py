from cryptography.hazmat.primitives import hashes

def hash_file(filename):
    sha1Hash = hashes.Hash(hashes.SHA1())
    md5Hash = hashes.Hash(hashes.MD5())
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            md5Hash.update(chunk)
            sha1Hash.update(chunk)
    md5Digest = md5Hash.finalize()
    sha1Digest = sha1Hash.finalize()
    print(filename)
    print('md5: ' + md5Digest.hex())
    print('sha1:' + sha1Digest.hex())

filename = 'shattered-1.pdf'
hash_file(filename)
filename2 = 'shattered-2.pdf'
hash_file(filename2)