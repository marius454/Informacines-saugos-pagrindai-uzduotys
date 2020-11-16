from RSAcipher_11LD import isPrime
from fractions import gcd
import random

def pollard_rho(n, seed=2, f=lambda x: x**2 + 1):
    x, y = seed, seed
    factors = []
    i = 0
    while i < 100000:
        d = 1
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd((x - y) % n, n)
        i += 1
        if d != 1 and d not in factors and d != n:
            factors.append(d)
            factors.append(int(n/d))
            i = 0
    factors.sort()
    return factors


n = 340282366920938463463374607431768211
# n = 1111111
# p = pollard_rho(n, random.randrange(2, n, 1), lambda x: (x**2 + 732) % n)
# p = pollard_rho(n, 2, lambda x: (x**2 + 732) % n)
p = pollard_rho(n)

print(p)


# 340282366920938463463374607431768211