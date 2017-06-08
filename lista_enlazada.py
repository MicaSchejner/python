class Nodo(object):

    def __init__(self,dato=None,prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

def verLista(nodo):

    while nodo:
        print nodo
        nodo = nodo.prox



v3=Nodo("Bananas")
v2=Nodo("Peras",v3)
v1=Nodo("Manzanas",v2)

verLista(v1)