# Ejercicio 3: Escribe una función que encuentre el elemento máximo de una matriz.

# Definición de la función encontrar_maximo que encuentra el elemento máximo de una matriz
def encontrar_maximo(matriz):
    maximo = float('-inf')  # Inicializa el valor máximo como el menor número posible

    for fila in matriz:  # Itera sobre cada fila en la matriz
        for elemento in fila:  # Itera sobre cada elemento en la fila
            if elemento > maximo:  # Comprueba si el elemento actual es mayor que el máximo actual
                maximo = elemento  # Si es así, actualiza el valor máximo

    return maximo  # Devuelve el valor máximo encontrado en la matriz