# Ejercicio 14:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no están duplicados.

def numeros_sin_duplicados(numeros):
    # Conjunto para almacenar los números sin duplicados
    numeros_sin_duplicados = set()
    # Conjunto para almacenar los números vistos
    numeros_vistos = set()

    # Itera a través de cada número en la secuencia
    for num in numeros:
        # Verifica si el número no ha sido visto
        if num not in numeros_vistos:
            # Si no ha sido visto, lo agrega al conjunto de números sin duplicados
            numeros_sin_duplicados.add(num)
            # Agrega el número al conjunto de números vistos
            numeros_vistos.add(num)
        else:
            # Si el número ya ha sido visto, lo elimina del conjunto de números sin duplicados (si está presente)
            numeros_sin_duplicados.discard(num)

    # Devuelve el conjunto de números sin duplicados
    return numeros_sin_duplicados

# Conjunto de números de ejemplo con duplicados
conjunto_numeros = {1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9}
# Llama a la función para encontrar los números sin duplicados en el conjunto
resultado = numeros_sin_duplicados(conjunto_numeros)
# Imprime los números sin duplicados
print("Números sin duplicados:", resultado)