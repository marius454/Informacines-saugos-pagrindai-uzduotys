from RSAcipher_11LD import isPrime
from quickPow_7LD import getQuickRemainder
import random
from math import gcd

def pollard_rho(n, seed=2, f=lambda x: (x**2 + 732) % n):
    a, b = seed, seed
    factors = []
    i = 0
    isNPrime = False
    while not isNPrime:
        d = 1
        a = int(f(a) % n)
        b = int(f(f(b)) % n)
        d = gcd((a - b) % n, n)
        i += 1
        if d != 1 and d not in factors and d != n:
            factors.append(int(d))
            n = n // d
            isNPrime = isPrime(int(n))

    factors.append(int(n))
    factors.sort()
    return factors

def printPollard(n):
    p = pollard_rho(n)
    print(p)

    factorString = "{} = ".format(n)
    for factor in p:
        factorString = factorString + "{} * ".format(factor)

    factorString = factorString[:-3]
    print(factorString)
    print("------------------------------------")


n = 11111111111111111111111111111
printPollard(n)

n = 4722366482869645141
printPollard(n)

n = 34571317791
printPollard(n)

n = 1073741823
printPollard(n)




# print(isPrime(36893488147419103231))
# n = 340282366920938463463374607431768211457