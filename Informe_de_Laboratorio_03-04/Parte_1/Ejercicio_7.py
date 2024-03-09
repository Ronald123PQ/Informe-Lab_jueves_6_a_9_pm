# Ejercicio 7: Crea una matriz de números complejos.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def crear_matriz_compleja(filas, columnas):
    # Define una función para crear una matriz compleja dada su cantidad de filas y columnas.
    matriz = np.zeros((filas, columnas), dtype=complex)
    # Crea una matriz de ceros con la forma especificada por (filas, columnas) y tipo de dato complejo.
    for i in range(filas):
        for j in range(columnas):
            # Itera sobre las filas y columnas de la matriz.
            real = float(input(f"Ingrese la parte real para la posición ({i + 1}, {j + 1}): "))
            # Solicita al usuario que ingrese la parte real para la posición actual.
            imaginaria = float(input(f"Ingrese la parte imaginaria para la posición ({i + 1}, {j + 1}): "))
            # Solicita al usuario que ingrese la parte imaginaria para la posición actual.
            matriz[i, j] = complex(real, imaginaria)
            # Asigna el número complejo creado con la parte real e imaginaria ingresada a la posición correspondiente en la matriz.
    return matriz
    # Retorna la matriz creada.

def imprimir_matriz_compleja(matriz):
    # Define una función para imprimir una matriz compleja.
    print(matriz)
    # Imprime la matriz.

filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.

mi_matriz_compleja = crear_matriz_compleja(filas, columnas)
# Llama a la función crear_matriz_compleja para crear una matriz compleja con el número de filas y columnas especificado.

print("La matriz creada es:")
# Imprime un mensaje indicando que se mostrará la matriz creada.
imprimir_matriz_compleja(mi_matriz_compleja)
# Llama a la función imprimir_matriz_compleja para mostrar la matriz creada.