class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def obtener_anho_nacimiento(self, anho_actual):
        anho_nacimiento = anho_actual - self.edad
        return anho_nacimiento

# objeto de la clase Persona con atributos
persona = Persona("Juan", 30)

# Llamar a los métodos de la clase Persona
persona.saludar()
print(f"Año de nacimiento: {persona.obtener_anho_nacimiento(2023)}")