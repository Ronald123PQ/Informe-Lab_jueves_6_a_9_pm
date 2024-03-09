#12)Verifica si una palabra ingresada por el usuario es un palíndromo.

# Definición de la función es_palindromo que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    # Convierte la palabra a minúsculas para hacer la comparación sin distinguir entre mayúsculas y minúsculas
    palabra = palabra.lower()

    # Comprueba si la palabra es igual a su inversa
    # Utiliza la técnica de slicing para invertir la palabra
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Llamar a la función para verificar si es un palíndromo
if es_palindromo(palabra_ingresada):
    print(f"{palabra_ingresada} es un palíndromo.")
else:
    print(f"{palabra_ingresada} no es un palíndromo.")