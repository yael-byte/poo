
num = int(input("Introduce un número entero: "))
cont = 0
n = abs(num)  # ignoramos el signo
while n > 0:
    n //= 10
    cont += 1
print(f"El número {num} tiene {cont} dígitos")              
