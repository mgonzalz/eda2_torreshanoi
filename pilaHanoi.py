class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self, numero):
        self.cima = None
        self.tamanio = 0
        self.numero = numero
    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1
    def desapilar(self):
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x
    def __str__(self):
        lista = []
        nodo = self.cima
        while nodo:
            lista.append(nodo.info)
            nodo = nodo.sig
        return str(lista)
