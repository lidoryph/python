invertir = float(input("Introduce una cantidad a invertir sin el simbolo €: "))
interes = float(input("Introduce un porcentaje de interes anual sin el simbolo %: "))
años = float(input("Introduce una cantidad de años a invertir: "))
capital: float = invertir * ((interes / 100) + 1) ** años

print("Capital final: " + str(round(capital, 2)))
