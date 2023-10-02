#Listas Creacion
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mezclada = [1, "dos", 3.0, True]

#Acceso a elementos de la lista:
fruta = frutas[0]  # Acceso al primer elemento, "manzana"
ultimo_numero = numeros[-1]  # Acceso al último elemento, 5

print(fruta)
print(ultimo_numero)

#Modificación de elementos de la lista
frutas[1] = "pera"  # Cambio de "banana" a "pera"
numeros.append(6)  # Agrega un elemento al final de la lista

print(frutas)
print(numeros)

#Longitud de la lista
cantidad_frutas = len(frutas)  # Devuelve 3
print(cantidad_frutas)

#Obtener parte de la lista
sublista = numeros[1:4]  # Obtiene [2, 3, 4]

#Concatenar dos listas
lista_combinada = numeros + frutas  # [1, 2, 3, 4, 5, "manzana", "banana", "naranja"]

#Eliminacion de elementos de la lista
del frutas[1]  # Elimina el elemento "banana"
