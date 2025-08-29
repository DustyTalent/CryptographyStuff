#A reverse ceasar cipher that uses subtraction

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

while True:
    maxKey = len(SYMBOLS)
    print("Enter the key (1 - 26)")
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}.'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #I swapped 2 the encryption and decryption symbols
        if mode == 'encrypt':
            translatedIndex = symbolIndex - key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex + key

        # Handle wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #append the symbol
        translated = translated + symbol


print(translated)
