def ord_insercion(lista):

    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            reubicar(lista,i+1)

        print "DEBUG: ", lista

def reubicar(lista,p):

    key = lista[p]
    while p > 0 and key < lista[p-1]:
        lista[p] = lista[p-1]
        p -=1

    lista[p] = key
    print "DEBUG2: ", lista


list = [18,6,66,44,9,22,14]

# print indexOfMinimum(list,0)
print ord_insercion(list)
