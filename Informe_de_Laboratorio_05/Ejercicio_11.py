# Ejercicio 11:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor.

def ordenar_numeros(conjunto_numeros):
    # Ordena los números en el conjunto y convierte el resultado en un conjunto nuevamente
    numeros_ordenados = sorted(conjunto_numeros)
    return set(numeros_ordenados)

# Conjunto de números de ejemplo
conjunto_numeros = {5, 3, 8, 1, 10, 2}

# Imprime el conjunto de números original
print("Conjunto de números:", conjunto_numeros)

# Llama a la función para ordenar los números en el conjunto
conjunto_ordenado = ordenar_numeros(conjunto_numeros)

# Imprime el conjunto de números ordenado
print("Conjunto ordenado:", conjunto_ordenado)