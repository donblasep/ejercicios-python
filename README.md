# Ejercicios pa salvar el certamen de intro!!

Buenas cabros, armé este apunte con ejercicios de la guía del profe porque vi que varios estaban perdidos. Le puse comentarios al código línea por línea pa que se entienda **qué hace cada cosa**, en vez de copiarlo a ciegas.

La idea es que lean los comentarios y traten de cachar la lógica de por qué está cada cosa ahí. Si hacen eso, deberían andar bien en la prueba. Y como varios preguntaron, agregué explicaciones de las cosas más básicas desde cero para que nadie se quede atrás.

---

## 1. ¿Qué es una variable? (Lo más básico de lo básico)

Antes de mandarnos a hacer ciclos y menús completos, tenemos que entender qué es una variable. Imagínate que una variable es derechamente una **caja** que tiene un nombre escrito por fuera con un plumón, y adentro le guardas un dato.

```python
# Acá creamos una caja llamada "edad" y le metemos el número 18
edad = 18

# Acá creamos una caja llamada "nombre" y le metemos texto (va con comillas)
nombre = "Juanito" 
```

Dependiendo de qué guardes en la caja, es el **tipo** de dato. Aprenderse esto te va a salvar la vida:
*   `int` (enteros): Números sin la coma decimal (ej: `-5`, `0`, `20`). Sirve pa contar cosas enteras, como personas o goles.
*   `float` (flotantes): Números con decimales (ej: `3.14`, `5.5`). **Ojo:** en Python siempre se usa el punto (`.`), no la coma (`,`). Si ponen coma, se les rompe el código.
*   `string` o `str` (texto): Letras, palabras o frases. **Siempre** tienen que ir entre comillas (por ejemplo, `"hola"` o `'chao'`). Si se te olvidan las comillas, Python va a creer que es una variable y va a tirar un error gigante rojo.
*   `bool` (booleanos): Es súper simple, es `True` (Verdadero) o `False` (Falso). Es literal como el interruptor de la luz de tu pieza: prendido o apagado.

---

## 2. El `=` vs el `==` (El error número 1 de la historia)

Este error les va a pasar a todos los que están partiendo, así que grábenselo al tiro, les prometo que va a salir en la prueba:
*   Un solo igual `=` significa **GUARDAR** o **ASIGNAR**. Es como decir "toma este valor y mételo en la caja".
    `nota = 7.0` (Agarro el número 7.0 y lo guardo adentro de la variable nota).
*   Doble igual `==` significa **PREGUNTAR** o **COMPARAR**. Es como la cara de sospecha de decir "¿Es verdad que esto es idéntico a esto otro?".
    `if nota == 7.0:` (¿Es verdad que la nota que está en la caja es un 7.0 perfecto?)

¡Nunca jamás hagan `if nota = 7.0:` porque Python se va a marear creyendo que le quieres guardar un dato adentro de un if y el programa va a explotar!

---

## 3. Tomar decisiones: el `if`, `elif` y `else`

Acá es donde el programa se pone inteligente. El `if` sirve para que el programa tome distintos caminos dependiendo de qué pase. Es decir "SI pasa esto... haz esto". Imaginen que es como las instrucciones o amenazas que da la mamá:
*   **`if`**: "SI te sacas un 7..."
*   **`elif`**: (significa "else if", o sea "O SI NO, SI...") "...O SI NO, SI te sacas entre un 4 y un 6..."
*   **`else`**: ("SI NO PASÓ ABSOLUTAMENTE NADA DE LO ANTERIOR...") "...SI NO te sacaste ni un 7, ni salvaste... estás castigado".

```python
nota = float(input("¿Que nota te sacaste? "))

if nota >= 6.0:  # Ojo con los dos puntos al final (:)
    print("¡Buena, te pasaste!")
elif nota >= 4.0:
    print("Salvaste el ramo, piola.")
else:
    print("¡F total, a seguir sufriendo en la proxima!")
```
**Algo MUY importante:** Fíjense que adentro del `if` hay un espacio vacío al principio de la línea del `print` (ese espacio se llama **indentación**, que se hace con la tecla Tabulador arriba de Bloq Mayus, o dando 4 espacios). Python es extremadamente mañoso con eso. Ese espacio le dice al programa *"oye, este print va adentro del if, sólo quiero que se ejecute si se cumple la condición"*. Si lo ponen pegado a la izquierda, les va a dar un error `IndentationError`.

