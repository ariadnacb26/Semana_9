import random

# Crear lista con 10 números enteros aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]

# Listas para pares e impares
pares = []
impares = []

# Separar números pares e impares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar resultados
print("Lista original:")
print(numeros)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros impares:")
print(impares)
