#15)Toma un número entero y calcula la suma de sus dígitos.

# Definición de la función suma_digitos que calcula la suma de los dígitos de un número entero
def suma_digitos(numero):
    suma = 0
    # Mientras el número sea diferente de 0, se suman los dígitos del número
    while numero != 0:
        # Se obtiene el último dígito del número y se suma a la variable suma
        suma += numero % 10
        # Se elimina el último dígito del número dividiendo entre 10 y tomando la parte entera
        numero //= 10
    return suma

# Se solicita al usuario que ingrese un número entero y se convierte a entero
numero_entero = int(input("Ingrese un número entero: "))

# Se llama a la función suma_digitos con el número entero ingresado por el usuario
resultado_suma = suma_digitos(numero_entero)

# Se imprime el resultado de la suma de los dígitos del número entero
print(f"La suma de los dígitos de {numero_entero} es: {resultado_suma}")