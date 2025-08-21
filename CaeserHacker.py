print('Caeser Cipher Hacker')

#Let the user enter the encypted messahe
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): #Loops through every possible key
    translated = ''

    #Decrypt each symbol
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key #Decrypt the number

            #Handle the wrap-around if num is less than 0
            if num < 0:
                num = num + len(SYMBOLS)

            #put the dycrepted number's symbol to translated message
            translated = translated + SYMBOLS[num]
        else:
            #Just add the symbol without decrypting
            translated = translated + symbol

    #Display the key being tested, along with decrypted text
    print('Key #{}: {}'.format(key, translated))
