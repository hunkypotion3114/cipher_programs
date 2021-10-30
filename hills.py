import random
import numpy as np


def alphabetInitialise():
    alphabet = []
    for a in range(0,26):
        alphabet.append(chr(a+65))
    alphabet.append(" ")
    return alphabet


def keyGenerator():
    keyList = []
    for a in range(0,4):
        randomNum = random.randint(1,20)
        keyList.append(randomNum)
    matrix = np.reshape(keyList , (2,2))
    return matrix 


def encryption(plainText):
    if(len(plainText)%2 != 0):
        plainText += " "
    alphabet = alphabetInitialise()
    rowLength = len(plainText)//2
    matrixInv = keyGenerator()
    keyMatrix = np.linalg.inv(matrixInv)
    index = np.reshape(list(map(lambda x: alphabet.index(x) , list(plainText))) , (rowLength , 2))
    cipherChr = []
    for b in range(0, rowLength):
        multipliedMatrix = index[b]
        multipliedMatrix = multipliedMatrix@matrixInv
        cipherChr.extend([alphabet[multipliedMatrix[0]%27] , alphabet[multipliedMatrix[1]%27]])
    cipher = "".join(cipherChr)
    print([cipher,matrixInv], sep="\n")


# encryption("HELLO WORLD")


def decryption(cipher):
    keyMatrix = np.array(cipher[1])
    alphabet = alphabetInitialise()
    indexes = np.reshape(list(map(lambda x : alphabet.index(x) , list(cipher[0]))), (len(cipher[0])//2,2))
    matrixMax = []
    for a in range(0,2):
        matrixSum = sum(keyMatrix[:,a])
        matrixMax.append(matrixSum)
    print(matrixMax , keyMatrix , indexes, sep="\n")
    constTerm = (keyMatrix[0,0]*keyMatrix[1,1] - keyMatrix[0,1]*keyMatrix[1,0])
    possibleValues = []
    counter = 0
    # while counter < len(cipher)//2:
    #     remainderList = indexes[counter]
    #     individualPossibleValues = []
    #     # for a in range(0, (matrixMax[0])):


decryption(['RLKKHEFQWKVN', [[11,  9],[12, 14]]])