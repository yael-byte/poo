

x = float(input("Introduce el primer número: "))
y = float(input("Introduce el segundo número: "))
z = float(input("Introduce el tercer número: "))

# Usamos funciones integradas
mayor = max(x, y, z)
menor = min(x, y, z)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
if x != y and x != z and y != z:
    print("los tres numeros son diferentes")