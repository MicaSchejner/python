def sum_digitos(num):

    if num < 10:
        return num
    else:
        return sum_digitos(num/10) + sum_digitos(num%10)


print sum_digitos(123)