try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError as e:
    # Manejo de la excepción
    print("¡Error! No se puede dividir por cero.")
    print(e)
finally:
    # Este bloque se ejecutará siempre
    print("Finalizando el proceso.")