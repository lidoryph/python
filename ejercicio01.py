edad = int(input("Cuantos años tienes?: "))
if edad >= 18:
        print("Eres mayor de edad!")
        peso = float(input("Introduce tu peso en kilos: "))
        altura = float(input("Introduce tu altura en metros: "))
        IMC = peso / ((altura)**2)
        
        if IMC < 19:
                print("Bajo peso.")
        elif IMC < 26:
                print("Peso normal.")
        elif IMC < 30:
                print("Sobrepeso.")
        else:
                print("Obesidad.")

else:
        print("No eres mayor de edad.\n")



print("--- FIN DEL PROGRAMA ---")