# Ejercicio 05:Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el primer conjunto pero no en el segundo.

def diferencia_entre_conjuntos(conjunto1, conjunto2):
    # Calcula la diferencia entre los conjuntos utilizando el operador de resta
    diferencia = conjunto1 - conjunto2
    return diferencia

# Conjuntos de ejemplo
conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {4, 5, 6, 7, 8}

# Llama a la función para calcular la diferencia entre los conjuntos A y B
resultado = diferencia_entre_conjuntos(conjuntoA, conjuntoB)

# Imprime los conjuntos y la diferencia entre ellos
print("Conjunto A:", conjuntoA)
print("Conjunto B:", conjuntoB)
print("Diferencia (A - B):", resultado)