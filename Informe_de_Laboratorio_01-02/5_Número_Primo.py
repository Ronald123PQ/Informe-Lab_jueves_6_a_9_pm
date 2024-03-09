#5)Verifica si un número ingresado por el usuario es primo o no.

# Definición de la función es_primo que verifica si un número es primo
def es_primo(numero):
    # Verifica si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Verifica si el número es 2, que es primo
    elif numero == 2:
        return True
    # Verifica si el número es par, excepto por 2
    elif numero % 2 == 0:
        return False
    else:
        # Verifica la divisibilidad del número por los impares hasta la raíz cuadrada del número
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

# Solicita al usuario que ingrese un número y lo convierte a entero
numero = int(input("Ingrese un número: "))

# Comprueba si el número ingresado es primo utilizando la función es_primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")