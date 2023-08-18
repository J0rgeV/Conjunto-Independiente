from Grafica import Grafica
from Vertice import Vertice
from Arista import Arista
from colorama import init, Fore, Back, Style
init()

class Main:
    
    # Variable que contiene la ruta del archivo .txt en cadena.
    # f = open("../archivo/Grafica.txt")

    enEjecucion = True

    rutaTxt = ""

    print(Fore.CYAN + "Hola, bienvenid@. Este programa te ayudará a obtener un conjunto independiente de una digráfica.")
    print("¿Qué deseas hacer?")
    print("\n1. Obtener un conjunto independiente de una digráfica.")

    while enEjecucion:
        vertices = []
        aristas = []
        sinRuta = True
        print("Para salir, presiona cualquier tecla.")
        opcion = input("\nOpción: ")

        if opcion != "1":
            enEjecucion = False
            print(Fore.YELLOW + "¡Hasta la próxima!")
        else:
            print("Para obtener un conjunto independiente de una digráfica, introduce la dirección del archivo .txt que la contiene.\n")

            # Lee la ruta del archivo y lo guarda en una variable.
            while sinRuta and enEjecucion:
                try:
                    rutaTxt = input(Fore.CYAN + "Ruta del archivo: ")
                    archivo = open(rutaTxt)
                    print(Fore.RESET + "El archivo contiene lo siguiente:\n")
                    print(Fore.GREEN + archivo.read())
                    archivo.close()

                    primeraLínea = False

                    print(Fore.RESET + "\n\nLeyendo archivo...\n")

                    with open(rutaTxt) as archivo:
                        primeraLínea = False
                        # Lee el archivo línea por línea.
                        for linea in archivo:
                            # Crea los objetos de tipo Vértice.
                            if primeraLínea == False:
                                for i in range(0, len(linea)):
                                    caracter = linea[i]
                                    if caracter != ",":
                                        vertices.append(Vertice(caracter))
                                primeraLínea = True
                            
                            # Crea los objetos de tipo Arista.
                            else:
                                caracter1 = linea[0]
                                caracter2 = linea[2]

                                vertice1 = vertice2 = None
                                for elemento in vertices:
                                    if vertice1 == None or vertice2 == None:
                                        if elemento.obtenerNombre() == caracter1:
                                            vertice1 = elemento
                                        elif elemento.obtenerNombre() == caracter2:
                                            vertice2 = elemento
                                # Queremos asegurarnos de que se tenga un par de vértices para crear una arista.
                                if (vertice1 != None) and (vertice2 != None):
                                    aristas.append(Arista(vertice1, vertice2))
                        pass
                    sinRuta = False
                except FileNotFoundError:
                    print(Fore.RED + "El archivo no existe, por favor vuelve a intentarlo.\n")
                except IsADirectoryError:
                    print(Fore.RED + "La ruta introducida es un directorio, no un archivo. Por favor vuelve a intentarlo.\n")

                grafica = Grafica(vertices, aristas)

                if sinRuta == False and len(vertices) > 0 and len(aristas) > 0:
                    conjuntoInd = grafica.obténCjtoIndependiente(vertices[0])

                    print(Fore.RESET + "El conjunto independiente de la gráfica es:")

                    string = vertices[0].obtenerNombre()
                    for i in range(1, len(conjuntoInd)):
                        if conjuntoInd[i].obtenerNombre() != "\n":
                            string = string + ", " + conjuntoInd[i].obtenerNombre()

                    print(Fore.YELLOW + "{" + string + "}")
                    print(Fore.CYAN + "\n\n¿Qué deseas hacer ahora?")
                    print("\n1. Obtener un conjunto independiente de otra digráfica.")

                if len(vertices) == 0 and len(aristas) == 0 and sinRuta == False:
                    print(Fore.YELLOW + "Vaya! Parece que el archivo está vacío. Bueno fácil, el conjunto independiente es {" + "} ;)")

                    print(Fore.CYAN + "\n\nBueno, ¿Qué deseas hacer ahora?")
                    print("\n1. Obtener un conjunto independiente de otra digráfica.")