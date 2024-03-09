#1. Validar la edad de un usuario.

def validar_edad(edad):
    # La función validar_edad toma un parámetro 'edad' que representa la edad de una persona.

    assert edad >= 18, "La edad debe ser mayor o igual a 18 años"
    # La instrucción 'assert' es una afirmación que verifica si la condición proporcionada es verdadera.
    # En este caso, la condición es 'edad >= 18', lo que significa que la edad debe ser mayor o igual a 18.
    # Si la condición es falsa, se genera un AssertionError con el mensaje "La edad debe ser mayor o igual a 18 años".