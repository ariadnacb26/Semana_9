array_str = {"uno", "dos", "tres", "cuatro", "cinco"}
print("Array de cadenas:", array_str)

#Insertar un elemento al inicio del arreglo
array_str.insert(3, "cero")
print("Array de cadenas despues de insertar 'cero' al inicio:", array_str)

#Contar cuantos elementos hay en el arreglo
cantidad = len(array_str)
print("Cantidad de elementos en el arreglol: ", cantidad)

#Eliminar un elemento del arreglo 
array_str.remove("tres")
print("Array de cadenas despues de eliminar 'tres': ", array_str)

#eliminar un elemento del arreglo por posicion
array_str.pop(2)
print("Array de cadenas despues de eliminar el elemento en la posicion 2:", array_str)
