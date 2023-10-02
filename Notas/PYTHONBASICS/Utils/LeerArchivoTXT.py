archivo = open('Ejemplo.txt')

# leer todas las lineas del archivo
print(archivo.read())

# leer una parte del arhivo
print(archivo.read(4))

# leer una linea completa del archivo
print(archivo.readline())

# Recorrer lineas de un archivo usando ciclo while
linea = archivo.readline()

while linea != "":
    print(linea)
    linea = archivo.readline()

# Recorrer lineas de un archivo usando ciclo for
for linea in archivo.readline():
    print(linea)
# cerrar el archivo leido
archivo.close()
