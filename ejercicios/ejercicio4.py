# Lista de palabras predefinida
palabras = ["manzana", "banana", "pera", "uva", "naranja", "sandía", "melón"]

# Mostrar la lista
print("Lista de palabras:")
print(palabras)

# Solicitar al usuario una palabra
buscada = input("\nIngresa una palabra para buscar en la lista: ").lower()

# Verificar si la palabra está en la lista
if buscada in palabras:
    print(f"La palabra '{buscada}' SÍ está en la lista.")
else:
    print(f"La palabra '{buscada}' NO está en la lista.")
