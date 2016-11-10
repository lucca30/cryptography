from euclidiano import inverso
from basics import mdc
#Define (inf, inf) as the neutral element of this algebra
# P1 and P2 are points in the Cartesian plane (x, y)
# A and B are coefficients of ellipitc equation in the form: Y^2=X^3+AX+B
def sum(P1, P2, A, B, mod):
    if(P1==("inf", "inf")):
        return P2
    elif(P2==("inf","inf")):
        return P1
    elif(P1[1]==-(P2[1]) and P1[0]==P2[0]):
        return ("inf", "inf")
    else:
        if(P1==P2):
            if(mdc(2*P1[1], mod)!=1):
                return ("error", mdc(2*P1[1], mod))
            lamb = (3*pow(P1[0],2)+A) *inverso(2*P1[1], mod)
        else:
            if(mdc(P2[0]-P1[0], mod)!=1):
                return ("error", mdc(P2[0]-P1[0], mod))
            lamb = (P2[1] - P1[1]) * inverso(P2[0] - P1[0], mod)
    x = (pow(lamb, 2)-P1[0]-P2[0]) % mod
    y = (lamb*(P1[0]-x) - P1[1]) % mod
    return (x,y)

def multiply(P1, A, B, mod, n):
    binary = bin(n)[2:]
    current = P1
    result = ("inf", "inf")
    for i in binary[::-1]:
        if(i=='1'):
            result = sum(result, current, A, B, mod)
        current = sum(current, current, A, B, mod)
        if(current[0]=="error"):
            return ("error", current[1])
    return result
