# Crear una lista vacía para guardar las calificaciones
calificaciones = []

print("Ingresa 8 calificaciones:")

# Pedir 8 calificaciones al usuario
for i in range(8):
    nota = float(input(f"Ingrese la calificación #{i + 1}: "))
    calificaciones.append(nota)

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Mostrar la lista y el promedio
print("\nCalificaciones ingresadas:")
print(calificaciones)

print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
