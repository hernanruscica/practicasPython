
#comentario de una linea
print("Fundamentos","Programación","en", sep = "***", end = "...")
print("Python")

"""Comentario multilinea 
en 
Python
"""

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


print("        *\n",
      "       * *\n", 
      "      *   *\n", 
      "     *     *\n", 
      "    *       *\n", 
      "   *         *\n",
      "  *           *\n", 
      " *             *\n", 
      "******     ******\n",
      "     *     *\n",
      "     *     *\n",
      "     *     *\n",
      "     *     *\n",
      "     *******\n",
      sep = "")


#print numeros hexadecimales y octales

print(0o123)
print(0x123)

#flotantes
flotante = 0.4 
flotante2 = .4 
print("comparando los flotantes", flotante == flotante2, flotante, flotante2)

#velocidad luz sin y con exponente
velocidadLuz = 300_000_000; velocidadLuzExponente = 3E8 
print("comparando la nomenclatura de exponente", 
      velocidadLuz == velocidadLuzExponente, velocidadLuz, velocidadLuzExponente)

#exponentes con flotantes
h = 6.62607E-34; flotante3 = 0.0000000000000000000001
print(h, flotante3)

#Imprimir cadenas

#con caracteres de escape
print("Me gusta \"Monty Python\"")
print("I\'m Monty Python.")

#con relaciones de comillas dobles y apostrofes
print('Me gusta "Monty Python"')
print("I'm Monty Python.")

#valores booleanos
print(True > False)
print(True < False)

#2.2.1.11 LABORATORIO: Literales de Python - Cadenas del curso de cisco
#Mostrar en pantalla lo de abajo, sin los numerales obvio...
#"Estoy"
#""aprendiendo""
#"""Python"""
print('"Estoy"\n""aprendiendo""\n"""Python"""\n')

#Funciones y algunas maneras de contener los resultados de los condicionales
TEMPERATURA_MAXIMA = 37
nombre = input("Ingrese su nombre:   ")
temperatura = input("Ingrese su temperatura:   ")
temperatura = float(temperatura)

def puedeIngresar (temperatura):    
    tieneFiebre = temperatura > TEMPERATURA_MAXIMA
    return not tieneFiebre

estadoIngreso = puedeIngresar(temperatura)

if (estadoIngreso):
    mensajeIngreso = "Usted puede ingresar"
else:
    mensajeIngreso = "Usted No puede ingresar"

print(mensajeIngreso)


#operadores aritmeticos

#potenciacion con el doble asterisco **
print(2 ** 3)

