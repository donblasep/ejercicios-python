# Apuntes intro a la programación!!

Este apunte contiene ejercicios introductorios de Python. El código incluye comentarios explicativos para ayudar a comprender **qué hace cada línea**. 

El objetivo es desarrollar la lógica de programación. Se incluyen además explicaciones breves de los conceptos fundamentales.

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

## 2. El `=` vs el `==` (Error clásico)

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
    print("Aprobaste!")
elif nota >= 4.0:
    print("Salvaste el ramo.")
else:
    print("Reprobaste!")
```
**Algo MUY importante:** Fíjense que adentro del `if` hay un espacio vacío antes del `print` (se llama **indentación**, que se hace con la tecla Tabulador). Ese espacio le dice al programa *"este print va adentro del if"*. Si no lo ponen, les dará un `IndentationError`.

---

## 4. Obligar a poner bien la nota (el ciclo `while`)

Un ciclo `while` repite una porción de código. Aquí lo usamos para indicar: *"mientras la nota sea inválida, volver a preguntar"*.

```python
# iniciamos con una nota mala a proposito para forzar que entre al while
nota = -1.0

# "mientras la nota sea menor a 1.0 o (or) mayor a 7.0 haz esto..."
while nota < 1.0 or nota > 7.0:
    
    nota = float(input("Ingrese su nota (entre 1.0 y 7.0): "))
    
    # si la nota esta mala, le avisamos antes de repetir
    if nota < 1.0 or nota > 7.0:
        print("Nota inválida, inténtelo de nuevo.")

print("Nota ingresada correctamente:", nota)
```

---

## 5. Contar números con el `for`

El `for` se usa cuando **ya sabemos exactamente cuántas veces queremos repetir algo** (ej. "repite esto 10 veces y sigue").

Acá usamos el `%` (módulo), que te da el resto de una división. Si al dividir por 2 el resto es 0 (`i % 2 == 0`), significa que el número es par. Es un truco muy útil.

```python
# le preguntamos al usuario hasta donde llegar
limite = int(input("¿Hasta qué número revisamos?: "))

# contador de números pares (parte en 0)
pares = 0

# range(1, limite + 1) porque en python el limite NO se incluye
for i in range(1, limite + 1):
    
    # si el resto de dividir por 2 es 0 → es par
    if i % 2 == 0:
        pares += 1  # le sumamos 1 al contador
        
print(f"Del 1 al {limite} encontramos {pares} números pares.")
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
    
    opcion = int(input("Elige una opción (1-3): "))
    
    if opcion == 1:
        cuanto = int(input("¿Cuánto dinero desea retirar?: "))
        
        # revisamos si alcanza el saldo
        if cuanto > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= cuanto
            print("Retiro exitoso. Saldo actual:", saldo)
            
    elif opcion == 2:
        cuanto = int(input("¿Cuánto dinero desea depositar?: "))
        saldo += cuanto
        print("Depósito exitoso. Tu saldo ahora es:", saldo)
        
    elif opcion == 3:
        print("Saliendo del sistema...")
        
    else:
        print("Opción inválida. Intente nuevamente.")
```

---

## 7. Los for anidados (un for adentro de otro)

Un "for anidado" es simplemente meter un ciclo `for` adentro de otro. 
Esto nos sirve mucho cuando queremos revisar cosas en 2 dimensiones, como **filas y columnas** de una tabla o hacer un patrón en pantalla.

El truco para entenderlo es: **por CADA vuelta que da el `for` de afuera, el `for` de adentro da TODAS sus vueltas completas.**

```python
# Ejemplo: Las tablas de multiplicar (del 1 al 3)

# El for "de afuera" escoge qué tabla vamos a ver
for tabla in range(1, 4):
    print(f"=== Tabla del {tabla} ===")
    
    # El for "de adentro" hace la multiplicacion del 1 al 5
    for numero in range(1, 6):
        resultado = tabla * numero
        print(f"{tabla} x {numero} = {resultado}")
        
    # Fíjate que este print vacío está fuera del for de "adentro", 
    # pero adentro del for de "afuera"
    print("") # Un salto de línea para separar cada tabla
```

Se recomienda leer y ejecutar estos códigos en su propio compu. Una buena práctica es intentar modificar el código para ver cómo reacciona y qué errores aparecen.

Si ya se sienten listos, **abran el archivo `exercices.py`**. Allí encontrarán una guía de repaso con ejercicios para practicar la escritura de código desde cero. 

Mucho éxito en la evaluación!

---
💡 **¿A punto de dar la prueba?** Revisa nuestro apunte resumen: [Torpedo del Certamen](torpedo_certamen.md)
