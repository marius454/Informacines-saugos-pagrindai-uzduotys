
# newList = list()
# sum = 0
# for i in range(len(senasList)):
#     if (i % 25 == 0 and i != 0):
#         newList.append(sum)
#         sum = 0

#     sum += senasList[i]

# from itertools import islice
# import math

# n = 3
# newList = list()
# senasList = [1,2,3,4,5,6,7,8,9,10]
# size = len(senasList) / n
# senasList = iter(senasList)
# tempList = [list(islice(senasList, n)) for i in range(int(math.ceil(size)))]
# for item in tempList:
#     newList.append(sum(item))

# print(tempList)
# print(newList)



# primeDivisorList = []
    # for i in range(2, math.sqrt(n) + 1):
    #     if (n % i == 0 and isPrime(i)):
    #         primeDivisorList.append(i)
    
    # return primeDivisorList

    
# def getPossibleDivisorPairs(n):
#     primeDivisorList = getPrimeFactors(n)
#     possibleDivisorPairs = []
#     if len(primeDivisorList) == 2:
#         possibleDivisorPairs.append(primeDivisorList)
#     else:
#         primeDivisorList = list(comb(primeDivisorList, 2))
#         for item in primeDivisorList:
#             if item[0] * item[1] == n:
#                 possibleDivisorPairs.append(primeDivisorList)
    
#     return possibleDivisorPairs


        # possibleDivisorPairs = getPossibleDivisorPairs(n)
        # for item in possibleDivisorPairs:
        #     fi = n - item[0] - item[1] + 1
        #     for i in range(2, fi + 1):
        #         if getGCD(i, fi)[0] == 1:
        #             possibleCipherExponents.append(i)




from quickPow_7LD import getQuickRemainder
from possibleExponents_10LD import getPossibleCipherExponents

try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Choose an e from a below coprimes array:\n")
print(str(getPossibleCipherExponents(p, q)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = getQuickRemainder(m,e,n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = getQuickRemainder(c,d,n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")

