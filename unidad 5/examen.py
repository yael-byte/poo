def programa_calificaciones():
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    num_materias = int(input("Ingrese el número de materias: "))

    calificaciones = []
    nombres_estudiantes = [f"Estudiante {i+1}" for i in range(num_estudiantes)]
    nombres_materias = [f"Materia {j+1}" for j in range(num_materias)]

    print("\n--- Captura de Calificaciones ---")
    for i in range(num_estudiantes):
        fila_estudiante = []
        print(f"\nCapturando calificaciones para {nombres_estudiantes[i]}:")
        for j in range(num_materias):
            while True:
                try:
                    calif = float(input(f"  Ingrese calificación para {nombres_materias[j]} (0-100): "))
                    if 0 <= calif <= 100:
                        fila_estudiante.append(calif)
                        break
                    else:
                        print("Error: La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
        calificaciones.append(fila_estudiante)

    # 1. Promedio de cada estudiante
    promedios_estudiantes = [sum(fila) / num_materias for fila in calificaciones]

    # 2. Promedio de cada materia
    promedios_materias = []
    if num_estudiantes > 0:
        for j in range(num_materias):
            suma_materia = sum(calificaciones[i][j] for i in range(num_estudiantes))
            promedios_materias.append(suma_materia / num_estudiantes)
    
    # 3. Calificación más alta y más baja
    calificaciones_planas = [calif for fila in calificaciones for calif in fila]
    
    calificacion_maxima = max(calificaciones_planas) if calificaciones_planas else "N/A"
    calificacion_minima = min(calificaciones_planas) if calificaciones_planas else "N/A"

    # --- Impresión de Resultados ---
    print("\n" + "="*50)
    print("RESUMEN DE CALIFICACIONES DEL GRUPO".center(50))
    print("="*50)

    # Imprimir Matriz de Calificaciones
    print("\nMatriz de Calificaciones:")
    header = ["Estudiante"] + nombres_materias + ["Promedio Est."]
    print(f"{header[0]:<15} | {' | '.join(f'{m:<15}' for m in header[1:-1])} | {header[-1]:<15}")
    print("-" * (15 + (num_materias * 18) + 3 + 15))

    for i in range(num_estudiantes):
        fila_str = f"{nombres_estudiantes[i]:<15} | "
        fila_str += ' | '.join(f'{calificaciones[i][j]:<15.2f}' for j in range(num_materias))
        fila_str += f" | {promedios_estudiantes[i]:<15.2f}"
        print(fila_str)

    print("-" * (15 + (num_materias * 18) + 3 + 15))


    print(f"{'Promedio Materia':<15} | ", end="")
    print(' | '.join(f'{pm:<15.2f}' for pm in promedios_materias))

    print("\n" + "-"*50)
    print("Estadísticas Generales".center(50))
    print("-"*50)
    print(f"Calificación Más Alta del Grupo: {calificacion_maxima}")
    print(f"Calificación Más Baja del Grupo: {calificacion_minima}")
    print("-" * 50)

if __name__ == "__main__":
    programa_calificaciones()