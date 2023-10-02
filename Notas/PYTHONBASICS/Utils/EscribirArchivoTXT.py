
#otra forma de leer archivos
with open('Ejemplo.txt', 'r') as reader:
    content = reader.readlines()
    with open('Ejemplo.txt', 'w') as writer:
        for line in content:
            writer.write(line)
        writer.write("\nNuevo Texto")
