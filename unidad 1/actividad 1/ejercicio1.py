a = float(input("Introduce la longitud del lado 1: "))
b = float(input("Introduce la longitud del lado 2: "))
c = float(input("Introduce la longitud del lado 3: "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("El triángulo es equilátero")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("Los lados ingresados NO forman un triángulo válido")
