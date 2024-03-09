#13)Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

# Definición de la función generar_tabla_multiplicar que imprime la tabla de multiplicar de un número dado
def generar_tabla_multiplicar(numero):
    # Imprime un encabezado que indica de qué número se está generando la tabla de multiplicar
    print(f"Tabla de multiplicar del {numero}:")

    # Itera sobre los números del 1 al 10 (inclusive)
    for i in range(1, 11):
        # Calcula el resultado de la multiplicación del número dado por el número actual del bucle
        resultado = numero * i

        # Imprime la expresión de la multiplicación y su resultado
        print(f"{numero} x {i} = {resultado}")

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Llamar a la función para generar la tabla de multiplicar
generar_tabla_multiplicar(numero_ingresado)