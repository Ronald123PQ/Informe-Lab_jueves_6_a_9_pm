# Ejercicio 12:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de mayor a menor.

def numeros_ordenados_de_mayor_a_menor(numeros):
    # Ordena los números en el conjunto en orden descendente y los convierte en una lista
    numeros_ordenados = sorted(numeros, reverse=True)
    return numeros_ordenados

# Conjunto de números de ejemplo
conjunto_numeros = {5, 2, 8, 1, 9, 3, 6, 15, 11}

# Llama a la función para ordenar los números de mayor a menor
resultado = numeros_ordenados_de_mayor_a_menor(conjunto_numeros)

# Imprime los números ordenados de mayor a menor
print("Números ordenados de mayor a menor:")
print(resultado)