#Recorrer una lista con un bucle for:
frutas = ["manzana", "banana", "naranja", "pera", "uva"]

for fruta in frutas:
    print(fruta)


#Imprimir números pares del 1 al 10 con un bucle for
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)

#Imprimir numeros del 1 al 10 sumando +2 al siguiente numero
for numero in range(1,10,2):
    print(numero)
print("**************************************")

#Imprime los numeros desde el cero hasta el valor indicado excluyendo el numero indicado en el rango
for numero in range(5):
    print(numero)