# LD 7: 1. Užprogramuoti greitojo kėlimo laipsniu algorimą.2. Apskaičiuoti (Stud.kn.Nr.)^{Pirminis_{Nr.Sąr+10}} mod (Pirminis_{Nr.Sąr+10}-Nr.Sąr)

import math

def getQuickRemainder(x, n, s):
    nBinaryStr = str(bin(n))[2:]
    nBinaryStr = nBinaryStr[::-1]

    rPrev = 0
    rMultProduct = 1

    # print("Intermediate remainders:", end=" ")
    for i in range(len(nBinaryStr)):
        remainder = 0
        if i == 0:
            remainder = x % s
        else:
            remainder = (rPrev * rPrev) % s

        # print(remainder, end=" ")

        rPrev = remainder
        if nBinaryStr[i] == "1":
            rMultProduct = (remainder * rMultProduct) % s
            
    # print ("")
    # print (x, "^", n, " mod(", s, ") = ", rMultProduct, sep="")
    # print ("")

    return rMultProduct

# getQuickRemainder(10,31,31)
# getQuickRemainder(17,60,1001)
# getQuickRemainder(1710930, 37, 37-12)
# getQuickRemainder(1710930, 37, 37-2)

# getQuickRemainder(134110512159248, 181, 31)