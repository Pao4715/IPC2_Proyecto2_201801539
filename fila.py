class Fila:

    def __init__(self, numero, secuencia):
        self.numero = numero
        self.secuencia = secuencia

    def __str__(self) -> str:
        return "{" + str(self.numero) + ", " + str(self.secuencia) + ", " +  "}"