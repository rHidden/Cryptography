text = 'Hello world'

encodedText = text.encode('UTF-8')

print('encoded type:', type(encodedText))
print('encoded text:', encodedText)

decodedText = encodedText.decode('UTF-8')

print('decoded type:', type(decodedText))
print('decoded text:', decodedText)
