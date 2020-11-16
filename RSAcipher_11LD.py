# LD 11: Sugeneruokite du tokius 8-bitų pirminius skaičius p ir q,
# kad RSA modulis būtų 16-bitų skaičiumi ir būtų galima naudoti šifravimo eksponentę p_{n+15}.
# Apskaičiuokite slaptąjį raktą ir užšifruokite savo vardą.

from possibleExponents_10LD import getPrimeFactors
from reverseMod_6LD import getGCD, calcReverseMod
from quickPow_7LD import getQuickRemainder
import math
import random
import textwrap

def isPrime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False 
        lst = list(range(3, int(math.sqrt(num)) + 1))
        lst = lst[0::2]
        for i in lst:
            if (num % i == 0):
                return False
        return True
    else:
        return False

def generate8BitPQ(e):
    if not isPrime(e):
        print("The given exponent is not a prime number")
        return
    p = 0
    q = 0
    check = 0
    while getGCD(e, p*q - p - q + 1)[0] != 1 or p*q < 0b111111111111111:
        p = random.randrange(128, 256, 2)
        q = random.randrange(128, 256, 2)

        if p == q:
            p = 0
            q = 0
        check += 1
        if check == 100:
            print ("Something is wrong, the program took too long")
            return
    
    print ("p = ", p, "q =", q)
    return p, q

# print(generate8BitPQ(59))

def RSA_Encrypt(text, e, p = None, q = None, blockLength = None):
    if p == None and q == None:
        print("p and q not provided, they will be generated randomly")
        p, q = generate8BitPQ(e)
    elif p == None:
        print("Only one argument of p and q is provided, it will not be used, both p and q will be generated randomly")
        p, q = generate8BitPQ(e)

    n = p*q
    fi = n - p - q + 1
    print ("fi =", fi)
    # print(getGCD(e, fi)[0])
    d = calcReverseMod(e, fi)
    cipher = ""
    encodingLength = 3
    if blockLength == None:
        blockLength = len(str(n)) - 1

    print ("public key = ({}, {})".format(n, e))
    print ("private key = ({}, {})".format(n, d))

    asciiBlocks = []
    block = ""
    for char in text:
        tempOrd = str(ord(char))
        while len(tempOrd) < encodingLength:
            tempOrd = "0" + tempOrd
        asciiBlocks.append(tempOrd)
    
    asciiText = ''.join(asciiBlocks)[::-1]
    print(''.join(asciiBlocks))
    blocks = textwrap.wrap(asciiText, blockLength)
    for i in range(len(blocks)):
        blocks[i] = blocks[i][::-1]
        # if int(blocks[i]) == 0:
        #     blocks.pop(i)
    blocks = blocks[::-1]
    print (blocks)

    for block in blocks:
        cipherBlock = str(getQuickRemainder(int(block), e, n))
        while len(cipherBlock) < blockLength:
            cipherBlock = "0" + cipherBlock
        
        print(block, cipherBlock)

        if len(cipherBlock) > blockLength:
            cipherBlock = cipherBlock[0:blockLength]
            # cipherBlock = cipherBlock[len(cipherBlock) - blockLength:len(cipherBlock)]
        cipher += cipherBlock
    
    print (cipher)
    print (RSA_Decrypt(cipher, n, d, blockLength))

    # return cipher


def RSA_Decrypt(cipher, n, d, blockLength):
    blocks = textwrap.wrap(cipher, blockLength)

    # blocks = blocks[::-1]
    print (blocks)
    asciiText = ""
    for block in blocks:
        m = str(getQuickRemainder(int(block), d, n))
        while len(str(m)) < blockLength:
            m = "0" + m
        if len(m) > blockLength:
            m = m[0:blockLength]
            # m = m[len(m) - blockLength:len(m)]
        print(block, m)
        asciiText += m
    print(asciiText)

    text = ""
    asciiBlocks = textwrap.wrap(asciiText[::-1], 3)
    asciiBlocks = asciiBlocks[::-1]
    isFrontZeroes = True
    for block in asciiBlocks:
        block = block[::-1]
        while len(block) < 3:
            block = "0" + block
        if block != "000":
            isFrontZeroes = False
        if not isFrontZeroes:
            text = text + chr(int(block))

    return text


# print(RSA_Encrypt("Vilnius", 59, 253, 191))

# print(RSA_Encrypt("Vilnius", 7, 11, 13))
# print(RSA_Encrypt("Vilnius", 59, 239, 227))
# print(RSA_Encrypt("Vilnius", 59, 247, 251))
# print(RSA_Encrypt("Vilnius", 59))
# print(RSA_Decrypt("24134187592814324096187592811434383", 54253, 2735))
# print(RSA_Decrypt("35001329302190235475329302158019818", 61997, 8339))
# print(RSA_Decrypt("070118004033118039080", 143, 103))


# RSA_Encrypt("Marius Bieliauskas", 59, 239, 227)
# RSA_Encrypt("Vilnius", 59)


# factors = getPrimeFactors(338898644639999)
# print(factors)
# fi = 338898644639999 - factors[0] - factors[1] + 1
# d = calcReverseMod(39827, fi)
# print(d)
# print("")
# print(RSA_Decrypt("134110512159248177845645444842", 338898644639999, d, 15))


# print(RSA_Encrypt("Daugai", 39827, 18409199, 18409201, 15))
# print(RSA_Encrypt("Vilnius", 939391, 993319, 999331, 12))

# print(RSA_Encrypt("Marius Bieliauskas", 59, 757, 1321, 6))