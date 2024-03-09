#10)Genera los primeros 10 números de la serie Fibonacci.

# Definición de la función fibonacci_recursivo que calcula el término n de la serie Fibonacci de manera recursiva
def fibonacci_recursivo(n):
    # Si n es 0 o 1, devuelve n
    if n <= 1:
        return n
    else:
        # Si n es mayor que 1, calcula el término Fibonacci recurriendo a los dos términos anteriores
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Genera una lista de los primeros 10 términos de la serie Fibonacci usando una comprensión de listas
fibonacci = [fibonacci_recursivo(i) for i in range(10)]

# Imprime los primeros 10 números de la serie Fibonacci
print("Los primeros 10 números de la serie Fibonacci son:")
print(fibonacci)