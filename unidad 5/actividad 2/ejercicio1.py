def crear_matriz(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(matriz):
    if not matriz:
        print("\nLa sala de cine no ha sido inicializada.")
        return

    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    print("\n" + "=" * (num_columnas * 4 + 10))
    print("SALA DE CINE".center(num_columnas * 4 + 10))
    print("=" * (num_columnas * 4 + 10))
    
    header = "  Fila |"
    for j in range(num_columnas):
        header += f" C{j+1:<2}"
    print(header)
    print("-" * (num_columnas * 4 + 10))

    for i in range(num_filas):
        fila_str = f" {i+1:<4} |"
        for asiento in matriz[i]:
            fila_str += f" {asiento:<2}"
        print(fila_str)
    
    print("-" * (num_columnas * 4 + 10))
    print("L = Libre | X = Ocupado")
    print("-" * (num_columnas * 4 + 10))

def obtener_posicion(num_filas, num_columnas):
    while True:
        try:
            fila = int(input("Ingrese el número de fila a operar: "))
            columna = int(input("Ingrese el número de columna (asiento): "))

            idx_fila = fila - 1
            idx_columna = columna - 1

            if 0 <= idx_fila < num_filas and 0 <= idx_columna < num_columnas:
                return idx_fila, idx_columna
            else:
                print(f"Error: El asiento ({fila}, {columna}) está fuera del rango de la sala.")
                print(f"La sala tiene {num_filas} filas y {num_columnas} asientos por fila.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def reservar_asiento(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    print("\n--- Reservar Asiento ---")
    idx_fila, idx_columna = obtener_posicion(num_filas, num_columnas)

    if matriz[idx_fila][idx_columna] == "L":
        matriz[idx_fila][idx_columna] = "X"
        print(f"Asiento en Fila {idx_fila+1}, Columna {idx_columna+1} RESERVADO con éxito.")
    else:
        print(f"Error: El asiento en Fila {idx_fila+1}, Columna {idx_columna+1} ya está OCUPADO.")

def liberar_asiento(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    print("\n--- Liberar Asiento ---")
    idx_fila, idx_columna = obtener_posicion(num_filas, num_columnas)

    if matriz[idx_fila][idx_columna] == "X":
        matriz[idx_fila][idx_columna] = "L"
        print(f"Asiento en Fila {idx_fila+1}, Columna {idx_columna+1} LIBERADO con éxito.")
    else:
        print(f"Error: El asiento en Fila {idx_fila+1}, Columna {idx_columna+1} ya estaba LIBRE.")

def mostrar_estadisticas(matriz):
    libres = 0
    ocupados = 0
    
    for fila in matriz:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1
    
    total = libres + ocupados
    
    print("\n--- Estadísticas de Ocupación ---")
    print(f"Capacidad Total: {total} asientos")
    print(f"Asientos Ocupados (X): {ocupados}")
    print(f"Asientos Libres (L): {libres}")
    print("-----------------------------------")


def main():
    
    while True:
        try:
            num_filas = int(input("Ingrese el número de filas de la sala: "))
            num_columnas = int(input("Ingrese el número de columnas (asientos por fila): "))
            
            if num_filas > 0 and num_columnas > 0:
                break
            else:
                print("El número de filas y columnas debe ser mayor que cero.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    asientos = crear_matriz(num_filas, num_columnas)

    while True:
        print("\n\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")
        print("======================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            mostrar_sala(asientos)
        elif opcion == '2':
            reservar_asiento(asientos)
        elif opcion == '3':
            liberar_asiento(asientos)
        elif opcion == '4':
            mostrar_estadisticas(asientos)
        elif opcion == '5':
            print("\nGracias por usar el sistema! Saliendo del programa.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()