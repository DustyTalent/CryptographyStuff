#Cracking Codes Ceaser cipher

import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Ask the user if they want to Encrypt or Decrypt
while True:
    print("Do you want to (E)ncrypt or (D)ecrypt?")
    response = input('> ').upper()
    if response.startswith('E'):
        mode = 'encrypt'
        break
    elif response.startswith('D'):
        mode = 'decrypt'
        break
    else:
        print('Invalid Input, enter an \'e\' or a \'d\'.')
        continue

# Ask the user for to input key
while True:
    maxKey = len(SYMBOLS)
    print("Enter the key (1 - 26)")
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

#Let the user enter the message
print('Enter the message to {}.'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #perform eyncryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound id needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Append the symbol without enycrpting/decrypting
        translated = translated + symbol

#Output the translated string
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass #Do nothing if pyclip is not installed
