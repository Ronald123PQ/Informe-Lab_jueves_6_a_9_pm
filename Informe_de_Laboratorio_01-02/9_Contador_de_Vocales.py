#9)Cuenta el número de vocales en una cadena de texto.

# Definición de la función contar_vocales que cuenta el número de vocales en una cadena de texto
def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para contar las vocales sin distinción de mayúsculas o minúsculas
    cadena = cadena.lower()

    # Inicializar el contador de vocales
    contador_vocales = 0

    # Definir un conjunto de vocales para verificar la pertenencia
    vocales = set("aeiou")

    # Contar el número de vocales en la cadena
    for caracter in cadena:
        if caracter in vocales:
            contador_vocales += 1

    return contador_vocales

# Solicitar al usuario que ingrese una cadena de texto
cadena_texto = input("Ingrese una cadena de texto: ")

# Llamar a la función para contar las vocales en la cadena ingresada por el usuario
numero_vocales = contar_vocales(cadena_texto)

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {numero_vocales}")