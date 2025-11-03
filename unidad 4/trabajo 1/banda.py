class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, somos {self.nombre} y tocamos {self.genero}.")

    def actuar(self):
        print(f"{self.nombre} está actuando.")

    def despedirse(self):
        print(f"{self.nombre} se despide. ¡Gracias por venir!")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes
    
    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


# Función para iniciar el festival
def iniciar_festival(lista_artistas):
    print("\n" + "="*60)
    print("BIENVENIDOS AL GRAN FESTIVAL DE MÚSICA")
    print("="*60 + "\n")
    
    for i, artista in enumerate(lista_artistas, 1):
        print(f"Actuación #{i}")
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación \n")
    
    print("="*60)
    print("GRACIAS POR ASISTIR AL FESTIVAL")
    print("="*60)
