class UnidadM:

    def __init__(self, fila, columna, capacidad):
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad

    def __str__(self) -> str:
        return "{" + str(self.fila) + ", " + str(self.columna) + ", " + str(self.capacidad) + "}"