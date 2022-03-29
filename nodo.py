class Nodo:

    def __init__(self, Node):
        self.Node = Node
        self.siguiente = None
        self.anterior = None

    def __str__(self) -> str:
        return str(self.Node) 