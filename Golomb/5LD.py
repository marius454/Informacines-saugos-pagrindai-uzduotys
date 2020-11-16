# LD 5: 
# 1. Sudaryti tiesinių registrų sistemos (TRS) modelį. 
# 2. Sugeneruoti Vernamo kriptosistemos raktą (Golombo pseudoatsitiktinę seką), tenkinantį atsitiktinumo testus. 
# 3. Atlikti testus (T1, T2, T4, T5).

from Golomb import getTests, printCheck
import random


def linearReg(c):
    X = []
    for i in range(len(c)):
        X.append(int(round(random.random(), 0)))
        
    n = len(X)
    m = pow(2, n) - 1
    c = c[::-1]
    string = ""

    for i in range(m):
        string += str(X[n-1])
        temp = 0
        for j in range(n):
            temp += int(X[j])*int(c[j])
        
        j = n-1
        while j > 0:
            X[j] = X[j-1]
            j -= 1

        X[0] = str(temp % 2)

    return string

string = linearReg("1000001")
print (string)
printCheck(string, 0.05)

string = linearReg("1000111")
print (string)
printCheck(string, 0.05)

string = linearReg("1100101")
print (string)
printCheck(string, 0.05)

string = linearReg("10010101")
print (string)
printCheck(string, 0.05)

string = linearReg("10110001")
print (string)
printCheck(string, 0.05)

string = linearReg("11100001")
print (string)
printCheck(string, 0.05)

# tests = getTests(string)
# print ("T1 =", tests[0], "T2 =", tests[1], "T4 =", tests[2], "|T5| =", tests[3])














def linearRegister(seed):
    X = [char for char in seed]
    # c = X[::-1]
    n = len(X)
    # c[n-1] = "1"
    # print (X, c)

    string = ""
    m = pow(2, n) - 1
    for i in range(m):
        string += X[n-1]
        temp = ""
        if X[n-1] == X[n-2]:
            temp = "0"
        else:
            temp = "1"

        j = n-3
        while j > 0:
            if temp == X[j]:
                temp = "0"
            else:
                temp = "1"
            j -= 1

        # temp = 0
        # for i in range(n):
        #     temp += int(X[i])*int(c[i])
        # temp = temp % 2

        j = n-1
        while j > 0:
            X[j] = X[j-1]
            j -= 1
        X[0] = temp
        # X[0] = str(temp)
        # c = X[::-1]
        # c[n-1] = "1"
        # print (X, c)
    print(string)
    return string


        