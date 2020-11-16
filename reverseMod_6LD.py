import math
import sympy as sp

def getGCD(nr1, nr2):
    divFinder = [[nr1, nr2, nr1 % nr2, nr1 // nr2]]
    n = len(divFinder)

    while divFinder[n-1][2] > 0:
        r = divFinder[n-1][1] % divFinder[n-1][2]
        d = divFinder[n-1][1] // divFinder[n-1][2]
        divFinder.append([divFinder[n-1][1], divFinder[n-1][2], r, d])
        n = len(divFinder)

    gcd = divFinder[n-1][1]
    return gcd, divFinder

# gcd = getGCD(57, 10)[0]
# print (gcd)
# gcd, divfinder = getGCD(42, 56)
# print (gcd)
# gcd, divfinder = getGCD(152, 34)
# print (gcd)
# gcd, divfinder = getGCD(858, 246)
# print (gcd)

def calcReverseMod(number, mod):

    gcd, divFinder = getGCD(number, mod)
    reverseDivFinder = divFinder[::-1]
    del reverseDivFinder[0]
    # if len(reverseDivFinder) == 1:
    if mod % number == 0:
        print (number, "is not an invertable module", mod)
        mod = mod + 1
        print ("finding calcReverseMod(", number, ",", mod, ") instead")

        gcd, divFinder = getGCD(number, mod)
        reverseDivFinder = divFinder[::-1]
        del reverseDivFinder[0]

    n = len(reverseDivFinder)

    # for item in reverseDivFinder:
    #     print (item)

    formula = ""

    for item in reverseDivFinder:
        temp = ""
        if formula == "":
            temp = " " + str(item[0]) + " - " + str(item[1]) + " * " + str(item[3]) + " "
            formula = temp
        else:
            old = " " + str(item[2]) + " "
            temp = "( " + str(item[0]) + " - " + str(item[1]) + " * " + str(item[3]) + " )"
            formula = formula.replace(old, temp)

    formula = formula.replace(" " + str(reverseDivFinder[n-1][0]) + " ", " x ")
    formula = formula.replace(" " + str(reverseDivFinder[n-1][1]) + " ", " y ")
    x, y = sp.symbols('x,y')
    
    # print ("formula:", reverseDivFinder[0][2], "=", formula)
    formula = "g = " + formula
    ldict = {'x': sp.symbols('x'), 'y': sp.symbols('y')}
    exec(formula, globals(), ldict)

    g = ldict['g']
    # sp.pprint(g)
    g = str(g).replace(" ", "")

    temp = ""
    A = 0
    for char in str(g):
        if char != "*" and char != "x" and char != "y":
            temp += char
        elif char == "*" or char == "x":
            if temp == "":
                A = 1
            elif temp == "-":
                A = -1
            elif temp[0] == "-":
                A = int(temp[1:]) * -1
            else:
                A = int(temp)
            break

    # print ("Didziausias bendras daliklis:", gcd)
    # print ("Atsakymas:", A % mod)
    # print ("")

    return A % mod


# calcReverseMod(37, 190210129)
# calcReverseMod(11, 23)
# calcReverseMod(3, 1710930)

# calcReverseMod(35, 12)
# calcReverseMod(84, 5)
# calcReverseMod(60, 7)

# calcReverseMod(105, 2)
# calcReverseMod(70, 3)
# calcReverseMod(30, 7)

# y1 = 11
# y2 = 4
# y3 = 2
# a1 = 1
# a2 = 3
# a3 = 0
# M1 = 35
# M2 = 84
# M3 = 60

# print(a1*y1*M1 + a2*y2*M2 + a3*y3*M3)
# print (1710933*1710933*1710933)

# print(pow(2,pow(2,6)) % 7)
# print (pow(1710933, 1710933) % 2)