# 🚀 Torpedo Solemne Python

## 1. Variables
```python
edad = int(input("Edad: "))   # int: número entero
nota = float(input("Nota: ")) # float: número decimal (con .)
```

## 2. Menú (`while` + `if`)
Se repite hasta elegir la opción de salir (ej. 3).
```python
opcion = 0
saldo = 10000

#Si la opción es 3, se sale del while, entonces mientras la opción sea distinta de 3, se ejecutará el while
while opcion != 3:
    opcion = int(input("1.Retirar 2.Depositar 3.Salir : "))
    if opcion == 1:
        monto = int(input("Monto: "))
        if monto > saldo: 
            print("Sin saldo")
        else: 
            saldo -= monto # quita plata
    elif opcion == 2:
        saldo += int(input("Monto: ")) # suma plata
```

## 3. Validación de Entrada (`while`)
Se le pregunta a la persona un valor, si este no es correcto, se le vuelve a preguntar hasta que sea correcto (Cuando es correcto, la variable estado debe ser falsa para salir del while)
```python
status = True

while status:
    nota = float(input("Nota (1-7): "))
    
    if nota >= 1.0 and nota <= 7.0:
        status = False
    else:
        print("Error. Ingrese nota válida")
```

## 4. Contadores, Acumuladores y Juego (`while`)
```python
secreto = 42
intentos = 0
num = 0
while num != secreto:
    num = int(input("Adivina el numero secreto: "))
    intentos += 1 # Contador (suma 1 por vuelta)
    if num < secreto: 
        print("El numero secreto es mayor")
    elif num > secreto: 
        print("El numero secreto es menor")
print("Adivinaste el numero secreto en", intentos, "intentos")

```

## 5. Ciclo `for` y Función Módulo (`%`)
Útil cuando sabes cuántas veces repetir. `%` saca el resto.
```python
num = 10
pares = 0
# range(1, 11) cuenta del 1 al 10 (el último no se incluye)
for i in range(1, num + 1): 
    if i % 2 == 0: # Si el resto de dividir por 2 es 0, es PAR
        pares += 1
```

## 6. Recomendaciones y Tips
* **Test mental** Arriba del todo, anota tus variables (`saldo`, `intentos`) y ve actualizando su valor mentalmente línea por línea.
* **Cuidado con la Indentación:** Todo lo que va "dentro" de un `while`, `for` o `if` lleva un espacio (Tabulador) al inicio de la línea.
* **Asignar o Preguntar?:** Un igual `=` guarda un dato (`edad = 18`). Doble igual `==` pregunta (`if edad == 18:`).
* **El menú:** Si el ejercicio dice "repetir hasta que...", es seguro que necesitas `while opcion != X:`.
