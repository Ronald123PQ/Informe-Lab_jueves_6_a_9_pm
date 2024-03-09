# Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.

# Definición de la función imprimir_piramide_invertida que imprime una pirámide invertida numérica
def imprimir_piramide_invertida(n, actual=1):
    # Verifica si el valor actual es menor o igual que n
    if actual <= n:
        # Imprime espacios en blanco antes de los números
        print(" " * (actual - 1), end="")

        # Imprime números descendentes desde el nivel actual hasta 1
        for i in range(actual, 0, -1):
            print(i, end=" ")

        # Imprime un salto de línea para pasar a la siguiente fila de la pirámide invertida
        print()

        # Llama recursivamente a la función con el siguiente nivel de la pirámide invertida
        imprimir_piramide_invertida(n, actual + 1)

# Solicita al usuario que ingrese un número entero
m = int(input("Ingrese número: "))

# Llama a la función imprimir_piramide_invertida con el número ingresado por el usuario
imprimir_piramide_invertida(m)