#Crhistopher Isram Mancilla Laure
#Polimorfismo

#Ejemplo 1
class Auto:
    rueda = 4
    def desplazamiento(self):
        print("El auto se esta desplazando sobre 4 ruedas")

class Moto:
    rueda = 2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

#Ejemplo 2
class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("animal salvaje")

class Perro(Animales):
    def tipo_animal(self):
        print("animal domestico")

nuevo_animal = Leon("SIMBA")
nuevo_animal.tipo_animal()

nuevo_animal2 = Perro("REX")
nuevo_animal2.tipo_animal()