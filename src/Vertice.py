"""Clase que representa un vértice de una digráfica."""

class Vertice():
    
    def __init__(self, nombre : str):
        self.nombre = nombre
        self.v = False

    def obtenerNombre(self):
        return self.nombre
    
    def fueVisitado(self):
        return self.v
    
    def visitado(self):
        self.v = True