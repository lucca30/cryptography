from euclidiano import inverso
def mdc(a, b):
    if(b==0):
        return a
    return mdc(b, a%b)
def fatorar(n):
    i=2
    lista = []
    while(True):
        if(n%i==0):
            multiplicidade = 1
            while(True):
                n = n/i
                if(n%i!=0):
                    break
                multiplicidade+=1
            lista.append((i, multiplicidade))
        i+=1
        if(n==1):
            break;
    return lista

def Chinese((x1, m1), (x2, m2)):
    t = (x2-x1)*inverso(m1, m2)%m2
    return (m1*t+x1, m1*m2)
