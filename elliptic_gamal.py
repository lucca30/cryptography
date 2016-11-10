from elliptic_basics import *
from random import randint

def gera(Prime,E, point):
    n = randint(2, Prime)
    Q = multiply(point, E[0], E[1], Prime, n)
    return (Q, E, n, Prime, point)

def encripta(Msg, Q, E, Prime, point):
    k = randint(2, Prime)
    c1 = multiply(point, E[0], E[1], Prime, k)
    c2 = sum(Msg, multiply(Q, E[0], E[1], Prime, k), E[0], E[1], Prime)
    return (c1, c2)

def decripta(Cifrado, E, Prime, n):
    temp = multiply(Cifrado[0], E[0], E[1], Prime, n)
    temp2 = (temp[0], -temp[1])
    return sum(Cifrado[1],temp2, E[0], E[1], Prime )