#division entera
print(6 // 4)

#modulo o resto de una division 
print (12 % 3)

#jerarquia de los operadores - el * tiene prioridad ante el + como en matematica
print(2 + 3 * 5)

#Enlazado de operadores 
#El operador tiene un enlazado del lado izquierdo.
#Las divisiones siempre devuelven flotantes
print(12 / 4 / 3)

#la exponenciacion tiene un enlazado de derecha a izquierda
print(2 ** 2 ** 3)
#2 al cubo = 8 y 2 a la 8 = 256

#operaciones con parentesis
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# (5 * (12 + 100) / (26)) // 2
# (5 * 112 / 26) // 2
# 21.53846153846154 // 2
# 10.0

#variables en python, convencion para los nombres mi_variable aunque tambien es aceptado miVariable
palabras_claves_python = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print (palabras_claves_python)
print("En python no es necesario declarar el tipo de dato, solo basta con asignarle un valor, y el tipo de dato de ese valor, sera el de la variable\n")
print("Por ejemplo:\nLa variable 'entero' no existe, con la sentencia 'entero = 1' ya la declaro con el valor y el tipo de valor.\n")
entero = 1
print("lo comprobamos usando la funcion 'type()', que nos dice que tipo de dato contiene 'entero'\nentero = " + str(entero) + " y es del tipo " + str(type(entero)))

#funcion para sacar la hipotenusa

def sacarHipotenusa(a, b):
    ladoA = a
    laboB = b
    hipotenusa = (ladoA ** 2 + laboB ** 2) ** 0.5
    return hipotenusa

def pedirCatetosYmostrarHipotenusa():
    catetoA = float(input("Ingrese el primer cateto>> "))
    catetoB = float(input("Ingrese el primer cateto>> "))    
    hipotenusaCalculado = sacarHipotenusa(catetoA, catetoB)
    print("Cateto 'A' = " + str(catetoA) + "\nCateto 'B' = " + str(catetoB) + "\nHipotenusa = " + str(hipotenusaCalculado))

pedirCatetosYmostrarHipotenusa()

"""
2.4.1.7 LABORATORIO: Variables
https://edube.org/learn/python-essentials-1-esp/laboratorio-variables-1
"""
juan = 3
maria = 5
adam = 6
print(str(juan) + "," + str(maria) + "," + str(adam))
total_manzanas = juan + maria + adam
print("numero total de manzanas = " + str(total_manzanas))

"""
2.4.1.9 LABORATORIO: Variables, un sencillo convertidor
https://edube.org/learn/python-essentials-1-esp/laboratorio-variables-un-sencillo-convertidor-1
"""
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

"""
2.4.1.10 LABORATORIO: Operadores y expresiones
https://edube.org/learn/python-essentials-1-esp/laboratorio-operadores-y-expresiones-3
"""
# programa que resuelva y = 3x3 - 2x2 + 3x - 1
x =  -1
x = float(x)
equis_cubo = 3 * (x ** 3)
equis_cuadrado =  -2 * (x ** 2) 
equis = 3 * x
independiente = -1
y = equis_cubo + equis_cuadrado + equis + independiente
print("y =", y)

# 2.6.1.7 Cómo hablar con una computadora: operadores de cadenas
# con el asterisco podemos multiplicar las cadenas..

print('*-' * 20, end = '*\n')
print(('*' + ' ' * 39 + '*\n') * 10)
print('*-' * 20, end = '*\n')


#2.6.1.9 LABORATORIO: Entradas y salidas simples
#https://edube.org/learn/python-essentials-1-esp/laboratorio-entradas-y-salidas-simples-1

# ingresa un valor flotante para la variable a aquí
valor01 = float(input('Ingrese 1er valor flotante : '))
# ingresa un valor flotante para la variable b aquí
valor02 = float(input('Ingrese 2er valor flotante : '))
# muestra el resultado de la suma aquí 
print(str(valor01) + ' + ' + str(valor02) + ' = ' + str(valor01 + valor02))
# muestra el resultado de la resta aquí
print(str(valor01) + ' - ' + str(valor02) + ' = ' + str(valor01 - valor02))
# muestra el resultado de la multiplicación aquí
print(str(valor01) + ' * ' + str(valor02) + ' = ' + str(valor01 * valor02))
# muestra el resultado de la división aquí
print(str(valor01) + ' / ' + str(valor02) + ' = ' + str(valor01 / valor02))
print("\n¡Eso es todo, amigos!")

#2.6.1.10 LABORATORIO: Operadores y expresiones
#https://edube.org/learn/python-essentials-1-esp/laboratorio-operadores-y-expresiones-4
x = float(input("Ingresa el valor para x: "))
# Escribe tu código aquí.
y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))
print("y =", y)


#2.6.1.11 LABORATORIO: Operadores y expresiones
#https://edube.org/learn/python-essentials-1-esp/laboratorio-operadores-y-expresiones-5
horas=int(input("Hora de inicio (horas): "))
minutos=int(input("Minuto de inicio (minutos): "))
duracion=int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#datos de prueba
#horas = 23; minutos = 58; duracion = 642
horasDia = 24
minutosHora = 60

minutos += duracion
horasQueMePase = minutos // minutosHora
minutos = minutos % minutosHora

horas += horasQueMePase
horas = horas % horasDia

print('El evento termina a las ' + str(horas) + ' : ' +str(minutos))

print(4 % 11)

x=11
y=4

x = x % y
x = x % y
y = y % x

