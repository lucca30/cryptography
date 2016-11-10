from random import randint
from elliptic_basics import *

def lenstra(N):
    A = randint(2, N-1);
    a = randint(2, N-1);
    b = randint(2, N-1);
    P = (a, b)
    B = (b**2 - a**3 - A*a)%N
    j = 2
    while(True):
        Q = multiply(P, A, B, N, j)
        P = Q
        if(Q[0]=="error"):
            if(Q[1]!=N):
                return Q[1]
            else:
                return "TENTE NOVAMENTE"
        j+=1
