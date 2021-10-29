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
        randomNum = random.randint(11,43)
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
        cipherChr.extend([alphabet[multipliedMatrix[0]%26] , alphabet[multipliedMatrix[1]%26]])
    cipher = "".join(cipherChr)
    print(keyMatrix,cipher, sep="\n")


encryption("HELLO WORLD")