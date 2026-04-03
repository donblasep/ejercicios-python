#inicializar un valor que obligue a entrar al blucle
nota = -1.0

while nota<1.0 or nota >7.0:
    nota = float(input("Ingrese una nota (entre 1.0 y 7.0)"))

    if nota<1.0 or nota >7.0:
        print("Error: El valor ingresado no es valido")

print("Nota registrada :)")


# F y F = F
# F y V = F
# V y F = F
# V y V = V

# F o F = F
# F o V = V
# V o F = V
# V o V = V
