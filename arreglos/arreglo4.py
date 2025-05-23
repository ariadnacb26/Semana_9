import os 
import random

CLEAR_COMMAND = "cls||clear"

participantes = list()
while True:
    os.system(CLEAR_COMMAND)
    os.system("color al")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar)")
    if nombre.lower() == 'fin':
        break 
    participantes.append(nombre.upper())

os.system(CLEAR_COMMAND)
print("Participantes registrados: ")
print(participantes)    
x = input("Presione 'ENTER' para continuar...")

#Crear un contador de 10 segundos 
cont = 10
while cont > 0:
    os.system(CLEAR_COMMAND)
    print(cont)
    time.sleep(1)
    cont 

fin = len(participantes) - 1
ganador = random.rendint (0, fin)
print("El ganador es: ", participantes {ganador})
    