#Break
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero > 5:
        print("Número mayor que 5 encontrado:", numero)
        break

#Continue
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0

while indice < len(numeros):
    numero = numeros[indice]
    indice += 1

    if numero % 2 == 0:
        continue

    print("Número impar:", numero)