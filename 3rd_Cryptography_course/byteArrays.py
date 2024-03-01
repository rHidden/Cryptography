#a
barr1 = bytearray()
barr2 = b'Python 3 programming'
#b
barr1 = barr2[0:7] + b'2' + barr2[8:]
print(barr1)
#c
print('Length of barr1:', len(barr1))
print('Length of barr2:', len(barr2))
#d
print(barr1)
print('5th character of barr1',barr1[5])
#e
print('5th character of barr1 in ASCII:', chr(barr1[5]))
#f
print('Hexadecimal representation of barr1:', ' '.join([hex(byte) for byte in barr1]))
