
#len(): Devuelve la longitud de una cadena.

texto = "Hola, mundo"
longitud = len(texto)
print(longitud)  # Output: 11

#concatenación: Puedes concatenar strings utilizando el operador +.

cadena1 = "Hola"
cadena2 = "Mundo"
concatenada = cadena1 + " " + cadena2
print(concatenada)  # Output: "Hola Mundo"

#split(): Divide una cadena en una lista de subcadenas basadas en un delimitador.

texto = "Manzanas,Peras,Uvas"
frutas = texto.split(",")
print(frutas)  # Output: ['Manzanas', 'Peras', 'Uvas']

#join(): Une una lista de strings en una sola cadena usando un separador.

frutas = ['Manzanas', 'Peras', 'Uvas']
texto = ",".join(frutas)
print(texto)  # Output: "Manzanas,Peras,Uvas"

#strip(): Elimina espacios en blanco (u otros caracteres) del principio y el final de una cadena.
cadena = "   Hola, mundo   "
limpiada = cadena.strip()
print(limpiada)  # Output: "Hola, mundo"

#find(): Encuentra la primera posición de una subcadena en una cadena.
texto = "La vida es bella"
posicion = texto.find("vida")
print(posicion)  # Output: 3