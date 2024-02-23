import string

plaintext = 0b1100
key = 0b1001

ciphertext = plaintext ^ key
var = ciphertext ^ key

print('ciphertext: ', bin(ciphertext))
print('var: ', bin(var))

bit_position = 0
bit_value = (ciphertext >> bit_position) & 1

new_ciphertext = (ciphertext ^ (1 << bit_position)) ^ key

print("changed cipher text:", bin(new_ciphertext))

print(5%21)
print(17%11)
print(-27%23)