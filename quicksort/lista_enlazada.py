from nodo import Nodo

# Clase para la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    # Método para agregar un elemento al final de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para convertir la lista enlazada a una lista Python normal
    def convertir_a_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista

    # Método para cargar desde una lista de Python
    def cargar_desde_lista(self, lista):
        self.cabeza = None
        for item in lista:
            self.agregar(item)

    # Método para mostrar los elementos de la lista enlazada
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()