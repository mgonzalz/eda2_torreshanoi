'''
class nodoPila():
    

class Pila():
    '''


class nodoPila(object):
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila(object):
    def __init__(self):
        self.superior = None
        self.tamanio = 0
    def apilar(self, dato):
        if self.superior == None:
            self.superior = nodoPila(dato)
            return
        nuevo_nodo = nodoPila(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
    def desapilar(self):
        if self.superior == None:
            print('Pila vacia')
            return
        self.superior = self.superior.siguiente
    def __str__(self):
        nodo_actual = self.superior
        while nodo_actual != None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return ''
