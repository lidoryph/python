from calcula_imc import calcula_imc

edad = int(input("Cuantos años tienes?: "))

if edad >= 18:
        print("Eres mayor de edad!")

        peso = float(input("Introduzca su peso en kg: "))
        altura = float(input("Introduzca su altura en metros: "))
        
        imc = calcula_imc(peso, altura)
        print("Tu índice de masa corporal (IMC) es de ", imc)
        
        if imc < 19:
                print("Bajo peso.")
        elif imc < 26:
                print("Peso normal.")
        elif imc < 30:
                print("Sobrepeso.")
        else:
                print("Obesidad.")

        print("Análisis terminado.\n")
else:
        print("No eres mayor de edad.\n")


print("--- PROGRAMA COMPLETADO ---")