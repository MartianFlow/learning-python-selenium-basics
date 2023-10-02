# Declaración de una variable global
variable_global = None


def usando_variable_global():
    # Indicamos que estamos utilizando la variable global
    global variable_global

    # Modificamos la variable global
    variable_global = "¡Hola desde la función!"


usando_variable_global()

# Imprimimos el valor de la variable global después de llamar a la función
print(variable_global)
