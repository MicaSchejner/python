def diffk(list,int):
    for i in range(len(list)-1,-1,-1):
        resta = list[i] - list[i-1]
        print resta
        if resta == int:
            return 1

    return 0

arr = [1,3,5]
print diffk(arr,2)
