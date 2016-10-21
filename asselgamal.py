from miller import primalidade
from gauss import Gauss
from random import randrange
from euclidiano import inverso
from hashlib import sha256 

def Gera(n1, n2):
    for i in range(n1, n2+1):
        if(primalidade(i)):
            p = i
            break
    g = Gauss(p)
    a = 2 + randrange(p-3)
    v = pow(g, a, p)
    return (p, g, a, v)    

def Assina(p, g, a, m):
    mensagem = sha256(m);
    mensagem = int(mensagem.hexdigest(), base=16)
    k = 2 + randrange(p-3)
    r = pow(g, k, p)
    k_inv = inverso(k, p-1)
    s = (k_inv*(mensagem - a*r))%(p-1)
    return (r, s)    

def Verifica(p, g, v, m, Am):
    if(Am[0]<1 or Am[0]>p-1):
        return False
    mensagem = sha256(m);
    mensagem = int(mensagem.hexdigest(), base=16)

    u1 = (pow(v, Am[0], p) * pow(Am[0], Am[1], p))%p
    u2 = pow(g, mensagem, p)
    if(u1==u2):
        return True
    else:
        return False
