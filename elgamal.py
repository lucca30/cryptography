from miller import primalidade
from gauss import Gauss
from random import randrange
from euclidiano import inverso

def Gera(n1, n2):
    for i in range(n1, n2+1):
        if(primalidade(i)):
            p = i
            break
    g = Gauss(p)
    d = 2 + randrange(p-3)
    c = pow(g, d, p)
    return (p, g, c, d)    

def Encripta(p, g, c, m):
    k = 2 + randrange(p-3)
    s = pow(g, k, p)
    t = (m*pow(c, k, p))%p
    return (s, t)    

def Decripta(p, d, m_):
    S_inv = inverso(m_[0], p)
    S_linha = pow(S_inv, d, p)
    m_linha = (S_linha * m_[1])%p
    return m_linha
