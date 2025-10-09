def calcula_imc(a, b):
        return round((a / ((b)**2)))


edad = int(input("Cuantos años tienes?: "))

if edad >= 18:
        print("Eres mayor de edad!")

        peso = float(input("Introduce tu peso en kilos: "))
        altura = float(input("Introduce tu altura en metros: "))
        
        IMC = calcula_imc(peso, altura)
        print("Tu IMC es de ", IMC)
        
        if IMC < 19:
                print("Bajo peso.")
        elif IMC < 26:
                print("Peso normal.")
        elif IMC < 30:
                print("Sobrepeso.")
        else:
                print("Obesidad.")

        print("--- ANALISIS COMPLETADO ---\n")
else:
        print("No eres mayor de edad.\n")


print("--- PROGRAMA COMPLETADOS ---")