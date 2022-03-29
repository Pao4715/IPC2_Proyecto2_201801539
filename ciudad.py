from listaDoble import ListaDoble

class Ciudad:

    def __init__(self):
        self.nombre = None
        self.noFilas = None
        self.columnas = None
        self.filas = ListaDoble()
        self.unidadesM = ListaDoble()


    def __str__(self) -> str:
        aux = self.filas.primero
        fila = '\n'
        while aux:
            fila += str(aux.Node) + '\n'
            aux = aux.siguiente

        aux2 = self.unidadesM.primero
        unidad = '\n'
        while aux2:
            unidad += str(aux2.Node) + '\n'
            aux2 = aux2.siguiente

        return "{" + str(self.nombre) + ", " + str(self.noFilas) + ", " + str(self.columnas) + ', ' + fila +  ", " + unidad + '}'