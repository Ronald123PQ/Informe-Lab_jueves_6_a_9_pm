#4. Asegurar que una lista no esté vacía.

def asegurar_lista_no_vacia(lista):
    # La función asegurar_lista_no_vacia toma un parámetro 'lista' que representa una lista.

    assert len(lista) > 0, "La lista no debe estar vacía"
    # La instrucción 'assert' verifica si la longitud de la lista es mayor que cero.
    # Si la lista está vacía (longitud igual a cero), se genera un AssertionError con el mensaje "La lista no debe estar vacía".