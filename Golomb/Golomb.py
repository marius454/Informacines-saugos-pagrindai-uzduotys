# LD 4: Algoritmizuoti statistikų T1, T2, T4 skaičiavimą. Apskaičiuoti statistikų reikšmes, kaip testinę seką naudojant 1) pirmas 3 vardo raidės (t.y. 24 bitai sekoje); 2) LD 3 raktą.
import math
from scipy.stats import chi2
from scipy.stats import norm

def getTests(test_string, P):
    N1 = test_string.count("1")
    N0 = test_string.count("0")
    n = len(test_string)

    T1 = (pow((N1-N0), 2)) / n
    T1check = chi2.ppf(1 - P, 1)

    N00 = 0
    N01 = 0
    N10 = 0
    N11 = 0

    for i in range(len(test_string) - 1):
        if test_string[i] == "0":
            if test_string[i+1] == "0":
                N00 += 1
            else:
                N01 += 1
        else:
            if test_string[i+1] == "0":
                N10 += 1
            else:
                N11 += 1

    T2 = ((4/(n-1)) * (pow(N00, 2) + pow(N01, 2) + pow(N10, 2) + pow(N11, 2))) - ((2/n) * (pow(N0, 2) + pow(N1, 2))) +1
    T2check = chi2.ppf(1 - P, 2)

    F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    repeating0 = 0
    repeating1 = 0
    for i in range(len(test_string)):
        if test_string[i] == "0":
            repeating0 += 1
            if repeating1 > 0:
                G[repeating1 - 1] += 1
                repeating1 = 0
            if i == len(test_string) - 1:
                F[repeating0 - 1] += 1
        else:
            repeating1 += 1
            if repeating0 > 0:
                F[repeating0 - 1] += 1
                repeating0 = 0
            if i == len(test_string) - 1:
                G[repeating1 - 1] += 1

    Ei = (n-1+3) / (pow(2, 1+2))

    T4 = 0
    i = 1
    while Ei >= 5:
        T4 += ((pow((F[i-1]-Ei),2)) / Ei) + ((pow((G[i-1]-Ei),2)) / Ei)
        i += 1
        Ei = (n-i+3) / (pow(2, i+2))
    T4check = chi2.ppf(1 - P, 2*i - 2)

    d = int(n/2)
    # d = 5
    Xd = 0

    for i in range(n-d):
        if test_string[i] == test_string[i+d-1]:
            Xd += 1

    # print(Xd)
    T5 = (2*Xd-n+d) / (math.sqrt(n-d))
    T5check = norm.ppf(1 - P/2, 0, 1)

    tests = {
        "T1": T1,
        "T2": T2,
        "T4": T4,
        "T5": abs(T5),
        "T1check": T1check,
        "T2check": T2check,
        "T4check": T4check,
        "T5check": T5check,
    }

    return tests

# test_string = "010011010110000101110010"
# test_string = "010011010110000101110010011010010111010101110011"
# test_string = "01001001011001110110111101110010011010010111001101100010011001010110110001101111011101100110000101110011"

# tests = getTests(test_string, 0.05)
# print (tests)


def printCheck(string, P):
    tests = getTests(string, P)
    print (tests)
    if tests["T1"] < tests["T1check"]:
        print ("T1 - Pass")
    else:
        print ("T1 - Fail")

    if tests["T2"] < tests["T2check"]:
        print ("T2 - Pass")
    else:
        print ("T2 - Fail")

    if tests["T4"] < tests["T4check"]:
        print ("T4 - Pass")
    else:
        print ("T4 - Fail")

    if tests["T5"] < tests["T5check"]:
        print ("T5 - Pass")
    else:
        print ("T5 - Fail")
    