# Ejercicio 5: Escribe una función recursiva que imprima la tabla de multiplicar del n.

def imprimir_tabla_multiplicar(n, multiplicador=1):
    # Define una función que imprime la tabla de multiplicar para un número dado.
    # 'n' es el número cuya tabla se imprimirá y 'multiplicador' es el valor con el que se multiplica, iniciando en 1 por defecto.

    if multiplicador <= 10:
        # Verifica si el multiplicador es menor o igual a 10 para imprimir solo hasta la tabla del 10.

        resultado = n * multiplicador
        # Calcula el resultado de la multiplicación.

        print(n, "x", multiplicador, "=", resultado)
        # Imprime la expresión de la multiplicación y su resultado.

        # Llamada recursiva con el siguiente multiplicador.
        imprimir_tabla_multiplicar(n, multiplicador + 1)

m = int(input("Ingrese número: "))
# Solicita al usuario que ingrese un número entero y lo convierte a entero, asignándolo a la variable 'm'.

imprimir_tabla_multiplicar(m)
# Llama a la función 'imprimir_tabla_multiplicar' con el número ingresado por el usuario como argumento para imprimir la tabla de multiplicar.