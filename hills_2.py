# Hills 2*2 Cipher

import random
import numpy as np


# Creating char list
def alphabetInitialise():
    alphabet = []
    for a in range(0,26):
        alphabet.append(chr(a+65))
    alphabet.append(" ")
    return alphabet


# generating a 2*2 matrix containing random ints.
def keyGenerator():
    keyList = []
    for a in range(0,4):
        randomNum = random.randint(15,35)
        keyList.append(randomNum)
    matrix = np.reshape(keyList , (2,2))
    return matrix 

#--this˅
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
    print([cipher,keyMatrix])


encryption("HELLO WORLD")

#--this˅
def decryption(cipher):
    keyMatrix = np.linalg.inv(np.array(cipher[1]))
    matrixInv = []
    for x in range(0,2):
        axis = []
        for y in range(0,2):
            bleh = str(keyMatrix[x,y]).split(".")
            blehDecimal = bleh[1]
            if(blehDecimal[0] == "9"):
                axis.append(int(bleh[0])+1)
            else:
                axis.append(int(bleh[0]))
        matrixInv.append(axis)
    matrixInv = np.array(matrixInv)
    alphabet = alphabetInitialise()
    indexes = np.reshape(list(map(lambda x : alphabet.index(x) , list(cipher[0]))), (len(cipher[0])//2,2))
    matrixMax = []
    for a in range(0,2):
        matrixSum = sum(matrixInv[:,a])
        matrixMax.append(matrixSum)
    constTerm = (matrixInv[0,0]*matrixInv[1,1] - matrixInv[0,1]*matrixInv[1,0])
    plainChrs = []
    counter = 0
    while counter < len(cipher[0])//2:
        remainderList = indexes[counter]
        for a in range(0, (matrixMax[0] +1)):
            for b in range(0, (matrixMax[1]+1)):
                term1 = matrixInv[1,1]*(27*a + remainderList[0]) - matrixInv[1,0]*(27*b + remainderList[1]) 
                term2 = matrixInv[0,0]*(27*b + remainderList[1]) - matrixInv[0,1]*(27*a + remainderList[0])
                if(term1*term2) > 0:
                    if (term1*constTerm > 0):
                        quotientX = str(term1/constTerm).split(".")
                        quotientY = str(term2/constTerm).split(".")
                        if(quotientX[1] == "0" and quotientY[1] == "0"):
                            if(int(quotientX[0]) < 27 and int(quotientY[0]) < 27):
                                chr1 = alphabet[int(quotientX[0])]
                                chr2 = alphabet[int(quotientY[0])]
                                plainChrs.extend([chr1, chr2])
        counter += 1
    plaintText = "".join(plainChrs)
    print(plaintText)

decryption(['VRSEYQXWPNHN', [[ 0.0625, -0.02929688],[-0.0625,  0.06054688]]])