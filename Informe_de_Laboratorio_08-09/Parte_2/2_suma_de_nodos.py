#11. Implementa una función que sume todos los nodos de una lista enlazada simple.

class ListaEnlazada:
    # Se define la clase ListaEnlazada, que representa una lista enlazada.

    def sumar_nodos(self):
        # Método para sumar los valores de los nodos en la lista.
        total = 0  # Se inicializa la variable total en 0.
        actual = self.cabeza  # Se comienza desde el primer nodo de la lista.
        while actual:
            # Mientras el nodo actual no sea None (es decir, mientras haya nodos en la lista).
            total += actual.dato
            # Se suma el valor del nodo actual al total.
            actual = actual.siguiente
            # Se avanza al siguiente nodo de la lista.
        return total
        # Se devuelve la suma total de los valores de los nodos en la lista.