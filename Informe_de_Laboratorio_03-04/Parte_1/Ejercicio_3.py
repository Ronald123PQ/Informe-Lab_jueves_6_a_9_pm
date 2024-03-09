# Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.

# Definición de la función imprimir_piramide que imprime una pirámide numérica
def imprimir_piramide(n, actual=1):
    # Verifica si el valor actual es menor o igual que n
    if actual <= n:
        # Imprime espacios en blanco antes de los números
        print(" " * (n - actual), end=" ")

        # Imprime números ascendentes
        for i in range(1, actual + 1):
            print(i, end=" ")

        # Imprime números descendentes
        for i in range(actual - 1, 0, -1):
            print(i, end=" ")

        # Imprime un salto de línea para pasar a la siguiente fila de la pirámide
        print()

        # Llama recursivamente a la función con el siguiente nivel de la pirámide
        imprimir_piramide(n, actual + 1)

# Solicita al usuario que ingrese un número entero
m = int(input("Ingrese número: "))

# Llama a la función imprimir_piramide con el número ingresado por el usuario
imprimir_piramide(m)