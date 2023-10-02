from ClasePadre import Animal


# Clase hija que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza="Desconocida"):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Woof!"


# Clase hija que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color="Negro"):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau!"


# Crear instancias de las clases hijas
mi_perro = Perro("Buddy", 3, "Labrador")
mi_gato = Gato("Whiskers", 2)

print(mi_perro.hacer_sonido())