from Pila import Pila

def divBy2(num):
    p = Pila()

    while num > 0:
        x = num % 2
        print x
        p.push(x)
        num = num // 2

    binString = ""
    while not p.empty():
        binString = binString + str(p.pop())

    return binString

print divBy2(5)