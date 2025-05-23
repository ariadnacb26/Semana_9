#Cargar una lista manualmente
#✓ Crea una lista con 10 números enteros y muestra el contenido
# Paso 1: Crear una lista manualmente con 10 números enteros
numeros = [12, 45, 7, 89, 23, 56, 78, 34, 90, 11]

# Paso 2: Mostrar un mensaje indicando lo que va a hacer el programa
print("Este programa contiene una lista de 10 números enteros.")
print("Mostraremos los números uno por uno:\n")

# Paso 3: Recorrer la lista y mostrar cada número por separado
for i in range(len(numeros)):
    print(f"Número en la posición {i}: {numeros[i]}")

# Paso 4: Mostrar la lista completa al final
print("\nLista completa:")
print(numeros)

