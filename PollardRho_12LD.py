from RSAcipher_11LD import isPrime
from quickPow_7LD import getQuickRemainder
import random
from math import gcd

def pollard_rho(n, seed=2, f=lambda x: (x**2 + 732) % n):
    x, y = seed, seed
    factors = []
    i = 0
    isNPrime = False
    while not isNPrime:
        d = 1
        x = int(f(x) % n)
        y = int(f(f(y)) % n)
        d = gcd((x - y) % n, n)
        i += 1
        if d != 1 and d not in factors and d != n:
            factors.append(int(d))
            n = n // d
            isNPrime = isPrime(int(n))

    factors.append(int(n))
    factors.sort()
    return factors


# n = 340282366920938463463374607431768211457
# n = 11111111111111111111111111111
# n = 4722366482869645141
# n = 34571317791
# n = 1073741823

p = pollard_rho(n)
print(p)

factorString = "{} = ".format(n)
for factor in p:
    factorString = factorString + "{} * ".format(factor)

factorString = factorString[:-3]
print(factorString)



# 340282366920938463463374607431768211457