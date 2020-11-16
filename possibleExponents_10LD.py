# 10 LD: Rasti visas galimas šifravimo eksponentes, kai RSA modulis yra duotas.
# Rezultatas: šifravimo eksponentės ir jų skaičius.

import math
from itertools import combinations as comb
from reverseMod_6LD import getGCD, calcReverseMod


def getPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors



def getPossibleCipherExponents(value1, value2 = None):
    possibleCipherExponents = []
    if value2 == None:
        n = value1

        possibleDivisorPairs = getPrimeFactors(n)
        fi = n - possibleDivisorPairs[0] - possibleDivisorPairs[1] + 1
        for i in range(2, fi + 1):
            if getGCD(i, fi)[0] == 1:
                possibleCipherExponents.append(i)
    else:
        p = value1
        q = value2
        
        fi = p*q - p - q + 1
        for i in range(2, fi + 1):
            if getGCD(i, fi)[0] == 1:
                possibleCipherExponents.append(i)

    return possibleCipherExponents
    


# n = 999997
# print(getPrimeFactors(n))
# print(getPossibleDivisorPairs(n))
# print (getPossibleCipherExponents(n))
# print (getPossibleCipherExponents(157,17))
