numero_secreto = 42
intento =0 
total_intentos=0

print("Bienvenidos al juego de adivinar")
while intento!= numero_secreto:
    intento = int(input("Ingrese numero:"))
    total_intentos+=1
    if intento<numero_secreto:
        print("Pista: El numero secreto es mayor:")
    elif intento>numero_secreto:
        print("Pista: El numero secreto es menor:")
    else:
        print(f"Super!, adivinaste! en un total de {total_intentos} intentos")
        
