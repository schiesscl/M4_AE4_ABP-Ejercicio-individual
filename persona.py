from tamagotchi import Tamagotchi

class Persona:
    def __init__ (self, nombre: str, apellido: str, tamagotchi: Tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi
        #Métodos:
    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} {self.apellido} está jugando con {self.tamagotchi.nombre}.")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} {self.apellido} está alimentando a {self.tamagotchi.nombre}.")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} {self.apellido} está curando a {self.tamagotchi.nombre}.")
        self.tamagotchi.curar()
