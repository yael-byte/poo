nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    print("\nAGREGAR CANCIONES")
    try:
        n = int(input("¿Cuántas canciones deseas agregar? "))
    except:
        print("Debes ingresar un número entero.")
        return

    for i in range(n):
        print(f"\nCanción {i+1}:")
        nombre = input("Nombre: ")
        artista = input("Artista: ")

        while True:
            try:
                duracion = float(input("Duración (minutos): "))
                break
            except:
                print("Ingresa un número válido.")

        while True:
            try:
                pop = int(input("Popularidad (1-100): "))
                if 1 <= pop <= 100:
                    break
                else:
                    print("Debe estar entre 1 y 100.")
            except:
                print("Ingresa un número entero.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(pop)

    print("Canciones agregadas correctamente.")


def ver_reportes():
    print("\nREPORTES DE LA PLAYLIST")

    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    pop_max = max(popularidades)
    pop_min = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones

    idx_max = popularidades.index(pop_max)
    idx_min = popularidades.index(pop_min)

    print(f"Total de canciones: {total_canciones}")
    print(f"Duración total: {duracion_total:.2f} min")
    print(f"Canción más popular: {nombres[idx_max]} ({pop_max})")
    print(f"Canción menos popular: {nombres[idx_min]} ({pop_min})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}")


def buscar_canciones():
    print("\nBÚSQUEDA DE CANCIONES")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    op = input("Elige opción: ")

    if op == "1":
        artista_buscar = input("Ingresa el artista: ")
        print("\nResultados:")
        encontrado = False
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"- {nombres[i]} ({artistas[i]}) - Popularidad: {popularidades[i]}")
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones de ese artista.")

    elif op == "2":
        try:
            minimo = int(input("Popularidad mínima: "))
            maximo = int(input("Popularidad máxima: "))
        except:
            print("Debes ingresar valores enteros.")
            return

        print("\nResultados:")
        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"- {nombres[i]} ({artistas[i]}) - Popularidad: {popularidades[i]}")
                encontrado = True
        if not encontrado:
            print("No hay canciones en ese rango de popularidad.")
    else:
        print("Opción inválida.")


def playlist_recomendada():
    print("\nPLAYLIST RECOMENDADA")

    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    promedio_pop = sum(popularidades) / len(popularidades)

    print(f"Popularidad promedio: {promedio_pop:.2f}")
    print("Canciones recomendadas:")

    encontrado = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio_pop:
            print(f"- {nombres[i]} ({artistas[i]}) - Popularidad: {popularidades[i]}")
            encontrado = True

    if not encontrado:
        print("No hay canciones por encima del promedio.")


def menu():
    while True:
        print("\n==============================")
        print("FESTIVAL PLAYLIST")
        print("==============================")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


menu()
