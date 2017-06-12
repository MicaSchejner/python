def busqueda_binaria(list,num):

    izq = 0
    der = len(list)-1

    while der >= izq:
        medio = (izq + der) / 2
        if list[medio] == num:
            return medio
        elif list[medio] < num:
            izq = medio + 1
        else:
            der = medio - 1

    return -1



list = [1,2,3,6,8,9]

print busqueda_binaria(list,5)


    

