num = int(input("Introduce un numero entero positivo para definir la altura: "))
if (num<0):
    input("Ingrese solo numeros positivos")
else:
    for i in range(num):
        print("*"*(i+1))