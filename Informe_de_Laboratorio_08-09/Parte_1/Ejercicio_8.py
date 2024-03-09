#8. Validar el estado de una variable después de una operación.

variable = 5
# Se inicializa la variable 'variable' con el valor 5.

variable += 3
# Se incrementa el valor de 'variable' en 3 unidades, ahora 'variable' tiene el valor 8.

assert variable == 8, "La variable no tiene el valor esperado después de la operación"
# Se utiliza la instrucción 'assert' para verificar si el valor de 'variable' es igual a 8.
# Si el valor de 'variable' es diferente de 8, se genera un AssertionError con el mensaje "La variable no tiene el valor esperado después de la operación".