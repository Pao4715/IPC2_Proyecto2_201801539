from listaDoble import ListaDoble

class Ciudad:

    def __init__(self, nombre, noFilas, columnas):
        self.nombre = nombre
        self.noFilas = noFilas
        self.columnas = columnas
        self.filas = ListaDoble()
        self.unidadM = ListaDoble()


    def __str__(self) -> str:
        return "{" + str(self.nombre) + ", " + str(self.noFilas) + ", " + str(self.columnas) + "}"