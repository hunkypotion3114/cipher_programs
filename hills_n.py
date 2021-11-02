# let us begin this amazing journey through shit. LOL
from math import remainder
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


def decryption(cipher):
    cipherText = list(cipher[0])
    n = cipher[2]
    keyMatrixInv = np.linalg.inv(cipher[1])
    alphabet = alphabetinitialise()
    matrixInv = []
    for e in range(0,n):
        axis = keyMatrixInv[e]
        for f in range(0,n):
            term = str(axis[f]).split(".")
            decimalVal = term[1]
            if decimalVal[0] == "9":
                matrixInv.append((int(term[0])) +1)
            else:
                matrixInv.append(int(term[0]))
    matrixInv = np.reshape(matrixInv , (n,n))
    remainderList = np.reshape(list(map(lambda x : alphabet.index(x) , cipherText)) , ((len(cipherText)//n) , n))

decryption(['GjstNxiopBJN', np.array([[ 0.12168397, -0.04867359,  0.05397924, -0.1005767 ],
       [ 0.05074971, -0.12029988, -0.06089965,  0.13056517],
       [-0.18800461,  0.07520185,  0.02560554,  0.08904268],
       [ 0.02422145,  0.09031142, -0.02906574, -0.07404844]]), 4])