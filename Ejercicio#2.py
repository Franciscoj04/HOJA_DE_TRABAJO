
num = int(input("Introduce un número entero positivo: "))
if (num<0):
    input("Ingrese solo numeros positivos")
else:
    for i in range(num, -1, -1):
        print(i, end=", ")