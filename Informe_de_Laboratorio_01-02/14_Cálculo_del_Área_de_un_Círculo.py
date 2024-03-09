#14)Pide el radio de un círculo al usuario y calcula su área.

# Importa el módulo math, que contiene funciones matemáticas, incluyendo pi
import math

# Definición de la función calcular_area_circulo que calcula el área de un círculo dado su radio
def calcular_area_circulo(radio):
    # Calcula el área del círculo utilizando la fórmula π * radio^2
    area = math.pi * radio**2
    return area

# Solicita al usuario que ingrese el radio del círculo y lo convierte a un número de punto flotante
radio = float(input("Ingrese el radio del círculo: "))

# Llama a la función calcular_area_circulo con el radio ingresado por el usuario y almacena el resultado en area_circulo
area_circulo = calcular_area_circulo(radio)

# Imprime el área del círculo utilizando una cadena de formato
print(f"El área del círculo con radio {radio} es: {area_circulo}")