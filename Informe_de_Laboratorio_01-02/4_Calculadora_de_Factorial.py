#4)Crea una función que calcule la factorial de un número.

# Definición de la función calcular_factorial que calcula el factorial de un número
def calcular_factorial(numero):
    # Maneja el caso en que el número sea negativo
    if numero < 0:
        return "Error"
    # Casos base: el factorial de 0 y 1 es 1
    elif numero == 0 or numero == 1:
        return 1
    else:
        # Para números mayores que 1, calcula el factorial utilizando recursión
        factorial = numero * calcular_factorial(numero - 1)
        return factorial

# Solicita al usuario que ingrese un número y lo convierte a entero
numero = int(input("Ingrese un número: "))

# Calcula el factorial del número ingresado por el usuario y lo imprime
print("El factorial de", numero, "es:", calcular_factorial(numero))