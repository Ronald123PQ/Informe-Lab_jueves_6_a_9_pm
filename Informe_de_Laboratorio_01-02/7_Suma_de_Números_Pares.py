#7)Calcula la suma de los números pares en un rango especificado por el usuario.

# Definición de la función suma_numeros_pares que calcula la suma de los números pares en un rango dado
def suma_numeros_pares(rango_inicio, rango_fin):
    suma = 0
    # Itera a través de cada número en el rango especificado
    for numero in range(rango_inicio, rango_fin + 1):
        # Verifica si el número es par (es divisible por 2)
        if numero % 2 == 0:
            # Si el número es par, lo suma al total
            suma = numero + suma
    return suma

# Solicita al usuario que ingrese el inicio y el final del rango y los convierte a enteros
inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el final del rango: "))

# Llama a la función suma_numeros_pares con el inicio y fin del rango especificado por el usuario
resultado_suma = suma_numeros_pares(inicio, fin)

# Imprime el resultado de la suma de los números pares en el rango especificado
print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {resultado_suma}")