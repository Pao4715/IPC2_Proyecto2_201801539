from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertarNodo(self, Node):
        if self.primero is None:
            self.primero = self.ultimo = Nodo(Node)
        else: 
            actual = self.ultimo
            self.ultimo = actual.siguiente = Nodo(Node)
            self.ultimo.anterior = actual

    
    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.Node)
            actual = actual.siguiente

    
    def buscar(self, ciudad):
        if self.primero is None:
            return
        actual = self.primero
        while actual:
            if actual.Node.nombre == ciudad:
                return actual.Node
            actual = actual.siguiente