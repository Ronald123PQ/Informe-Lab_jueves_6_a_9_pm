#10. Desarrollar el código de buscar nodo en la lista enlazada simple.

class Nodo:
# Se define la clase Nodo, que representa un nodo individual en una lista enlazada.
    def __init__(self, dato):
        self.dato = dato
        # Se define el atributo 'dato' para almacenar el valor del nodo.
        self.siguiente = None
        # Se establece el atributo 'siguiente' para apuntar al siguiente nodo en la lista. Inicialmente se establece en None.

class ListaEnlazada:
# Se define la clase ListaEnlazada, que representa la lista enlazada en su conjunto.
    def __init__(self):
        self.cabeza = None
        # Se define el atributo 'cabeza' para apuntar al primer nodo de la lista. Inicialmente se establece en None.

    def buscar(self, clave):
        actual = self.cabeza
        # Se inicializa el nodo 'actual' con la cabeza de la lista.
        while actual is not None:
          # Se itera mientras 'actual' no sea None, es decir, mientras haya nodos en la lista.
            if actual.dato == clave:  # Se compara el dato del nodo actual con la clave buscada.
                return True
                # Si se encuentra la clave en el nodo actual, se devuelve True.
            actual = actual.siguiente  # Se avanza al siguiente nodo de la lista.
        return False
        # Si se recorre toda la lista y no se encuentra la clave, se devuelve False.