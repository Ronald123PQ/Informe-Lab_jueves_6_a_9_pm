#13. Implementa una función que concatene dos listas enlazadas simples.

class ListaEnlazada:
    # Clase que representa una lista enlazada.

    def __init__(self):
        # Constructor que inicializa una lista enlazada vacía.
        self.cabeza = None
        # El atributo 'cabeza' apunta al primer nodo de la lista.0

    def concatenar_listas(lista1, lista2):
      # Función para concatenar dos listas enlazadas.
      if not lista1.cabeza:
          # Si la primera lista está vacía, se devuelve la segunda lista.
          return lista2
      if not lista2.cabeza:
          # Si la segunda lista está vacía, se devuelve la primera lista.
          return lista1

      actual = lista1.cabeza
      while actual.siguiente:
          # Se recorre la primera lista hasta el último nodo.
          actual = actual.siguiente
      actual.siguiente = lista2.cabeza
      # Se establece el siguiente del último nodo de la primera lista al primer nodo de la segunda lista.
      return lista1