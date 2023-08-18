from Vertice import Vertice

"""Clase que implementa una digráfica."""
class Grafica:

    def __init__(self, vertices : list, aristas : list):
        self.vertices = vertices
        self.aristas = aristas
        self.cjtoInde = []

    def obténCjtoIndependiente(self, primerVertice : Vertice):
        """
            Devuelve el conjunto independiente de la gráfica.

            De forma recursiva tendremos:

            1.- Elige el primer vértice dado en la gráfica (pasado como parámetro).
            2.- Lo añade al conjunto independiente.
            3.- Obtiene los vértices adyacentes al vértice elegido.
            4.- Los vértices adyacentes no son parte del conjunto, por lo que se marcan sólo como visitados.
            5.- Para los vértices adyacentes a los adyacentes al vértice inicial, se evalúa si sus vértices adyacentes son parte del conjunto independiente obtenido al momento.
                Si para algún vértice resulta falso, entonces:
                5.1.- Se repite el proceso desde el paso 2.
            
            6.- Se repite el proceso desde el paso 1 con el siguiente vértice de la gráfica que no ha sido visitado.
            7.- El proceso termina cuando se hayan visitado todos los vértices de la gráfica.
            8.- Se devuelve el conjunto independiente.
        """
        self.cjtoInde.append(primerVertice)

        primerVertice.visitado()
        
        # Se obtienen los vértices adyacentes.
        adyacentes = self.__obténAdyacentes(primerVertice)

        # Se marcan como visitados los vértices adyacentes.
        for vertice in adyacentes:
            vertice.visitado()

        # Se evalúan los vértices adyacentes a los adyacentes.
        for vertice in adyacentes:
            adyacentesAdyacentes = self.__obténAdyacentes(vertice)
            for verticeAdyacente in adyacentesAdyacentes:
                vAdyacentes = self.__obténAdyacentes(verticeAdyacente)
                for vAdyacente in vAdyacentes:
                    if verticeAdyacente.fueVisitado() == False:
                        for verticeCjtoInd in self.cjtoInde:
                            if (verticeCjtoInd.obtenerNombre() == vAdyacente.obtenerNombre()) and (verticeAdyacente.fueVisitado() == False):
                                verticeAdyacente.visitado()
                if verticeAdyacente.fueVisitado() == False:
                    self.obténCjtoIndependiente(verticeAdyacente)

        # Se repite el proceso con el siguiente vértice que no ha sido visitado y si ya fueron todos visitados, devolverá al conjunto independiente de esta gráfica.
        for vertice in self.vertices:
            if vertice.fueVisitado() == False:
                self.obténCjtoIndependiente(vertice)

        return self.cjtoInde

    def __obténAdyacentes(self, vertice : Vertice):
        """Método privado que devuelve los vértices adyacentes a un vértice dado."""
        adyacentes = []
        for arista in self.aristas:
            if arista.antecesor().obtenerNombre() == vertice.obtenerNombre():
                adyacentes.append(arista.sucesor())
        return adyacentes