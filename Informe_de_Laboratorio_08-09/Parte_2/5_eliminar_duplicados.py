#14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.

class ListaEnlazada:
    # Clase que representa una lista enlazada.

    def eliminar_duplicados(self):
        # Método para eliminar nodos duplicados en la lista enlazada.

        actual = self.cabeza
        # Se comienza desde la cabeza de la lista.

        while actual:
            corredor = actual
            # Se define un corredor para recorrer la lista desde el nodo actual.

            while corredor.siguiente:
                # Mientras haya un siguiente nodo en la lista.
                if corredor.siguiente.dato == actual.dato:
                    # Si el dato del siguiente nodo es igual al dato del nodo actual.
                    corredor.siguiente = corredor.siguiente.siguiente
                    # Se salta el nodo siguiente, eliminándolo de la lista.
                else:
                    corredor = corredor.siguiente
                    # Si no hay duplicado, se avanza al siguiente nodo.
            actual = actual.siguiente
            # Se avanza al siguiente nodo de la lista.