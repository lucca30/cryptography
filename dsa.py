from miller import primalidade
from gauss import Gauss
from random import randrange
from euclidiano import inverso
from hashlib import sha256 

def Gera(n1, n2):
    for i in range(n1, n2+1):
        if(primalidade(i)):
            q = i
            break
    t=2
    while(True):
        if(primalidade(t*q+1)):
            p = t*q+1
            break
    g_linha = Gauss(p)
    g = pow(g_linha, (p-1)/q, p)
    a = 2 + randrange(p-2)
    v = pow(g,a,p)
    return p,q,g,a,v

def Assina(p, q, g, a, m):
    r = 0
    s = 0
    mensagem = sha256(m);
    mensagem = int(mensagem.hexdigest(), base=16)
    while(r==0 or s==0):
        k = 2 + randrange(q-2)
        r = pow(g, k, p)%q
        k_inv = inverso(k, q)
        s = (k_inv * (mensagem+a*r))%q
    return (r, s)        

def Verifica(p, q, g, v, m, Am):
    r = Am[0]
    s = Am[1]
    mensagem = sha256(m);
    mensagem = int(mensagem.hexdigest(), base=16)
    
    if(r<=0 or r>=q or s<=0 or s>=q):
        return False
    s_inv = inverso(s,q)
    u1 = (s_inv*mensagem)%q
    u2 = (r*s_inv)%q
    u3 = ((pow(g, u1, p)*pow(v, u2, p))%p)%q
    if(u3==r):
        return True
    return False
