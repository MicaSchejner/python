def merge_sort(list):
    if len(list) <= 1:
        return list

    medio = len(list)/2
    izq = merge_sort(list[:medio])
    der = merge_sort(list[medio:])
    return merge(izq,der)

def merge(list1,list2):
    i = 0
    j = 0
    lista_rta = []
    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            lista_rta.append(list1[i])
            i += 1
        else:
            lista_rta.append(list2[j])
            j += 1

    lista_rta += list1[i:]
    lista_rta += list2[j:]
    return lista_rta


lista = [8,-3,5,7,4,2]
print merge_sort(lista)
