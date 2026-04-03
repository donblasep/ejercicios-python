
# Ejercicios pa salvar el certamen de intro!!

Buenas cabros, armé este apunte con ejercicios de la guía del profe porque vi que varios estaban perdidos. Le puse comentarios al código línea por línea pa que se entienda **qué hace cada cosa**, en vez de copiarlo a ciegas.

La idea es que lean los comentarios y traten de cachar la lógica de por qué está cada cosa ahí. Si hacen eso, deberían andar bien en la prueba.

---

## 1. Obligar a poner bien la nota (el ciclo `while`)

Este es típico. Si nos piden una nota, tenemos que asegurarnos de que esté entre 1.0 y 7.0. Acá usamos un `while`, que básicamente es: *"mientras la nota esté mala, sigo preguntando"*.

```python
# iniciamos la nota con un numero falso para forzar q entre al while
# si empezamos con un 5.0, se saltaria todo el while y estaria mal
nota = -1.0

# "mientras la nota sea menor a 1.0 o mayor a 7.0"
while nota < 1.0 or nota > 7.0:
    
    # pedimos la nota al usuario (float = numero con decimales)
    nota = float(input("pon tu nota aca (entre 1.0 y 7.0): "))
    
    # si esta mala, avisamos
    if nota < 1.0 or nota > 7.0:
        print("error profe, nota invalida")

# si sale del while, la nota es valida
print("nota ingresada :)", nota)
```

---

## 2. Contar números con el `for`

El `for` es muy útil cuando ya sabemos cuántas veces queremos repetir algo. En este caso, el límite lo pone el usuario con un `input`, pero la idea es la misma, el programa ya tiene claro desde el inicio hasta dónde va a contar

Además usamos el `%`, que es un truco para identificar números pares. Este operador te da el resto de una división, entonces si tomas cualquier número y al dividirlo por 2 el resto es 0 (`i % 2 == 0`), significa que es par

```python
# numero entero
limite = int(input("hasta que numero revisamos?: "))

# contador de pares
pares = 0

# range(1, limite + 1) porque el limite no se incluye
for i in range(1, limite + 1):
    
    # si el resto de dividir por 2 es 0 → es par
    if i % 2 == 0:
        pares += 1  # lo mismo que pares = pares + 1

print(f"del 1 al {limite} pillamos {pares} numeros pares")
```

---

## 3. Hacer un menú (while + if)

Los menús casi siempre van con `while`. La idea es que se repita hasta que el usuario decida salir (opción 3).

```python
saldo = 10000 
opcion = 0  # lo que elige el usuario

# corre hasta que elija salir
while opcion != 3:
    print("=== CAJERO ===")
    print("1. Sacar plata")
    print("2. Meter plata")
    print("3. Retirarse")
    
    opcion = int(input("elige que vas a hacer: "))
    
    if opcion == 1:
        cuanto = int(input("cuanto quieres?: "))
        
        if cuanto > saldo:
            print("estay pato, no tienes plata")
        else:
            saldo -= cuanto
            print("listo. saldo actual:", saldo)
            
    elif opcion == 2:
        cuanto = int(input("cuanto vay a meter?: "))
        saldo += cuanto
        print("tu saldo esta en:", saldo)
        
    elif opcion == 3:
        print("nos vemooos")
        
    else:
        print("opcion mala!")
```

---

Ya ps cabros, léanlo un par de veces, ejecuten los códigos ustedes mismos y prueben romperlos. Así se aprende mucho más que copiando nomas.

Éxito en el solemne