---

## 4. Obligar a poner bien la nota (el ciclo `while`)

Este es típico caso de prueba. Si nos piden pedirle una nota al profe, tenemos que asegurarnos sí o sí de que esté entre 1.0 y 7.0. Un `while` es un ciclo, repite el código que está adentro suyo. Acá lo usamos para decir: *"mientras la nota esté mala, sigo molestando y preguntando de nuevo"*.

```python
# iniciamos la nota con un numero falso y malo a proposito para forzar q entre al while
# si empezamos con un 5.0, el while no partiría nunca porque diría "ah, ya tá buena"
nota = -1.0

# "mientras la nota sea menor a 1.0 o (or) mayor a 7.0 haz esto..."
while nota < 1.0 or nota > 7.0:
    
    # pedimos la nota al usuario obligandolo a escribir un float (numero con punto decimal)
    nota = float(input("pon tu nota aca (entre 1.0 y 7.0): "))
    
    # si la nota efectivamente esta mala, le avisamos antes de repetir el loop
    if nota < 1.0 or nota > 7.0:
        print("error profe, nota invalida, escriba bien la nota")

# si logramos salir de las garras del while, es porque la nota era valida por fin
print("nota ingresada :)", nota)
```

---

## 5. Contar números con el `for`

El `for` es nuestro otro tipo de ciclo, pero es muy distinto. Es ultra útil cuando **ya sabemos exactamente cuántas veces queremos repetir algo**. En el `while` dependíamos de una condición sin saber cuándo iba a terminar, con el `for` es onda "repite esto 10 veces y punto".

Además acá abajo usamos el `%` (módulo), que es un truco clasico para identificar números pares en los certámenes. Este operador te pasa el resto de una división, entonces si tomas cualquier número y al dividirlo por 2 el resto sobra 0 (`i % 2 == 0`), significa que cabe justito y es par.

```python
# le preguntamos al usuario hasta dnde quiere llegar leyendo un int (numero entero, sin puntos)
limite = int(input("hasta que numero revisamos?: "))

# creamos una variable contador y la partimos en 0, pq aun no pillamos pares
pares = 0

# range(1, limite + 1) porque en python el ultimo numero del limite misteriosamente NO se incluye
for i in range(1, limite + 1):
    
    # verificamos: si el resto de dividir la i por 2 es 0 → bingo, es par
    if i % 2 == 0:
        pares += 1  # esto es lo mismito que escribir pares = pares + 1, sumarle 1 al contador
        
print(f"del 1 al {limite} pillamos {pares} numeros pares")
```

---

## 6. Hacer un menú (while + if combinados)

Los famosos menús casi siempre se hacen con la pareja de oro: un `while` grandote envolviendo varios `if`/`elif`. La idea central es que el `while` se repita infinitas veces hasta que el usuario elija la opción de salir (acá es la 3).

```python
saldo = 10000 
opcion = 0  # creamos una cajita pa guardar lo que va a elegir el usuario de a poco

# esto corre infinitamente mientras el compadre no elija la opcion 3
while opcion != 3:
    print("=== CAJERO DE MENTIRA ===")
    print("1. Sacar plata")
    print("2. Meter plata")
    print("3. Retirarse y vivir la vida")
    
    # pedimos un int porque las opciones del menu son 1, 2 o 3 (no 1.5)
    opcion = int(input("elige que vas a hacer y pon un numero: "))
    
    if opcion == 1:
        cuanto = int(input("cuanto quieres?: "))
        
        # cachar si andamos patos
        if cuanto > saldo:
            print("estay pato, no tienes plata suficiente pa este gusto")
        else:
            saldo -= cuanto  # forma corta de poner saldo = saldo - cuanto
            print("listo, te desconte la plata. saldo actual:", saldo)
            
    elif opcion == 2:
        cuanto = int(input("cuanto vay a meter?: "))
        saldo += cuanto
        print("buena, tu saldo ahora esta en:", saldo)
        
    elif opcion == 3:
        # si llegamos aca, el while se va a dar cuenta en la prox vuelta q debe apagarse
        print("nos vemooos cuidese")
        
    else:
        # por si se le ocurre escribir "5" y romper todo
        print("opcion mala! lee el menu porfa")
```

Ya ps cabros, léanlo, tómense un café, ejecuten los códigos ustedes mismos en su compu y prueben romperlos borrándole un tab o una letra.

Mucho éxito en el solemne!
