from Vertice import Vertice

"""Clase que representa una arista de una digráfica."""
class Arista():

    """Constructor de la Arista que recibe un par de vértices."""
    def __init__(self, anterior, siguiente):
        self.anterior = anterior
        self.siguiente = siguiente

    def antecesor(self):
        return self.anterior

    def sucesor(self):
        return self.siguiente