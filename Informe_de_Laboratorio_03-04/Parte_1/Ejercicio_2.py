# Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.

# Definición de la función suma_recursiva que calcula la suma recursiva de los números enteros desde 1 hasta n
def suma_recursiva(n):
    # Caso base: Si n es igual a 1, devuelve 1
    if n == 1:
        return 1
    else:
        # Caso recursivo: Calcula la suma recursiva desde 1 hasta n - 1 y le suma n
        resultado = n + suma_recursiva(n - 1)
        # Imprime el resultado parcial de la suma hasta el número n
        print("Suma hasta", n, ":", resultado)
        return resultado

# Solicita al usuario que ingrese un número entero
m = int(input("Ingrese número: "))

# Llama a la función suma_recursiva con el número ingresado por el usuario
resultado_total = suma_recursiva(m)

# Imprime la suma total de los números enteros desde 1 hasta el número ingresado por el usuario
print(f"Suma total: {resultado_total}")