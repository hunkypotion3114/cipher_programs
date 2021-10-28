import random
import numpy as np

def initialiseAlphabet():
    alphabet = []
    lowerCase = []
    for a in range(0,26):
        upperCaseChr = chr(a+65)
        lowerCaseChr = chr(a+97)
        lowerCase.append(lowerCaseChr)
        alphabet.append(upperCaseChr)
    alphabet.extend(lowerCase)
    alphabet.extend([" "])
    return alphabet

def keyGenerator(alphabet,lenOfText):
    key = []
    for b in range(0,8):
        keyValue = alphabet[random.randint(0,25)]
        key.append(keyValue)
    timesToMultiply = lenOfText // 8
    extraAddition = lenOfText % 8
    keyExtra = key[0:extraAddition]
    keyList = key*timesToMultiply
    keyList.extend(keyExtra)
    return [keyList,key]

def encryption(plainText):
    alphabet = initialiseAlphabet()
    lenOfText = len(plainText)
    keys = keyGenerator(alphabet, lenOfText)
    keyList = keys[0]
    key = keys[1]
    encryptionArray = np.array([keyList, list(plainText)])
    cipherText = ""
    for c in range(0, lenOfText):
        array = encryptionArray[:,c]
        indexOfChr = sum(list(map(lambda x: alphabet.index(x) , array)))% 53
        cipherText += alphabet[indexOfChr]
    cipher = [cipherText , "".join(key)]
    return cipher


# print(encryption("HIMANSHU UDUPI"))

def keyReplication(key, lenOfText):
    timesToMultiply = lenOfText // 8
    extraAddition = lenOfText % 8
    keyList = key*timesToMultiply
    keyList.extend(key[0:extraAddition])
    return keyList

def decryption(cipher):
    alphabet = initialiseAlphabet()
    cipherText = list(cipher[0])
    lenOfText = len(cipherText)
    key = list(cipher[1])
    print(key)
    keylist = keyReplication(key, lenOfText)
    cipherArray = np.array([keylist, cipherText])
    possibleChrs = []
    for d in range(0, lenOfText):
        array = cipherArray[:,d]
        indexes = list(map(lambda x: alphabet.index(x), array))
        if (53*1 + indexes[1] - indexes[0]) < 53:
            possibleChrs.append(alphabet[53*1 + indexes[1] - indexes[0]])
        else:
            possibleChrs.append(alphabet[53*0 + indexes[1] - indexes[0]])
    print(possibleChrs)

decryption(encryption("Hello world"))