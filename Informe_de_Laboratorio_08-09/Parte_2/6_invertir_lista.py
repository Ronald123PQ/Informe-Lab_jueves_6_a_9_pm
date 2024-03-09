#15. Implementa una función que invierta el orden de una lista enlazada simple.

class ListaEnlazada:
    # Clase que representa una lista enlazada.

    def invertir(self):
        # Método para invertir la lista enlazada.
        anterior = None
        # Se inicializa el nodo anterior como None, ya que será el último nodo en la lista invertida.
        actual = self.cabeza
        # Se comienza desde la cabeza de la lista.

        while actual:
            # Mientras haya un nodo actual en la lista.
            siguiente_nodo = actual.siguiente
            # Se guarda el siguiente nodo antes de invertir el enlace.
            actual.siguiente = anterior
            # Se invierte el enlace del nodo actual para que apunte al nodo anterior.
            anterior = actual
            # Se actualiza el nodo anterior al nodo actual.
            actual = siguiente_nodo
            # Se avanza al siguiente nodo en la lista original.

        self.cabeza = anterior
        # Al finalizar, la cabeza de la lista se establece como el último nodo invertido, que ahora es el primero.