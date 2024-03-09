#11)Ordena una lista de números ingresados por el usuario de menor a mayor.

# Definición de la función ordenar_lista_menor_a_mayor que ordena una lista de menor a mayor
def ordenar_lista_menor_a_mayor(lista):
    # Utiliza la función sorted() para ordenar la lista y devuelve el resultado
    return sorted(lista)

# Solicitar al usuario que ingrese una lista de números separados por espacios
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
lista_numeros = [float(numero) for numero in entrada_usuario.split()]

# Llamar a la función para ordenar la lista de menor a mayor
lista_ordenada = ordenar_lista_menor_a_mayor(lista_numeros)

# Mostrar la lista ordenada
print("Lista ordenada de menor a mayor:")
print(lista_ordenada)