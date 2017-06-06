def leerAtras(A):
    cont = 0
    for i in range(len(A)-1,-1,-1):
        if A[i]!= ' ':
            cont += 1
            if A[i-1] == ' ':
                break
        else:
            continue

    return cont

def factorial(A):
    fact = 1
    cont = 0
    while A>1:
        fact *= A
        A -=1
    A = str(fact)
    for i in range(len(A)-1,-1,-1):
        if A[i] == '0':
            cont +=1
        else:
            break


    return cont

def factorial2(A):
    fact = 1
    cont = 0
    while A>1:
        fact *= A
        A -=1
    while True:
        if fact%10 == 0:
            cont +=1
            fact = fact/10
        else:
            break


    return cont

def trailingZeroes(A):
    ret = 0
    while A != 0:
        ret += (A / 5)
        A /= 5
    return ret






print trailingZeroes(9247)
