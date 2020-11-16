import operator as op
from functools import reduce

def nCr(n,r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

text_file = open(r"Vigenero/V.7.txt", "r")

coded_text = text_file.read().upper()
coded_text = ''.join(i for i in coded_text if i.isalnum())

print (coded_text)

# print (coded_text)

n = 26
N = len(coded_text)
kt = 0.067
k0 = round(1/n, 3)
sumComb = 0
for i in range(26):
    ai = chr(i + 65)
    mi = coded_text.count(ai)
    sumComb += nCr(mi, 2)

kc = round((1/nCr(N,2)) * sumComb, 3)
print (k0, kc, kt)

d = ((N * (kt-k0)) / ((kc * (N-1)) + kt - N*k0))

print ("d =", d)
print ("Rakto ilgis:", int(round(d, 0)))