print(y)

x=1
y=2
z = x 
x = y
y = z
print(x, y)

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

x = 2
y = 4
x = x / y
y = y / x
print(y)

z = y = x = 1
print(x, y, z, sep = "*")

y = 2 + 3 * 5
print(Y)

print(12%0)

x = 2
y = 4
x = x // y
y = y // x
print(y)


#3.1.1.9 Tomando decisiones en Python
# Se leen tres números.

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
numero01 = int(input("Ingrese el primer numero: "))
numero02 = int(input("Ingrese el segundo numero: "))
numero03 = int(input("Ingrese el tercer numero: "))

largest_number = max(numero01, numero02, numero03)
# Imprime el resultado.
print("El número más grande es:", largest_number)


#3.1.1.10 LABORATORIO: Operadores de comparación y ejecución condicional
cadena = input("Ingrese cadena: ")
if cadena == 'ESPATIFILIO':
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
elif cadena == 'espatifilo':
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No " + cadena + "!")


#3.1.1.11 LABORATORIO: Fundamentos de la sentencia if-else
ingreso = float(input("Introduce el ingreso anual:"))
ingreso_limite = 85528
if (ingreso <= ingreso_limite):
    impuesto_a_pagar = (ingreso * 0.18) - 556.02
else:
    impuesto_a_pagar = 14839.02 + 0.32 * (ingreso - ingreso_limite)
impuesto_a_pagar = round(impuesto_a_pagar, 0)
print("El impuesto es:", impuesto_a_pagar, "pesos")


#3.1.1.12 LABORATORIO: Fundamentos de la sentencia if-elif-else
#codigo que tiene que mostrar si un año es bisiesto o no.
anio = int(input("Introduce un año:"))#
# Escribe tu código aquí.
es_bisiesto = False
"""
Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común.
De lo contrario, es un año bisiesto.
"""
def es_bisiesto(anio):
    if (anio % 4 != 0):
        es_bisiesto = False
    elif (anio % 100 != 0):
        es_bisiesto = True
    elif (anio % 400 != 0):
        es_bisiesto = False
    else:
        es_bisiesto = True
    return es_bisiesto

if (anio < 1582):
    respuesta = "No dentro del período del calendario Gregoriano"
else:
    es_bisiesto_respuesta = es_bisiesto(anio)
    if (es_bisiesto_respuesta):
        respuesta = "Año Bisiesto"
    else:
        respuesta = "Año Común"
print(respuesta)

#3.2.1.2 Bucles en Python | while
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

cantidad_pares = 0
cantidad_impares = 0

# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while numero: #numero != 0
    # Verificar si el número es impar.
    if numero % 2: #numero % 2 == 1
        # Incrementar el contador de números impares odd_numbers.
        cantidad_impares += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        cantidad_pares += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", cantidad_impares)
print("Cuenta de números pares:", cantidad_pares)


#3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto
numero_secreto = 777
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numeroEnteroElegido = int(input("Ingrese un numero entero"))
while numeroEnteroElegido != numero_secreto :
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numeroEnteroElegido = int(input("Ingrese un numero entero"))
print("¡Bien hecho, muggle! Eres libre ahora")



#3.2.1.5 Bucles en Python | for
for i in range(3):
    print("tres primeros: " + str(i))    
for j in range(4, 9):
    print("de cuatro a ocho, posicion: " + str(j))
for k in range(8, 20, 2):
    print("numeros pares, posicion: " + str(k))
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2



#3.2.1.6 LABORATORIO: Fundamentos del bucle for: el conteo
import time

    # Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle - usar: time.sleep (1)

# Escribe una función de impresión con el mensaje final.
for i in range(1, 6):
    print(str(i) + " Mississippi")
    time.sleep(1)

#3.2.1.7 Control de bucles en Python | break y continue
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        continue #"break" y "continue" son las instrucciones que rompen el ciclo
        #break rompe todo el ciclo "for" y continue saltea esa iteracion del ciclo
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


