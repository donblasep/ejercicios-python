#contador de pares e impares con bucle for
# el uso de range

n = int(input("Ingrese el número límite"))

#usamos n+1 para incluir el numero n en el recorrido
pares = 0
impares = 0

for i in range(1, n+1):
    if i % 2 == 0:
        pares +=1
    else:
        impares +=1

print(f"Resultado del 1 al {n}")
print(f"Total de pares:{pares}")
print(f"Total de impares:{impares}")



    
