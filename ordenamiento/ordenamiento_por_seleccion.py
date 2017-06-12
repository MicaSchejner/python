def ordenamiento_por_seleccion(list):

    for i in range(len(list)):
        minIndex = indexOfMinimum(list,i)
        swap(list,i,minIndex)

    return list




def swap(list, firstIndex, secondIndex):
    tmp = list[firstIndex]
    list[firstIndex] = list[secondIndex]
    list[secondIndex] = tmp




def indexOfMinimum(list,startIndex):
    minValue = list[startIndex]
    minIndex = startIndex

    for i in range(minIndex+1,len(list),1):
        if list[i] < minValue:
            minIndex = i
            minValue = list[i]

    return minIndex


list = [18,6,66,44,9,22,14]

# print indexOfMinimum(list,0)
print ordenamiento_por_seleccion(list)
