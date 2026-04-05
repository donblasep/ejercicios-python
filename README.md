# Ejercicios pa salvar el certamen de intro!!

Buenas cabros, armé este apunte con los ejercicios típicos. Le puse comentarios al código para que se entienda **qué hace cada cosa** y no copien a ciegas. 

La idea es que entiendan la lógica. Agregué también explicaciones cortitas de lo más básico para que todos partamos de la misma base.

---

## 1. ¿Qué es una variable?

Imagínate que es una **caja** con un nombre por fuera, donde adentro guardas un dato.

```python
edad = 18          # Caja "edad" guarda el número 18
nombre = "Juanito" # Caja "nombre" guarda texto (va con comillas)
```

Dependiendo de qué guardes, es el **tipo** de dato:
*   `int` (enteros): Números sin decimales (`-5`, `0`, `20`).
*   `float` (flotantes): Números con decimales (`3.14`, `5.5`). **Ojo:** Usa siempre punto (`.`), no coma.
*   `string` o `str` (texto): Palabras o frases. **Siempre** entre comillas (`"hola"`).
*   `bool` (booleanos): Solo puede ser `True` (Verdadero) o `False` (Falso). Como un interruptor.

---

## 2. El `=` vs el `==` (Error típico)

*   Un solo igual `=` es para **GUARDAR** o **ASIGNAR**.
    `nota = 7.0` (Guardo el 7.0 en la variable nota).
*   Doble igual `==` es para **PREGUNTAR** o **COMPARAR**.
    `if nota == 7.0:` (¿Es verdad que la nota es exactamente 7.0?)

Nunca hagan `if nota = 7.0:` porque el programa dará error!

---

## 3. Tomar decisiones: `if`, `elif` y `else`

Sirven para que el programa tome caminos distintos según qué pase:
*   **`if`**: "SI pasa esto..." (Ej: "SI te sacas un 7...")
*   **`elif`**: "O SI NO, SI pasa esto otro..." (Ej: "O SI NO, SI te sacas un 5...")
*   **`else`**: "SI NO PASÓ NADA DE LO ANTERIOR..." (Ej: "Estás castigado").

```python
nota = float(input("¿Que nota te sacaste? "))

if nota >= 6.0:  # Ojo con los dos puntos al final (:)
    print("¡Buena, te pasaste!")
elif nota >= 4.0:
    print("Salvaste el ramo.")
else:
    print("¡F, a seguir estudiando!")
```
**Algo MUY importante:** Fíjense que adentro del `if` hay un espacio vacío antes del `print` (se llama **indentación**, que se hace con la tecla Tabulador). Ese espacio le dice al programa *"oye, este print va adentro del if"*. Si no lo ponen, les dará un `IndentationError`.

---

## 4. Obligar a poner bien la nota (el ciclo `while`)

Un ciclo `while` repite código. Acá lo usamos para decir: *"mientras la nota esté mala, sigo preguntando"*.

```python
# iniciamos con una nota mala a proposito para forzar que entre al while
nota = -1.0

# "mientras la nota sea menor a 1.0 o (or) mayor a 7.0 haz esto..."
while nota < 1.0 or nota > 7.0:
    
    nota = float(input("pon tu nota aca (entre 1.0 y 7.0): "))
    
    # si la nota esta mala, le avisamos antes de repetir
    if nota < 1.0 or nota > 7.0:
        print("nota invalida, intentelo de nuevo")

print("nota ingresada :)", nota)
```

---

## 5. Contar números con el `for`

El `for` se usa cuando **ya sabemos exactamente cuántas veces queremos repetir algo** (ej. "repite esto 10 veces y sigue").

Acá usamos el `%` (módulo), que te da el resto de una división. Si al dividir por 2 el resto es 0 (`i % 2 == 0`), significa que el número es par. Es un truco muy útil.

```python
# le preguntamos al usuario hasta donde llegar
limite = int(input("hasta que numero revisamos?: "))

# contador de números pares (parte en 0)
pares = 0

# range(1, limite + 1) porque en python el limite NO se incluye
for i in range(1, limite + 1):
    
    # si el resto de dividir por 2 es 0 → es par
    if i % 2 == 0:
        pares += 1  # le sumamos 1 al contador
        
print(f"del 1 al {limite} pillamos {pares} numeros pares")
```

---

## 6. Hacer un menú (while + if combinados)

Los menús se hacen combinando un `while` con varios `if`/`elif`. La idea es que se repita hasta que el usuario elija salir (opción 3).

```python
saldo = 10000 
opcion = 0  

# corre infinitamente mientras no elija la opcion 3
while opcion != 3:
    print("=== CAJERO ===")
    print("1. Sacar plata")
    print("2. Meter plata")
    print("3. Retirarse")
    
    opcion = int(input("elige que vas a hacer y pon un numero: "))
    
    if opcion == 1:
        cuanto = int(input("cuanto quieres?: "))
        
        # revisamos si alcanza el saldo
        if cuanto > saldo:
            print("estay pato, no tienes plata suficiente")
        else:
            saldo -= cuanto
            print("listo, te desconte la plata. saldo actual:", saldo)
            
    elif opcion == 2:
        cuanto = int(input("cuanto vay a meter?: "))
        saldo += cuanto
        print("buena, tu saldo ahora esta en:", saldo)
        
    elif opcion == 3:
        print("nos vemooos cuidese")
        
    else:
        print("opcion mala! lee el menu porfa")
```

Ya ps cabros, léanlo, ejecuten los códigos ustedes mismos en su compu y prueben romperlos borrándole un tab o una letra.

Y si ya se sienten listos, **abran el archivo `exercices.py`**. Ahí hay una mini guía de repaso con ejercicios en blanco para que  escriban código desde cero. 

Mucho éxito en el solemne!
