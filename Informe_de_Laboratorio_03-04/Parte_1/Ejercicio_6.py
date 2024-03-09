# Ejercicio 6: Crea una matriz de números reales.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def crear_matriz(filas, columnas):
    # Define una función para crear una matriz dada su cantidad de filas y columnas.
    matriz = np.zeros((filas, columnas), dtype=float)
    # Crea una matriz de ceros con la forma especificada por (filas, columnas) y tipo de dato float.
    for i in range(filas):
        for j in range(columnas):
            # Itera sobre las filas y columnas de la matriz.
            valor = float(input(f"Ingrese el valor para la posición {i+1},{j+1}: "))
            # Solicita al usuario que ingrese el valor para la posición actual.
            matriz[i, j] = valor
            # Asigna el valor ingresado a la posición correspondiente en la matriz.
    return matriz
    # Retorna la matriz creada.

def imprimir_matriz(matriz):
    # Define una función para imprimir una matriz.
    print(matriz)
    # Imprime la matriz.

filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a entero.
columnas = int(input("Ingrese el número de columnas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a entero.

mi_matriz = crear_matriz(filas, columnas)
# Llama a la función crear_matriz para crear una matriz con el número de filas y columnas especificado.

print("La matriz creada es:")
# Imprime un mensaje indicando que se mostrará la matriz creada.
imprimir_matriz(mi_matriz)
# Llama a la función imprimir_matriz para mostrar la matriz creada.