#3.2.1.8 Control de bucles en Python | break y continue
#con break se puede hacer un ciclo que entre siempre, y que salgo cuando queramos con la sentencia break
contador_iteraciones = 0
numeroIteracionesMax = 5
while True :    
    if (contador_iteraciones == numeroIteracionesMax):        
        break
    print("iteracion " + str(contador_iteraciones) + " dentro del while")
    contador_iteraciones += 1
print("fuera del while")


#3.2.1.9 LABORATORIO: La sentencia break - Atascado en un bucle
"""
Escenario
La instrucción break se implementa para salir/terminar un bucle.
Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" 
como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el bucle con éxito". Debe imprimirse en la pantalla y el bucle debe terminar.
No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.
"""

print("'chupacabra' para salir\n")
palabra_secreta = "chupacabra"
while True :
    palabra_ingresada = str(input("Ingrese una palabra:"))
    if (palabra_ingresada == palabra_secreta):
        print("¡Has dejado el bucle con éxito")
        break

#3.2.1.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales
"""
Escenario
La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.
Se puede usar tanto con while y for.
Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La sentencia continue.
Tu programa debe:
Pedir al usuario que ingrese una palabra.
Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, 
no te preocupes.
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
Prueba tu programa con los datos que le proporcionamos.
"""

palabra_ingresada = str(input("Ingrese una palabra:  "))
palabra_ingresada_mayusculas = palabra_ingresada.upper()

for letra in palabra_ingresada_mayusculas:
    if (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'): continue
    else: print(letra + '\n')



#3.2.1.11 LABORATORIO: La sentencia continue - El Bonito Devorador de Vocales
"""
Escenario
Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior (3.1.2.10) y crear un mejor devorador de vocales (bonito) mejorado! 
Escribe un programa que use:
Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La instrucción continue.
Tu programa debe:
Pedir al usuario que ingrese una palabra.
Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, 
no te preocupes.
Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las 
letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.
Prueba tu programa con los datos que le proporcionamos.
"""

palabra_sin_vocales = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
palabra_ingresada = str(input("Ingrese una palabra:  "))
palabra_ingresada_mayusculas = str(palabra_ingresada.upper())


for letra in palabra_ingresada_mayusculas:
    if (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'): continue
    else: palabra_sin_vocales = palabra_sin_vocales + letra
print("Antes   del devorador de vocales: " + palabra_ingresada)
print("despues del devorador de vocales: " + palabra_sin_vocales)

#3.2.1.12 Bucles while en Python | else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#3.2.1.13 Bucles for en Python | else
i = 10
for i in range(5,1):
    print(i)
else:
    print("else:", i)



#3.2.1.14 LABORATORIO: Fundamentos del bucle while

"""
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.
Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. 
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
La figura ilustra la regla utilizada por los constructores:
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, 
terminan su trabajo inmediatamente.
Prueba tu código con los datos que hemos proporcionado.
"""

cantidad_bloques_piso_actual = 1
bloques = int(input("Ingresa el número de bloques: "))
tengo_bloques_suficientes = (bloques - cantidad_bloques_piso_actual) > cantidad_bloques_piso_actual 
contador_pisos = 1
if tengo_bloques_suficientes: contador_pisos += 1

while tengo_bloques_suficientes:     
    bloques = bloques - cantidad_bloques_piso_actual
    cantidad_bloques_piso_actual += 1
    tengo_bloques_suficientes = (bloques - cantidad_bloques_piso_actual) > cantidad_bloques_piso_actual
    if tengo_bloques_suficientes: contador_pisos += 1

print("La altura de la piramide es: " + str(contador_pisos))

"""
Datos de prueba:
Entrada de muestra: 6
Salida esperada: La altura de la pirámide es: 3
------------------------------------------------
Entrada de muestra: 20
Salida esperada: La altura de la pirámide es: 5
----------------------------------------------------
Entrada de muestra: 1000
Salida esperada: La altura de la pirámide es: 44
---------------------------------------------------
Entrada de muestra: 2
Salida esperada: La altura de la pirámide es: 1
"""



