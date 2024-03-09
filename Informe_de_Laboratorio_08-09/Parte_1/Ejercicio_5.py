#5. Validar la igualdad de dos objetos.

def validar_igualdad(objeto1, objeto2):
    # La función validar_igualdad toma dos objetos como parámetros y verifica si son iguales.

    assert objeto1 == objeto2, "Los objetos no son iguales"
    # La instrucción 'assert' verifica si objeto1 es igual a objeto2.
    # Si los objetos no son iguales, se genera un AssertionError con el mensaje "Los objetos no son iguales".