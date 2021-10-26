import random
import numpy as np


def keyGenerator():
    key = []
    storageOfCipher = []
    while len(key) != 8:
        term = random.randint(0,9)
        if term not in key:
            key.append(term)
        if len(storageOfCipher) != 8:
            storageOfCipher.append([])
    key_storage = [key, storageOfCipher]
    return key_storage


def rearrangingKeys(oldIndex, storageOfCipher, sortedCipher):
    value = storageOfCipher[oldIndex]
    sortedCipher.extend(value)
    return sortedCipher


def encryption(plainText):
    storageOfCipher, keys = keyGenerator()[1], keyGenerator()[0]
    for a in range(0,len(plainText)):
        index = a % 8
        indexList = storageOfCipher[index]
        indexList.append(plainText[a])
    sortedKeys =  sorted(keys)
    sortedCipher = []
    list(map(lambda x: rearrangingKeys(keys.index(x), storageOfCipher, sortedCipher), sortedKeys))
    cipher = ["".join(sortedCipher), keys]
    return cipher


def decryption(cipher):
    cipherText, keys = cipher[0], cipher[1]
    sortedKeys = sorted(keys)
    numOfChrs = []
    storageOfSort = []
    if len(cipherText) > 8:
        numOfChrs = list(np.ones(8, dtype=int))
        indexCounter = 0
        while sum(numOfChrs) != len(cipherText):
            numOfChrs[indexCounter] = numOfChrs[indexCounter] +1
            if(indexCounter == 7):
                indexCounter = 0
            else:
                indexCounter +=1
    else:
        list(np.ones(len(cipherText), dtype=int))
    chrList = list(cipherText)
    sliceStart = 0
    for c in range(0, len(sortedKeys)):
        index = keys.index(sortedKeys[c])
        sliceEnd = numOfChrs[index] + sliceStart
        storageOfSort.append(chrList[sliceStart:sliceEnd])
        sliceStart = sliceEnd
    finalSort = []
    for d in keys:
        indexToPush = sortedKeys.index(d)
        chrsPushed = storageOfSort[indexToPush]
        if(len(chrsPushed) != max(numOfChrs)):
            chrsPushed.append(" ")
        finalSort.append(chrsPushed)
    finalSort = np.array(finalSort)
    limit = np.shape(finalSort)[1]
    counter = 0
    plainText = ""
    while counter <= (limit-1):
        plainText += "".join(finalSort[:,counter])
        counter += 1
    return plainText
