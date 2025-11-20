class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=80):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
        self._validar_estado()

    def _validar_estado(self):
        """Asegura que los atributos se mantengan en el rango de 0 a 100."""
        self.salud = max(0, min(100, self.salud))
        self.felicidad = max(0, min(100, self.felicidad))
        self.energia = max(0, min(100, self.energia))

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        self._validar_estado()
        print("Aumenta su felicidad en 10 y disminuye su salud en 5.")
        self.mostrar_estado()

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        self._validar_estado()
        print("Aumenta su felicidad en 5 y aumenta su salud en 10.")
        self.mostrar_estado()

    def curar(self):
        self.felicidad -= 5
        self.salud += 20
        self._validar_estado()
        print("Disminuye su felicidad en 5 y aumenta su salud en 20.")
        self.mostrar_estado()

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}, Color: {self.color}, Salud: {self.salud}, Felicidad: {self.felicidad}, Energía: {self.energia}")
        
class Gozarutchi(Tamagotchi):
    def jugar(self):
        self.felicidad += 15
        self.salud -= 3
        self._validar_estado()
        print("Gozarutchi está jugando y se siente más feliz.")
        self.mostrar_estado()

    def comer(self):
        self.felicidad += 10
        self.salud += 5
        self._validar_estado()
        print("Gozarutchi comió y se siente mejor.")
        self.mostrar_estado()

    def curar(self):
        self.felicidad -= 2
        self.salud += 15
        self._validar_estado()
        print("Gozarutchi fue curado y se siente más saludable.")
        self.mostrar_estado()
