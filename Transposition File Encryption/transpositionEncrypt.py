import pyperclip

def main():
    myMessage = 'Alvins hot juice box'
    myKey = 9

    ciphertext = encryptMessage(myKey, myMessage)

    #Use "|" incase there are spaces at the end
    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #Each string in the text is like a column in a grid
    ciphertext = [''] * key

    #Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        #Keep looping until cipherIndex goes past the message lenght
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            #Move currentIndex over
            currentIndex += key

    #Convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
