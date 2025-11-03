class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
    
    def presentarse(self):
        print(f"Hola a todos! Soy {self.nombre}, artista de {self.genero}.")
        print(f"   Mi popularidad es de {self.popularidad}/100")
    
    def actuar(self):
        print(f"{self.nombre} está actuando")
    
    def despedirse(self):
        print(f"Gracias por su apoyo- {self.nombre}")