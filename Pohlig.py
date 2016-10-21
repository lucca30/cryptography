from basics import fatorar, Chinese
from euclidiano import inverso
from BSGS import BSGS
def PH(p, g, h):
    Fatores = fatorar(p-1)
    result = (0, 1)
    for i in Fatores:
        gi = (pow(g, (p-1)/(pow(i[0], i[1])), p))
        gi_ = (inverso(gi, p))
        hi = (pow(h, (p-1)/(pow(i[0], i[1])), p))
        xi = 0
        xij = 0
        gi_linha = pow(gi,pow(i[0], i[1]-1) , p)
        j = 0
        while(j<i[1]):
            hij = (pow(hi,pow(i[0], i[1]-1-j) , p) * pow(gi_,pow(i[0], (i[1]-1-j))*xi , p) )%p
            xij = BSGS(p, gi_linha, hij)
            xi +=( int(xij) * pow(i[0], j))
            j+=1
        result = Chinese(result, (xi, pow(i[0], i[1])))
    return result[0]
