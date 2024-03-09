#2)Solicita un número al usuario y determina si es par o impar.

# Definición de la función es_par_o_impar que determina si un número es par o impar
def es_par_o_impar(numero):
    # Verifica si el número es divisible por 2 sin dejar residuo
    if numero % 2 == 0:
        # Si el residuo es cero, el número es par
        return "par"
    else:
        # Si el residuo no es cero, el número es impar
        return "impar"

# Solicita al usuario que ingrese un número y lo convierte a entero
numero = int(input("Ingrese un número: "))

# Llama a la función es_par_o_impar con el número ingresado por el usuario y almacena el resultado
resultado = es_par_o_impar(numero)

# Imprime el resultado
print(f"El número {numero} es {resultado}.")