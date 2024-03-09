#12. Crea una función que devuelva la longitud de una lista enlazada simple.

class ListaEnlazada:
    # Se define la clase ListaEnlazada, que representa una lista enlazada.

    def longitud(self):
        # Método para calcular la longitud de la lista enlazada.
        contador = 0  # Se inicializa el contador en 0.
        actual = self.cabeza  # Se comienza desde el primer nodo de la lista.
        while actual:
            # Mientras el nodo actual no sea None (es decir, mientras haya nodos en la lista).
            contador += 1
            # Se incrementa el contador en 1 por cada nodo visitado.
            actual = actual.siguiente
            # Se avanza al siguiente nodo de la lista.
        return contador
        # Se devuelve el contador, que representa la longitud de la lista enlazada.