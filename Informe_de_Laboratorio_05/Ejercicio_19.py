# Ejercicio 19:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados.

def numeros_ordenados_sin_duplicados(conjunto_numeros):
    # Convierte el conjunto de números en un conjunto para eliminar duplicados y luego lo convierte en una lista
    numeros_ordenados = sorted(set(conjunto_numeros))
    # Convierte la lista ordenada en un conjunto y la devuelve
    return set(numeros_ordenados)

# Conjunto de números con duplicados
conjunto_de_numeros = {5, 3, 8, 1, 10, 2, 5, 8, 2}
# Llama a la función para obtener el conjunto ordenado sin duplicados
conjunto_ordenado_sin_duplicados = numeros_ordenados_sin_duplicados(conjunto_de_numeros)

print("Conjunto de números:", conjunto_de_numeros)
print("Conjunto ordenado sin duplicados:", conjunto_ordenado_sin_duplicados)