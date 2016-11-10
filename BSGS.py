from math import sqrt
from euclidiano import inverso
def BSGS(p, g, h, ordem):
    m = int(sqrt(ordem))
    if (sqrt(p-1) - m != 0):
        m += 1
    j = 0
    B = []
    while(j<m):
        s = pow(g, j, p)
        B.append(s)
        j+=1
    g_ = inverso(g, p)
    t = pow(g_, m, p)
    i=0
    while(i<m):
        s = (pow(t, i, p)*h)%p
        if(s in B):
            j = B.index(s)
            x = (i*m + j)
            return x
        i+=1
    return 0
