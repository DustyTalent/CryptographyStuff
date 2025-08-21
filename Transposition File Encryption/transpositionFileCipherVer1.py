import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'testFile.encrypted.txt'
    outputFilename = 'testFile.decrypted.txt'

    myKey = 10
    myMode = 'decrypt'

    #If the input file does not exist, program ends
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quiting...' %(inputFilename))
        sys.exit()

    #If the output file already exists, give the user a chance to quit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %
              (outputFilename))
        respones = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message form the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    #Measure how long the Encryption/Decryption will take
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,
                                              len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__== '__main__':
    main()
