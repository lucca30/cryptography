def inverso(n, p):
    alpha1 = 1
    alpha2 = 0
    resto1 = n
    resto2 = p
    while(True):
        temp = resto1%resto2
        quociente = resto1//resto2
        if(temp==0):
            break
        resto1 = resto2
        resto2 = temp
        temp = alpha1 - alpha2*quociente
        alpha1 = alpha2
        alpha2 = temp
    return alpha2%p

def completo(n, p):
    alpha1 = 1
    alpha2 = 0
    beta1 = 1
    beta2 = 0
    resto1 = n
    resto2 = p
    while(True):
        temp = resto1%resto2
        quociente = resto1//resto2
        if(temp==0):
            break
        resto1 = resto2
        resto2 = temp
        temp = alpha1 - alpha2*quociente
        alpha1 = alpha2
        alpha2 = temp
        temp = beta1 - beta2*quociente
        beta1 = beta2
        beta2 = temp
    return (alpha2, beta2, resto2)
