class Nodo:

    def __init__(self,dato = None, next=None):
        self.dato = None
        self.next = None

    def __str__(self):
        return srt(self.dato)


class LinkedList:

    def __init__(self):
        self.len = 0
        self.head = None

    def addPpio(self, dato):
        nodo = Nodo(dato)
        nodo.next = self.head
        self.head = nodo
        self.len += 1

    def deleteInPosition(self,pos):

        if (pos < 0) or (pos >= self.len):
            raise IndexError("indice fuera de rango")
        if pos == None:
            pos = self.len-1

        if pos == 0:
            dato = self.head.dato
            self.head = self.head.next

    def buscar(self,dato):






# class Solution:
#     def removeNthFromEnd(self, A, B):
#         if not A:
#             return A
#
#         tail = A
#
#         for _ in xrange(B):
#             tail = tail if tail is None else tail.next
#
#         if tail is None:
#             return A.next
#
#         prev = None
#         curr = A
#
#         while tail:
#             tail = tail.next
#             prev = curr
#             curr = curr.next
#
#         prev.next = curr.next
#
#         return A

