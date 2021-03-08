num = int(input("Introduce un número entero positivo: "))
if (num<0):
    input("Ingrese solo numeros positivos")
else:
    for i in range(1, num):
        if num % i == 0:
            break
    if (i + 1)  == num:
        print(str(num) + " es primo")
    else: 
        print(str(num) + " no es primo")
