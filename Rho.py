from basics import mdc
from euclidiano import *
from random import randint
a_y = 0
b_y = 0
a_z = 0
b_z = 0
def f(n, p, g, h):
    global a_y
    global b_y
    global a_z
    global b_z
    if(n[0]>=0 and n[0]<p/3):
        return ((n[0]*g)%p, (n[1]+1)%(p-1), n[2])
    if(n[0]>=p/3 and n[0]<(2*p)/3):
        return (pow(n[0], 2, p), (n[1]*2)%(p-1), (n[2]*2)%(p-1))
    if(n[0]>=(2*p)/3 and n[0]<p):
        return ((n[0]*h)%p, n[1], (n[2]+1)%(p-1))

def Rho(p, g, h):
    y = (1, 0, 0)
    z = (1, 0, 0)
    y = f(y, p, g, h)
    z = f(f(z, p, g, h), p, g, h)
    while(y[0]!=z[0]):
        y = f(y, p, g, h)
        z = f(z, p, g, h)
        z = f(z, p, g, h)

    u = y[1] - z[1]%(p-1)
    v =z[2] - y[2]%(p-1)
    if(v==0):
        return False
    if(mdc(v, p-1)==1):
        return (u*inverso(v, p-1))%(p-1)
    Tupla = completo(v, p-1)
    alpha = Tupla[0]
    beta = Tupla[1]
    d = Tupla[2]
    m = (p-1)/d
    t = (alpha*u)/d % m
    i=0
    while(i<d):
        ans = t+(m*i)
        if(pow(g, ans, p)==h):
            return ans
        i+=1
