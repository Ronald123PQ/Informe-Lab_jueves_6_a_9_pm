# Ejercicio 2: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def calcular_estadisticas(matriz):
    # Define una función para calcular estadísticas de una matriz dada.

    # Calcula la media de los elementos de la matriz utilizando la función mean de NumPy.
    media = np.mean(matriz)

    # Calcula la mediana de los elementos de la matriz utilizando la función median de NumPy.
    mediana = np.median(matriz)

    # Calcula la desviación estándar de los elementos de la matriz utilizando la función std de NumPy.
    desviacion_estandar = np.std(matriz)

    # Retorna la media, mediana y desviación estándar calculadas.
    return media, mediana, desviacion_estandar

# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
filas = int(input("Ingrese el número de filas: "))

# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))

# Crea una matriz aleatoria de dimensiones (filas, columnas) utilizando NumPy.
mi_matriz = np.random.random((filas, columnas))

print("La matriz es:")
print(mi_matriz)
# Imprime la matriz generada.

# Llama a la función calcular_estadisticas para obtener la media, mediana y desviación estándar de la matriz.
media, mediana, desviacion_estandar = calcular_estadisticas(mi_matriz)

# Imprime la media, mediana y desviación estándar de la matriz.
print(f"La media de los elementos de la matriz es: {media}")
print(f"La mediana de los elementos de la matriz es: {mediana}")
print(f"La desviación estándar de los elementos de la matriz es: {desviacion_estandar}")