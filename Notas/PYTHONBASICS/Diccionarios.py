#Creación de un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

#Acceso a valores por clave
nombre_persona = persona["nombre"]  # "Juan"

#Modificación de valores
persona["edad"] = 31  # Cambia la edad de 30 a 31

#Agregar nuevos pares clave-valor
persona["profesion"] = "Ingeniero"

#Eliminar un par clave-valor
del persona["edad"]  # Elimina la clave "edad" y su valor asociado

claves = persona.keys()  # Devuelve una vista de las claves en el diccionario
valores = producto.values()  # Devuelve una vista de los valores en el diccionario
