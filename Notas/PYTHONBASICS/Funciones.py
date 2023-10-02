#Funcion sin parametros
def saludar():
    print("¡Hola! Bienvenido a Python.")

# Llamada a la función
saludar()

#Función con parámetros
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función con argumentos
resultado_suma = sumar(5, 3)
print("El resultado de la suma es:", resultado_suma)