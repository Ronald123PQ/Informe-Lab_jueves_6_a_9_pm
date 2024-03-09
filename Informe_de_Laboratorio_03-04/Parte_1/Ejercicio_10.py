# Ejercicio 10: Suma dos matrices de diferentes tamaños.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def sumar_matrices(matriz1, matriz2):
    # Define una función para sumar dos matrices.

    if matriz1.shape == matriz2.shape:
        # Verifica si las dimensiones de ambas matrices son iguales.
        suma = matriz1 + matriz2
        # Realiza la suma de las dos matrices elemento a elemento.
        return suma
        # Retorna la matriz resultante de la suma.
    else:
        return None
        # Retorna None si las dimensiones de las matrices no son iguales.

filas_matriz1 = int(input("Ingrese el número de filas para la Matriz 1: "))
# Solicita al usuario que ingrese el número de filas para la matriz 1 y lo convierte a un entero.
columnas_matriz1 = int(input("Ingrese el número de columnas para la Matriz 1: "))
# Solicita al usuario que ingrese el número de columnas para la matriz 1 y lo convierte a un entero.
filas_matriz2 = int(input("Ingrese el número de filas para la Matriz 2: "))
# Solicita al usuario que ingrese el número de filas para la matriz 2 y lo convierte a un entero.
columnas_matriz2 = int(input("Ingrese el número de columnas para la Matriz 2: "))
# Solicita al usuario que ingrese el número de columnas para la matriz 2 y lo convierte a un entero.

matriz1 = np.random.random((filas_matriz1, columnas_matriz1))
# Crea una matriz aleatoria de dimensiones (filas_matriz1, columnas_matriz1) utilizando NumPy.
matriz2 = np.random.random((filas_matriz2, columnas_matriz2))
# Crea una matriz aleatoria de dimensiones (filas_matriz2, columnas_matriz2) utilizando NumPy.

print("Matriz 1:")
print(matriz1)
# Imprime la matriz 1.
print("Matriz 2:")
print(matriz2)
# Imprime la matriz 2.

resultado_suma = sumar_matrices(matriz1, matriz2)
# Llama a la función sumar_matrices para sumar las matrices.

if resultado_suma is not None:
    # Verifica si la suma de las matrices no es None.
    print("La suma de las matrices es:")
    print(resultado_suma)
    # Imprime la matriz resultante de la suma.
else:
    print("Las matrices no tienen dimensiones compatibles para sumar")
    # Imprime un mensaje indicando que las matrices no tienen dimensiones compatibles para sumar.