#6. Asegurar que un ciclo while se ejecuta al menos una vez.

def ciclo_con_al_menos_una_ejecucion():
    # La función ciclo_con_al_menos_una_ejecucion intenta ejecutar un ciclo al menos una vez.

    condicion = False
    # Se inicializa la variable condicion como False.

    while not condicion:
        # Se inicia un bucle while con la condición de que la variable condicion sea False.

        condicion = True
        # Se actualiza la variable condicion a True para que el bucle se ejecute al menos una vez.

    assert condicion, "El ciclo no se ejecutó al menos una vez"
    # Se utiliza la instrucción 'assert' para verificar si el ciclo se ejecutó al menos una vez.
    # Si la condición condicion es False, se genera un AssertionError con el mensaje "El ciclo no se ejecutó al menos una vez".