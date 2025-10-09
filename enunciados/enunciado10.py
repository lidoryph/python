payasos = int(input("Introduzca el número de payasos vendidos: "))
muñecas = int(input("Introduzca el número de muñecas vendidas: "))
peso_paquetes = payasos * 112 + muñecas * 75
print("El peso del paquete es de:", peso_paquetes, "gramos.")

if peso_paquetes >= 500:
	print("Mas de 500 gramos!")
