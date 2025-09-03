
num = int(input("Introduce un número entero: "))
invertido = 0
n = abs(num)
while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n //= 10

if num < 0:
    invertido = -invertido
print(f"El número invertido es: {invertido}")