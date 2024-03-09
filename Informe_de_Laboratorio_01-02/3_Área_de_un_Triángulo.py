#3)Pide la base y la altura de un triángulo al usuario y calcula su área.

# Definición de la función calcular_area_rectangulo que calcula el área del rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

# Solicitar al usuario que ingrese la base del rectángulo y convertir el valor a flotante
base = float(input("Ingrese la base del rectángulo: "))
# Solicitar al usuario que ingrese la altura del rectángulo y convertir el valor a flotante
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el área del rectángulo utilizando la función calcular_area_rectangulo
area = calcular_area_rectangulo(base, altura)

# Imprimir el área del rectángulo
print(f"El área del rectángulo es: {area}")