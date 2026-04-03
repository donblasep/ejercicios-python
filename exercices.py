""" aca veran ejercicios sin respuestas, en las cuales pueden ejercitar su logica y forma de programar
este sera un archivo unico donde se vera una especie de "tutorial" de que es cada funcion y como funciona, seguido
de un par de ejercicios que pueden usar para entrenar, prueben distintas formas de responder un mismo problema """

"""variables: estas son valores definidos por el programador para hacer uso futuro de ellos, estos valores pueden ir desde un numero, una cadena de texto
o incluso operaciones, una variable se define asi:
"nombre de la variable" = "valor" """

"""funcion print()
print es lo mas basico en python, imprime un valor en pantalla, usando los siguientes parametros
print(<valor a imprimir>)"""
#ejemplo:

print("Hola") 
print(8)
#como se puede ver, uno de estos valores esta entre "", el siguiente punto a explicar seran los tipos de dato
"""existen varios tipos de dato, entre ellos los siguientes:
string (str): cadena de texto, palabras o parrafos de texto
integer (int): numero entero, cualquier numero sin incluir valores decimales
float: numero decimal, cualquier numero incluyendo decimal, si el numero no tiene decimal, este valor sera demostrado con un .00 al final
booleano (bool): condicion de verdadero / falso, retorno de True o False
character (char): un caracter simple, una letra, normalmente no es usado por python, ya que se considera un string directamente, no existe
un comando para transformarlo a char"""


int()
str()
float()
bool()


"""comando "Input", este comando pide un valor ingresado por consola al usuario, se usa de la siguiente forma:
"Variable" = Input(<valor a solicitar>) el Input puede estar vacio, pero normalmente se suele especificar que dato estamos buscando"""


"""operadores basicos, estos son los operadores basicos y sus significados:
== (igual a)
+ (suma)
- (resta)
/ (division)
* (multiplicacion)
% (resto)

pdt: el resto funciona de la siguiente manera; "valor"%"parametro", se divide el numero de forma entera (sin decimales), el resto de la multiplicacion
(ej: 2/2 = 0, ya que es division exacta, pero, 3/2 = 1, ya que el resto de la division es 1 al no poder seguir dividiendo sin usar decimales)"""

# Ejercicio N1: crear un sistema que multiplique, divida, reste o sume dos parametros ingresados por el usuario (x [*./.-.+] y) no ocupar mas de 2/3 lineas de codigo...






""" condicionales: son comandos que determinan que una condicion impuesta por el programador sea verdadera o falsa,
comandos condicionales:
if: comprueba la condicion
uso: if "parametro 1" "condicion" "parametro 2":
    "codigo"
elif: comprueba una condicion si la anterior no fue verdadera
else: si ninguna condicion anterior es verdadera, se ejecuta este codigo
"""

#Ejercicio N2: crear un sistema en el cual compruebe si un valor numerico es mayor a otro, no ocupar mas de 7 u 8 lineas








"""ciclos: repiten el bloque de codigo que les es asignado determinada cantidad de veces, por ahora, hemos aprendido 2 tipos de ciclo:
while: se repite siempre y cuando una condicion sea verdadera, es decir, es un ciclo condicional
for: se en un rango determinado, es decir, un ciclo de rango

uso de for:
for "parametro x" in "rango" / "range(min, max, intervalo)"
"""

#Ejercicio N3: crear un ciclo while que sume un numero de 1 en 1 100 veces, en no mas de 7 lineas







""" Ejercicio N4: Un contador de entrenamiento

 Eres el entrenador de un atleta y necesitas un programa que registre
 su progreso durante una sesión de ejercicio.
 El programa debe:
 1. Preguntar al usuario cuántas repeticiones hará el atleta
 2. Preguntar con cuántos kilos empieza
 3. Por cada repetición, el peso aumenta 2.5 kilos
 El programa debe mostrar por cada vuelta:
 - En qué repetición va el atleta (ej: "Repetición 1 de 10")
 - Con cuántos kilos está levantando en esa repetición

 Ejemplo de output esperado con 3 repeticiones y 10 kilos iniciales:
 Repetición 1 de 3 | Peso: 12.5 kg
 Repetición 2 de 3 | Peso: 15.0 kg
 Repetición 3 de 3 | Peso: 17.5 kg

 intenta no usar mas de 20 lineas de codigo...
 """







# si necesitas ayuda con algun ejercicio, o no comprendes la problematica, consulta a quien quieras que creas que pueda ayudarte, al recibir ayuda 
# recuerda centrarte en comprender la logica, mas allá de copiar la respuesta


#pdt: este es el bloque 1 de resumen de conocimientos, el siguiente codigo será un resumen de otro bloque de contenidos aprendidos en clase