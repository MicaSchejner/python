def find(tup,targ):

    if type(tup) == int:
        return [-1, -1]
    #isInList = targ in tup

    if targ in tup == False:
        return [-1,-1]
    else:
        #inicio = tup.index(targ)
        final = 0
        for i in range(tup.index(targ)+1, len(tup)):
            if tup[i] == targ:
                final = i
            else:
                final = i-1
                break


    return [tup.index(targ),final]


arr = (4,7,7,7,8,10,10)

print find(arr,3)
