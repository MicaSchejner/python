def buscar_sumas(list,num):

    izq = 0
    der = len(list)-1
    medio = (izq+der)/2

    print "izq"
    print izq
    print "der"
    print der
    print "medio"
    print list[medio]
    if list[medio]<=num:
        der = medio + 1
        print list[:der]
    else:
        izq = medio + 1
        print list[izq:]


    return list[:der]

list = [1,3,4,7,8,10]
print buscar_sumas(list, 10)


    

