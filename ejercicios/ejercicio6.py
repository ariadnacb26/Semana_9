# Crear una lista vacía
numeros = []

print("Ingresa 10 números:")

# Pedir 10 números al usuario
for i in range(10):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    numeros.append(numero)

# Mostrar la lista original
print("\nLista original:")
print(numeros)

# Invertir la lista usando slicing
lista_invertida = numeros[::-1]

# Mostrar la lista invertida
print("\nLista en orden inverso:")
print(lista_invertida)
