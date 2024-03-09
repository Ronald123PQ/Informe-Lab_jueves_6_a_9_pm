#1)Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario.

# Definición de la función para sumar dos números
def suma(a, b):
    return a + b

# Definición de la función para restar dos números
def resta(a, b):
    return a - b

# Definición de la función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Definición de la función para dividir dos números
def division(a, b):
    # Verifica si el divisor no es cero para evitar la división por cero
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Solicitar al usuario que ingrese el primer número
numero1 = float(input("Ingrese el primer número: "))
# Solicitar al usuario que ingrese el segundo número
numero2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones aritméticas usando las funciones definidas
resultado_suma = suma(numero1, numero2)
resultado_resta = resta(numero1, numero2)
resultado_multiplicacion = multiplicacion(numero1, numero2)
resultado_division = division(numero1, numero2)

# Imprimir los resultados de las operaciones
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)