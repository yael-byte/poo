class Pokemon:
    _total_creados = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon._total_creados += 1
        print(f"¡Ha aparecido un {self.nombre} salvaje! ")

    def mostrar_info(self):
        print("\n--- Información del Pokémon ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")
        print("-----------------------------\n")

    def entrenar(self, *stats_a_mejorar):
        self.nivel += 1
        print(f"¡{self.nombre} ha subido al nivel {self.nivel}! ")

        if not stats_a_mejorar:
            self.ataque += 2
            self.defensa += 2
            self.salud += 5
            print("Todas las estadísticas han mejorado.")
        else:
            if "ataque" in stats_a_mejorar:
                self.ataque += 4
                print("¡El ataque ha aumentado!")
            if "defensa" in stats_a_mejorar:
                self.defensa += 4
                print("¡La defensa ha aumentado!")
            if "salud" in stats_a_mejorar:
                self.salud += 10
                print("¡La salud ha aumentado!")

    def atacar(self, objetivo):
        daño = max(1, self.ataque - objetivo.defensa)
        objetivo.salud -= daño
        print(f"¡{self.nombre} ataca a {objetivo.nombre} y le causa {daño} de daño!")
        if objetivo.salud <= 0:
            print(f"¡{objetivo.nombre} ha sido derrotado!")

    @classmethod
    def total_pokemons(cls):
        print(f"Actualmente existen {cls._total_creados} Pokémon en el juego.")
        return cls._total_creados

    @classmethod
    def restar_pokemon(cls):
        if cls._total_creados > 0:
            cls._total_creados -= 1