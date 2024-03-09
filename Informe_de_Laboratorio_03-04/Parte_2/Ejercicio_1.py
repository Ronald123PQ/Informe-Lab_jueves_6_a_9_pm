# Ejercicio 1: Crea una matriz de números aleatorios de tamaño 100x100.

import random
# El módulo random que contiene funciones para generar números aleatorios.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

# Funcion crear_matriz_aleatoria para crear la matriz con la libreria numpy (opcion 1).
def crear_matriz_aleatoria_1(filas, columnas):

    matriz_aleatoria = np.random.random((filas, columnas))
    # Creamos una matriz de números aleatorios de tamaño 100x100
    return matriz_aleatoria

# Define una función llamada crear_matriz que genera una matriz con el módulo random (opcion 2)
def crear_matriz_2(filas, columnas):
    matriz = []  # Inicializa una lista vacía que contendrá la matriz.
    for _ in range(filas):  # Itera sobre el número de filas.
        fila = []  # Inicializa una lista vacía que representará una fila de la matriz.
        for _ in range(columnas):  # Itera sobre el número de columnas.
            fila.append(random.randint(0, 100))  # Agrega un número entero aleatorio entre 0 y 100 a la fila.
        matriz.append(fila)  # Agrega la fila a la matriz.
    return matriz  # Retorna la matriz completa.

# Define una función llamada imprimir_matriz que imprime la matriz en formato legible.
def imprimir_matriz(matriz):
    for fila in matriz:  # Itera sobre cada fila de la matriz.
        print(fila)  # Imprime la fila en la consola.

filas = 100  # Define el número de filas para la matriz.
columnas = 100  # Define el número de columnas para la matriz.

# Creamos una matriz de números aleatorios de tamaño 100x100, opcion 1.
matriz_100x100_1 = crear_matriz_aleatoria_1(filas, columnas)
# Imprimimos la matriz
print(matriz_100x100_1)

# Crea una matriz aleatoria con 100 filas y 100 columnas, opcion 2.
matriz_aleatoria_2 = crear_matriz_2(filas, columnas)
# Imprime la matriz aleatoria generada.
imprimir_matriz(matriz_aleatoria_2)