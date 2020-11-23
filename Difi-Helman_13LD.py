# L13: Nulaužti Difi-Helmano schemą (rasti bendrą slaptą raktą). Duota:
# 1. Generatorius g = 7;
# 2. Grupės eilė n = 131071;
# 3,4. Gavėjo ir siūntėjo skaičiai GS = 79792266297612001, SS = 11398895185373143.

from quickPow_7LD import getQuickRemainder
from reverseMod_6LD import calcReverseMod
from math import sqrt

def bruteForceLog(g, gxmod, n):
    gj = 0
    j = 1
    while gj != gxmod:
        j += 1
        gj = getQuickRemainder(g, j, n)
    return j

def BstepGstepLog(g, gxmod, n):
    m = int(sqrt(n)) + 1
    B = []
    for i in range(m):
        gamaR = calcReverseMod(g, n)
        gamaR = getQuickRemainder(gamaR, i, n)
        agr = (gxmod * gamaR) % n
        if agr == 1:
            return i
        else:
            B.append([agr, i])
    delta = getQuickRemainder(g, m, n)

    for q in range(1, 1000000):
        deltaQ = getQuickRemainder(delta, q, n)
        for pair in B:
            if pair[0] == deltaQ:
                return q*m + pair[1]

    print(TimeoutError)
    exit()
        

def getDHSecretKey(g, n, gb, ga):
    gabmod = 0

    if (gb < ga):
        gbmod = gb % n
        # b = bruteForceLog(g, gbmod, n)
        b = BstepGstepLog(g, gbmod, n)
        gabmod = getQuickRemainder(ga % n, b, n)
    else:
        gamod = ga % n
        # a = bruteForceLog(g, gamod, n)
        a = BstepGstepLog(g, gamod, n)
        gabmod = getQuickRemainder(gb % n, a, n)

    print (gabmod)
    print ("---------------")
    return gabmod

print ("")

g = 7
n = 131071
gb = 79792266297612001
ga = 11398895185373143
getDHSecretKey(g, n, gb, ga)

g = 7
n = 331
gb = 79792266297612001
ga = 11398895185373143
getDHSecretKey(g, n, gb, ga)

