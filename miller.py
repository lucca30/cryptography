# if n < 3,317,044,064,679,887,385,961,981, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41.
def primalidade(N):
    for i in range(2,50000):
        if(N%i==0):
            return False
    if(N%2==0):
        return False
    if((not Miller(N, 2)) or (not Miller(N, 3)) or (not Miller(N, 5)) or (not Miller(N, 7))):
        return False
    if((not Miller(N, 11)) or (not Miller(N, 13)) or (not Miller(N, 17)) or (not Miller(N, 19))):
        return False
    if((not Miller(N, 23)) or (not Miller(N, 29)) or (not Miller(N, 31)) or (not Miller(N, 37)) or (not Miller(N, 41))):
        return False
    return True
def Miller(N, b):
    q=N-1
    k=0
    while(q%2==0):
         q = q//2
         k += 1

    r = pow(b, q, N)
         
    for i in range(0, k):
        if( (i==0 and r==1) or r==N-1 ):
            return True
        #True seria o equivalente a teste inconclusivo
        r = pow(r, 2, N)
    return False
        #False seria o equivalente a numero composto
