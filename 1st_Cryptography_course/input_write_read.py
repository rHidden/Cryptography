input = input('Enter string: ')
encodedInput = input.encode('UTF-8')

with open('input_write_read.txt', 'wb') as f:
    f.write(encodedInput)

with open('input_write_read.txt', 'rb') as f:
    print(f.read())