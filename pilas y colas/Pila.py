class Pila:
    def __init__(self):
        self.items = []

    def push(self,x):
        #agrega al final de la lista
        self.items.append(x)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            raise ValueError("The stack is empty")

    def peek(self):
        return self.items[len(self.items)-1]

    def empty(self):
        return self.items == []


