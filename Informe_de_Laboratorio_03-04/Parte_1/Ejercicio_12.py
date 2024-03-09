# Ejercicio 12: Calcula la media de los elementos de una matriz.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def calcular_media(matriz):
    # Define una función para calcular la media de los elementos de una matriz.

    media = np.mean(matriz)
    # Calcula la media de los elementos de la matriz utilizando la función mean de NumPy.
    # La función mean calcula la media aritmética de los elementos de la matriz.
    return media
    # Retorna el valor de la media calculada.

filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.

mi_matriz = np.random.random((filas, columnas))
# Crea una matriz aleatoria de dimensiones (filas, columnas) utilizando NumPy.

print("La matriz es:")
print(mi_matriz)
# Imprime la matriz generada.

media_matriz = calcular_media(mi_matriz)
# Llama a la función calcular_media para obtener la media de los elementos de la matriz.

print(f"La media de los elementos de la matriz es: {media_matriz}")
# Imprime el valor de la media de la matriz.