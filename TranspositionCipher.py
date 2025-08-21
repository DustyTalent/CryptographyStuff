#The all in one Transposition Cipher, Encrypt and Decrypt in the same program

#To improve the program overall, it can also warn the user if the chosen key
# is too long or short to encrypt the message

import math, sys

def main():
    print('Welcome user to the Transposition Cipher!')
    print('''\nWhat Would you like to do?
1. Encrypt message
2. Decrypt message
3. Quit\n''')

    while True:
        choice0 = input('> ')

        if choice0 == '1':
            mode = 'encrypt'
            print('\nYou chose encryption mode.\n')
            break
        elif choice0 == '2':
            mode = 'decrypt'
            print('\nYou chose decryption mode.\n')
            break
        elif choice0 == '3':
            print('\nGoodbye user\n')
            sys.exit()
        else:
            print('Invalid Input')

    print('Now enter the message.\n')
    myMessage = input('> ')

    while True:
        print('\nEnter the key\n')
        myKey = input('> ')

        if not myKey.isdecimal():
            continue

        if 0 <= int(myKey):
            myKey = int(myKey)

            if (myKey == 1) or (myKey >= len(myMessage)):
                print('''If you enter a key of 1, the same length or a number bigger than
the number of chracters the message stays the same''')
            else:
                break
            
    if mode == 'encrypt':
        ciphertext = encryptMessage(myKey, myMessage)
        print(ciphertext + '|')
    elif mode == 'decrypt':
        plaintext = decryptMessage(myKey, myMessage)
        print(plaintext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    #Loop through each column
    for column in range(key):
        currentIndex = column

        #Loop until currentIndex goes past message length
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key

    return''.join(ciphertext)


def decryptMessage(key, message):
    #Calculate values, the number of columns in transposition grid
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if(column == numOfColumns) or (column == numOfColumns - 1 and
                                       row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return''.join(plaintext)
    


if __name__ == '__main__':
    main()
