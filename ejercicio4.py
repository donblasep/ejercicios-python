#Bucles anidados!!!
n = int(input("Ingrese la altura del triangulo:"))
for i in range(1,n+1):
    #el bucle interno imprime 'i' asteriscos en la misma linea
    for j in range(0,i):
        print("*",end="")
    print("")
