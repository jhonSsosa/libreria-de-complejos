import math
import cmath
# Operacion de numeros imaginarios.

def suma(a,b):
    cc = (a[0] + b[0])
    ci = (a[1] + b[1])
    return (cc,ci)


def resta(a,b):
    cc = (a[0] - b[0])
    ci = (a[1] - b[1])
    return (cc, ci)


def producto(a,b):
    cc = ((a[0] * b[0]) - (a[1] * b[1]))
    ci = ((a[0] * b[1]) + (b[0] * a[1]))
    return (cc, ci)


def divicion(a,b):
    cc = (((a[0] * b[0]) + (b[1] * a[1])) / (b[0] * 2 + b[1] * 2))
    ci = (((b[0] * a[1]) - (a[0] * b[1])) / (b[0] * 2 + b[1] * 2))
    return(cc,ci)


def modulo(a):
    a = (((a[0]) * 2 + (a[1])*2) * (1 / 2))
    return a

def conjugado(a):
    a = (a[0],a[1] * (-1))
    return a

def rectangular_polar(a):
    cc = math.atan2(a[1], a[0])
    ci = math.sqrt((a[0] * a[0]) + (a[1] * a[1]))
    return(cc,ci)

def complejo(a):
    cc = (a[0] * cmath.cos(a[1]))
    ci = (a[0] * cmath.sin(a[1]))
    return(cc,ci)

def prettyprinting(a):
    if type(a) == tuple:
        if a[1] < 0:
            print(a[0],a[1],"i")
        elif a[1] == 0:
            print(a[0])
        else:
            print(a[0],"+",a[1],"i")
    else:
        print(a)

def prettyPrintingPolar(c):
    print("(" + str(a[0]) + "," + str(a[1]) + ")")

a = (4, 5)
b = (3, 6)

prettyprinting(suma(a,b))
prettyprinting(resta(a,b))
prettyprinting(producto(a,b))
prettyprinting(divicion(a,b))
prettyprinting(modulo(a))
prettyprinting(conjugado(a))
prettyPrintingPolar(rectangular_polar(a))
prettyPrintingPolar(complejo(a))
