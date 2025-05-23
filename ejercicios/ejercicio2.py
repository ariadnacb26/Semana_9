# Crear una lista vacía para guardar los números
numeros = []

print("Ingresa 10 números:")

# Solicitar 10 números al usuario
for i in range(10):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    numeros.append(numero)

# Calcular la suma total de los elementos
suma_total = sum(numeros)

# Mostrar los resultados
print("\nLista ingresada:")
print(numeros)

print(f"\nLa suma total de los elementos es: {suma_total}")
