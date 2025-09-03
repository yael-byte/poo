calificacion = int(input("Introduce la calificación (0-100): "))

if 90 <= calificacion <= 100:
    print("Tu calificación es: A")
elif 80 <= calificacion <= 89:
    print("Tu calificación es: B")
elif 70 <= calificacion <= 79:
    print("Tu calificación es: C")
elif 60 <= calificacion <= 69:
    print("Tu calificación es: D")
elif 0 <= calificacion < 60:
    print("Tu calificación es: F")
else:
    print("⚠️ Error: calificación fuera de rango (0-100)")
