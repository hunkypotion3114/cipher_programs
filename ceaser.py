import random
def initialiseKey(shiftBy):
    indexList = []
    lowerCase= []
    upperCase = []
    for a in range(65,91):
        indexList.append(a-64)
        lowerCase.append(chr(a+32))
        upperCase.append(chr(a))
        indexList.append(a-64+26)
    alphabetList = upperCase + lowerCase
    i = 53
    while len(indexList) != 63:
        indexList.append(i)
        i += 1
    indexList.sort()
    alphabetList += list(map(lambda x: str(x), indexList[:9]))
    alphabetList.extend(["0", " "])
    shiftValue = indexList[:shiftBy]
    indexList = indexList[shiftBy:]
    indexList.extend(shiftValue)
    keyValue = [indexList, alphabetList]
    return keyValue


def encryption(plainText):
    shiftBy = random.randint(1,52)
    keyValue = initialiseKey(shiftBy)
    numericalKey = keyValue[0]
    chrs = keyValue[1]
    cipherText = "".join(list(map(lambda x: chrs[numericalKey[chrs.index(x)] -1], plainText)))
    cipher_key = [cipherText, shiftBy]
    return cipher_key


def decrpytion(cipherText, key):
    keyValue = initialiseKey(key)
    numericalKey = keyValue[0]
    chrs = keyValue[1]
    indexList = list(map(lambda x : numericalKey.index(chrs.index(x)+1), cipherText))
    plainText = "".join(list(map(lambda x: chrs[x], indexList)))
    return plainText
