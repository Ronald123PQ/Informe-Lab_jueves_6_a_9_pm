#3. Validar el rango de una calificación.

def validar_calificacion(calificacion):
    # La función validar_calificacion toma un parámetro 'calificacion' que representa una calificación numérica.

    assert 0 <= calificacion <= 10, "La calificación debe estar en el rango de 0 a 10"
    # La instrucción 'assert' verifica si la calificación está en el rango de 0 a 10.
    # Si la calificación no está en ese rango, se genera un AssertionError con el mensaje "La calificación debe estar en el rango de 0 a 10".