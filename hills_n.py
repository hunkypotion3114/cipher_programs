# let us begin this amazing journey through shit. LOL
import random
import numpy as np


def alphabetinitialise():
    lowerCase = []
    upperCase = []
    for a in range(0,26):
        lowerCaseChr = chr(97+a)
        upperCaseChr = chr(65+a)
        lowerCase.append(lowerCaseChr)        
        upperCase.append(upperCaseChr)
    alphabet = upperCase + lowerCase
    alphabet.append(" ")
    return alphabet


def keyGenerator(n):
    counter = 0
    matrix = []
    while counter < n:
        axis = []
        for b in range(0,n):
            item = random.randint(13,31)
            axis.append(item)
        matrix.append(axis)
        counter += 1
    matrix = np.array(matrix)
    return matrix


def encryption(plainText):
    alphabet = alphabetinitialise()
    if len(plainText)//2 < 3:
        n = 2
    else:
        n = random.randint(2,(len(plainText)//2))
    while len(plainText)%n != 0:
        plainText += " "
    plainText = list(plainText)
    row = len(plainText)//n
    indexes = np.reshape(np.array(list(map(lambda x: alphabet.index(x) , plainText))) , (row, n))
    matrixInv = keyGenerator(n)
    keyMatrix = np.linalg.inv(matrixInv)
    cipherText = []
    for d in range(0,row):
        axis = indexes[d]
        matrixProduct = axis @ matrixInv
        cipherText.extend(list(map(lambda x: alphabet[x%53] , matrixProduct)))
    cipherText = "".join(cipherText)
    cipher = [cipherText , keyMatrix , n]
    return cipher


print(encryption("Hello World"))

