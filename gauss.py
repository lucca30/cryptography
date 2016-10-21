from math import sqrt
def Gauss(p):
    fatores = fatoracao(p-1)
    g = 1
    for i in fatores:
        a = 2
        while(pow(a, int((p-1)/i[0]), p)==1):
            a+=1
        h = pow(a, int((p-1)/(pow(i[0], i[1]))), p)
        g = (g*h)%p
    return g

def fatoracao(n):
    lista = []
    top = n
    for i in range (2, n):
        exp = 0
        while(n%i==0):
            exp+=1
            n = n/i
        if(exp!=0):
            lista.append((i, exp))
        if(n==1):
            break
    return lista
