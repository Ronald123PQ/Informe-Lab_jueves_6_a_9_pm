#2. Verificar el tipo de dato de una variable.

def verificar_tipo(variable):
    # La función verificar_tipo toma un parámetro 'variable' que representa una variable cuyo tipo se desea verificar.

    assert isinstance(variable, int), "La variable debe ser de tipo entero"
    # La instrucción 'assert' verifica si 'variable' es una instancia de la clase 'int', es decir, si es de tipo entero.
    # Si 'variable' no es de tipo entero, se genera un AssertionError con el mensaje "La variable debe ser de tipo entero".