def quick_sort(lista):
    if len(lista) < 2:
        return lista
    menores,medio,mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)

def _partition(lista):

    pivote = lista[0]
    menores = []
    mayores = []
    for x in xrange(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores

lista = [8,-3,5,7,4,2]
print quick_sort(lista)