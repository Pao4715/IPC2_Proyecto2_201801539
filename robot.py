class Robot:

    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad


    def __str__(self) -> str:
        return "{" + str(self.nombre) + ", " + str(self.tipo) + ", " + str(self.capacidad) + "}"
        