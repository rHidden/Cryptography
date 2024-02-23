user_input = input('Enter value: ')

#Exercise 1
for char in user_input:
    byte_value = ord(char)
    print(char, 'byte value =', byte_value)

#Exercise 2
if isinstance(user_input, int):
    print('\nBinary input:', bin(int(user_input)))
    print('Hexadecimal input:', hex(int(user_input)))
else:
    print("\nInput is not an integer. Skipping...")

#Exercise 3
user_input2 = input('\nEnter string with danish letters to be encoded with UTF-8: ')
encodedInput = user_input2.encode('UTF-8')

with open('exercises_1-5.txt', 'wb') as f:
    f.write(encodedInput)

#Exercise 4 - ASCII CAN NOT READ DANISH STRINGS - SKIP
# user_input2 = input('\nEnter string with danish letters to be encoded with ASCII: ')
# encodedInput = user_input2.encode('ASCII')

# with open('exercises_1-5.txt', 'wb') as f:
#     f.write(encodedInput)

#Exercise 5
with open('spotify.png', 'rb') as f:
    signature = f.read(8)

print(signature)

