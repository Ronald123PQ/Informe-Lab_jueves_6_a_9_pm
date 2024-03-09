# Ejercicio 9: Accede al elemento central de una matriz.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def acceder_elemento_central(matriz):
    # Define una función para acceder al elemento central de una matriz dada.

    if matriz.shape[0] % 2 == 1 and matriz.shape[1] % 2 == 1:
        # Verifica si tanto el número de filas como el número de columnas son impares.
        fila_central = matriz.shape[0] // 2
        # Calcula el índice de la fila central.
        columna_central = matriz.shape[1] // 2
        # Calcula el índice de la columna central.
        elemento_central = matriz[fila_central, columna_central]
        # Accede al elemento central de la matriz.
        return elemento_central
        # Retorna el elemento central si la matriz tiene un número impar de filas y columnas.
    else:
        return None
        # Retorna None si la matriz no tiene un número impar de filas y columnas.

filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.

mi_matriz = np.random.random((filas, columnas))
# Crea una matriz aleatoria de dimensiones (filas, columnas) utilizando NumPy.

elemento_central = acceder_elemento_central(mi_matriz)
# Llama a la función acceder_elemento_central para obtener el elemento central de la matriz.

if elemento_central is not None:
    # Verifica si el elemento central no es None.
    print(f"El elemento central de la matriz es: {elemento_central}")
    # Imprime el elemento central de la matriz.
else:
    print("La matriz no tiene un número impar de filas y columnas.")
    # Imprime un mensaje indicando que la matriz no tiene un número impar de filas y columnas.