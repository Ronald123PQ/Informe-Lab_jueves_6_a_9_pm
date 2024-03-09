# Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.

# Definición de la función imprimir_pares que imprime todos los números pares menores o iguales a 100
def imprimir_pares(numero):
    # Verifica si el número es menor o igual a 100
    if numero <= 100:
        # Verifica si el número es par
        if numero % 2 == 0:
            # Si es par, imprime el número
            print(numero)
        # Llama a la función nuevamente con el siguiente número
        imprimir_pares(numero + 1)

# Llama a la función imprimir_pares con el número inicial 1
imprimir_pares(1)