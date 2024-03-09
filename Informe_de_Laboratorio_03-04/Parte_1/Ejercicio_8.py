# Ejercicio 8: Crea una matriz de matrices.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def crear_matriz_de_matrices(filas, columnas, dimension_matriz):
    # Define una función para crear una matriz de matrices dada su cantidad de filas, columnas y la dimensión de las matrices internas.
    matriz = np.empty((filas, columnas), dtype=object)
    # Crea una matriz vacía con la forma especificada por (filas, columnas) y tipo de dato objeto.
    # El tipo de dato objeto permite almacenar cualquier tipo de objeto, incluidas matrices de NumPy.
    for i in range(filas):
        for j in range(columnas):
            # Itera sobre las filas y columnas de la matriz.
            matriz[i, j] = np.random.random((dimension_matriz, dimension_matriz))
            # Asigna a la posición actual de la matriz una matriz aleatoria de dimensiones (dimension_matriz, dimension_matriz).
    return matriz
    # Retorna la matriz creada.

def imprimir_matriz_de_matrices(matriz):
    # Define una función para imprimir una matriz de matrices.
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            # Itera sobre las filas y columnas de la matriz.
            print(f"Matriz en posición ({i + 1}, {j + 1}):\n{matriz[i, j]}")
            # Imprime la matriz en la posición actual.
            print("-----")
            # Imprime un separador entre las matrices.
        print()
        # Imprime una línea en blanco entre las filas de la matriz principal.

filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.
dimension_matriz = int(input("Ingrese la dimensión de las matrices internas: "))
# Solicita al usuario que ingrese la dimensión de las matrices internas y lo convierte a un entero.

mi_matriz_de_matrices = crear_matriz_de_matrices(filas, columnas, dimension_matriz)
# Llama a la función crear_matriz_de_matrices para crear una matriz de matrices con las dimensiones especificadas.

print("La matriz creada es:")
# Imprime un mensaje indicando que se mostrará la matriz creada.
imprimir_matriz_de_matrices(mi_matriz_de_matrices)
# Llama a la función imprimir_matriz_de_matrices para mostrar la matriz de matrices creada.