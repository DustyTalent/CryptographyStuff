import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('Welcome to the Substitution Cipher!')
    print('''\nWhat would you like to do?
          1.Encrypt
          2.Decrypt
          3.Quit\n''')
    
    while True:
        choice0 = input('> ')

        if choice0 == '1':
            myMode = 'encrypt'
            print('\nYou chose encryption mode.\n')
            break
        elif choice0 == '2':
            myMode = 'decrypt'
            print('\nYou chose decryption mode.\n')
            break
        elif choice0 == '3':
            print('\nGoodbye user\n')
            sys.exit()
        else:
            print('Invalid Input')

    print('Now enter the message.\n')
    myMessage = input('> ')
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

    print('\nThe key has already been chosen for you\n')

    if not keyIsValid(myKey):
        sys.exit('There is an issue in the key or symbol set')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)

def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # Decrypt can use the same code as encrypt just need to
        # swap where the LETTERS and key strings are used
        charsA, charsB =charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            #Encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            #Symbol is not in LETTERS; just add it
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()