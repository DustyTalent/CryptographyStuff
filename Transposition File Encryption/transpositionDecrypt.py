import math, pyperclip

def main():
    myMessage = 'Atol xvjiunisc eh ob'
    myKey = 9

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    #Number of "shaded boxes" in the last column of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = ['']*numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column

        # If there are no more columns or we're at a shaded box, go back
        # to the first column and the next row
        if (column == numOfColumns) or (column == numOfColumns - 1 and
                                        row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return''.join(plaintext)

if __name__=='__main__':
    main()
    
