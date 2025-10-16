intentos = int()
numero = int(input("Introduce un numero: "))

while(numero > 0):
        intentos += 1
        print("Intentalo de nuevo")
        numero = int(input("Introduce un numero: "))

print("Te ha costado", intentos, "intentos")
