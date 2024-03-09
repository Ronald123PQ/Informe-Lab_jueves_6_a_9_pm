#7. Asegurar que una función retorna un valor específico.

def funcion_retorna_valor_especifico():
    # La función funcion_retorna_valor_especifico llama a la función hacer_algo() y verifica si retorna el valor esperado.

    resultado = hacer_algo()
    # Se llama a la función hacer_algo() y se guarda el resultado en la variable resultado.

    assert resultado == 42, "La función no retornó el valor esperado"
    # Se utiliza la instrucción 'assert' para verificar si el resultado de hacer_algo() es igual a 42.
    # Si el resultado es diferente de 42, se genera un AssertionError con el mensaje "La función no retornó el valor esperado".