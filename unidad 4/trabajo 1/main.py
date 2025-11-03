class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def resumen(self):
        return f"{self.nombre} - {self.genero} (Popularidad: {self.popularidad})"


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion):
        super().__init__(nombre, genero, popularidad)
        self.cancion = cancion

    def resumen(self):
        return f"Cantante: {super().resumen()} - Canción más popular: {self.cancion}"


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def resumen(self):
        return f"DJ: {super().resumen()} - Estilo: {self.estilo}"


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def resumen(self):
        return f"Banda: {super().resumen()} - Integrantes: {self.integrantes}"


def iniciar_festival(lista_artistas):
    print("\nINICIANDO FESTIVAL\n")
    if not lista_artistas:
        print("No hay artistas registrados.")
        return

    ordenados = sorted(lista_artistas, key=lambda a: a.popularidad, reverse=True)

    print("Cartel del festival (ordenado por popularidad):\n")
    for i, artista in enumerate(ordenados, start=1):
        print(f"{i}. {artista.resumen()}")
    print("\n¡Que comience la música!\n")


def main():
    print("ORGANIZADOR DE FESTIVAL DE MÚSICA\n")
    
    while True:
        try:
            num_artistas = int(input("¿Cuántos artistas se presentarán en el festival? "))
            if num_artistas > 0:
                break
            else:
                print("Por favor, ingresa un número mayor a 0.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    lista_artistas = []
    
    for i in range(num_artistas):
        print(f"\n--- Artista #{i+1} ---")
        
        while True:
            tipo = input("Tipo de artista (Cantante/DJ/Banda): ").strip().lower()
            if tipo in ['cantante', 'dj', 'banda']:
                break
            else:
                print("Tipo inválido. Elige entre: Cantante, DJ o Banda")
        
        nombre = input("Nombre del artista: ").strip()
        genero = input("Género musical: ").strip()
        
        
        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                else:
                    print("La popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
       
        if tipo == 'cantante':
            cancion = input("Canción más popular: ").strip()
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == 'dj':
            estilo = input("Estilo de mezcla: ").strip()
            artista = DJ(nombre, genero, popularidad, estilo)
        else:  
            while True:
                try:
                    integrantes = int(input("Número de integrantes: "))
                    if integrantes > 0:
                        break
                    else:
                        print("Debe haber al menos 1 integrante.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            artista = Banda(nombre, genero, popularidad, integrantes)
        
        lista_artistas.append(artista)
        print(f"{nombre} agregado al festival")
    

    iniciar_festival(lista_artistas)



if __name__ == "__main__":
    main()
