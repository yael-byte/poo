class Planeta:
    _total_planetas = 0

    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia  
        Planeta._total_planetas += 1
        print(f" Planeta '{self.nombre}' registrado.")

    def __del__(self):
        Planeta._total_planetas -= 1
        print(f"💥 Planeta '{self.nombre}' eliminado.")

    @classmethod
    def total_planetas(cls):
        print(f"Total de planetas registrados: {cls._total_planetas}")
        return cls._total_planetas

    def mostrar_info(self):
        print(f"Planeta: {self.nombre} | Distancia: {self.distancia} millones de km")


class NaveEspacial:
    _total_naves = 0

    def __init__(self, nombre, velocidad, *recursos, **misiones):
        self.nombre = nombre
        self.velocidad = velocidad  
        self.destino = None
        self.recursos = recursos
        self.misiones = misiones
        NaveEspacial._total_naves += 1
        print(f" Nave '{self.nombre}' registrada.")

    def __del__(self):
        NaveEspacial._total_naves -= 1
        print(f" Nave '{self.nombre}' eliminada.")

    @classmethod
    def total_naves(cls):
        print(f"Total de naves registradas: {cls._total_naves}")
        return cls._total_naves

    def asignar_destino(self, planeta):
        self.destino = planeta
        print(f"Destino asignado: {planeta.nombre}")

    def calcular_tiempo_viaje(self):
        if not self.destino:
            print("No hay destino asignado.")
            return None
        tiempo = self.destino.distancia / self.velocidad
        print(f"Tiempo estimado de viaje a {self.destino.nombre}: {tiempo:.2f} horas")
        return tiempo

    def mostrar_info(self):
        print(f"Nave: {self.nombre} | Velocidad: {self.velocidad} millones km/h")
        if self.destino:
            print(f"Destino: {self.destino.nombre}")
        if self.recursos:
            print(f"Recursos: {', '.join(self.recursos)}")
        if self.misiones:
            print("Misiones:")
            for k, v in self.misiones.items():
                print(f"  {k}: {v}")



planetas = []
naves = []

def registrar_planeta():
    nombre = input("Nombre del planeta: ")
    try:
        distancia = float(input("Distancia desde la Tierra (millones de km): "))
        planeta = Planeta(nombre, distancia)
        planetas.append(planeta)
    except ValueError:
        print("Distancia inválida.")

def registrar_nave():
    nombre = input("Nombre de la nave: ")
    try:
        velocidad = float(input("Velocidad (millones de km/h): "))
        recursos = input("Recursos (separados por coma): ").split(",")
        misiones = {}
        while True:
            clave = input("Agregar misión (nombre, Enter para terminar): ")
            if not clave:
                break
            valor = input(f"Descripción de la misión '{clave}': ")
            misiones[clave] = valor
        nave = NaveEspacial(nombre, velocidad, *recursos, **misiones)
        naves.append(nave)
    except ValueError:
        print("Velocidad inválida.")

def asignar_destino():
    if not naves or not planetas:
        print("Debes registrar al menos una nave y un planeta.")
        return
    for i, nave in enumerate(naves):
        print(f"{i+1}. {nave.nombre}")
    idx_nave = int(input("Elige la nave: ")) - 1
    for j, planeta in enumerate(planetas):
        print(f"{j+1}. {planeta.nombre}")
    idx_planeta = int(input("Elige el planeta destino: ")) - 1
    naves[idx_nave].asignar_destino(planetas[idx_planeta])

def calcular_tiempo():
    if not naves:
        print("No hay naves registradas.")
        return
    for i, nave in enumerate(naves):
        print(f"{i+1}. {nave.nombre}")
    idx_nave = int(input("Elige la nave: ")) - 1
    naves[idx_nave].calcular_tiempo_viaje()

def mostrar_info():
    print("\n--- Información de Planetas ---")
    for planeta in planetas:
        planeta.mostrar_info()
    print("\n--- Información de Naves ---")
    for nave in naves:
        nave.mostrar_info()

def menu():
    while True:
        print("\n--- Simulador de Viajes Interplanetarios ---")
        print("1. Registrar planeta")
        print("2. Registrar nave")
        print("3. Asignar destino")
        print("4. Calcular tiempo de viaje")
        print("5. Mostrar información")
        print("6. Total de planetas y naves")
        print("7. Salir")
        op = input("Elige una opción: ")
        if op == "1":
            registrar_planeta()
        elif op == "2":
            registrar_nave()
        elif op == "3":
            asignar_destino()
        elif op == "4":
            calcular_tiempo()
        elif op == "5":
            mostrar_info()
        elif op == "6":
            Planeta.total_planetas()
            NaveEspacial.total_naves()
        elif op == "7":
            print("¡Hasta pronto, viajero espacial!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()