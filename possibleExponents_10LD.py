# 10 LD: Rasti visas galimas šifravimo eksponentes, kai RSA modulis yra duotas.
# Rezultatas: šifravimo eksponentės ir jų skaičius.

import math
from itertools import combinations as comb
from reverseMod_6LD import getGCD

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

def getPossibleCipherExponents(value1):
    possibleCipherExponents = []
    n = value1

    possibleDivisorPairs = getPrimeFactors(n)
    fi = n - possibleDivisorPairs[0] - possibleDivisorPairs[1] + 1
    for i in range(2, fi + 1):
        if getGCD(i, fi)[0] == 1:
            possibleCipherExponents.append(i)

    return possibleCipherExponents



# n = 299
# print("")
# print(getPrimeFactors(n))
# print (getPossibleCipherExponents(n))

# n = 221
# print("")
# print(getPrimeFactors(n))
# print (getPossibleCipherExponents(n))

# n = 323
# print("")
# print(getPrimeFactors(n))
# print (getPossibleCipherExponents(n))

# n = 391
# print("")
# print(getPrimeFactors(n))
# print (getPossibleCipherExponents(n))

# n = 667
# print("")
# print(getPrimeFactors(n))
# print (getPossibleCipherExponents(n))
