
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


#imprime todos los caracteres antes del @ en una misma linea, 
# gracias a la variable 'end', porque asi no pone el '/'
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "") 


#Crea un programa con un bucle for y una sentenciacontinue. 
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        print("x", end = "")
        continue
    print(digit, end = "")

"""
Operaciones lógicas y de bits en Python
diferencias entre estos dos tipos de operaciones de comparacion
"""

entero_1 = 15
entero_2 = 22
resultado_operacion_logica = entero_1 & entero_2
print(resultado_operacion_logica)

"""
-----------------------------------------------
            LISTAS O ARRAYS
-----------------------------------------------
"""

#3.4.1.3 Listas - colecciones de datos | Indexación

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.
numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.
print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

#3.4.1.4 Listas - colecciones de datos | Operaciones en listas

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

#No puedes acceder a un elemento que no existe , no puedes obtener su valor ni asignarle un valor. 
# Ambas instrucciones causarán ahora errores de tiempo de ejecución: print(numbers[4]) O numbers[4] = 1

#3.4.1.5 Listas - colecciones de datos | Operaciones en listas

#Los valores negativos en los indices de las listas SON validos.
print("El ultimo elemento de la lista es: ", numbers[-1]) #Con -1 se muestra el ultimo elemento
print("El AnteUltimo elemento de la lista es: ", numbers[-2]) #con -2 se muestra el alteultimo elemento
# y asi con todos hasta llegar al 1er elemento, donde se terminan los indices negativos.


#3.4.1.6 LABORATORIO: Lo básico de las listas

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# Paso 1: escribe una línea de código que solicite al usuario
numero_entero = int(input("Ingrese un numero entero para reemplazar en el medio: "))

# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2] = numero_entero

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista de sombreros es ",len(hat_list))
print("La lista es: ", hat_list)



#3.4.1.8 Listas - colecciones de datos | Métodos de listas
#Los metodos de las listas: append e insert

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)

print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

#3.4.1.9 Listas - colecciones de datos | Métodos de listas

# Creando mis listas vacías.
mi_lista = []
mi_lista_inversa = []  

for i in range(5):
    #append agrega el nuevo valor al final de la lista, obteniendo [1,2,3,4,5]
    mi_lista.append(i + 1)
    #insert agrega el nuevo valor (2do parametro) en la posicion indicada en el primer parametro
    mi_lista_inversa.insert(0, i + 1)
print("mi lista original: ", mi_lista)
print("mi lista inversa : ", mi_lista_inversa)

#3.4.1.10 Listas - colecciones de datos | Listas y bucles
#formas de recorrer una lista, de forma parecida al forEach de javascript
total = 0
longitud_mi_lista = len(mi_lista)
for i in range(longitud_mi_lista):
    total += mi_lista[i]
print("Sumatoria de mi lista original: ", total)
total = 0
for i in mi_lista_inversa:
    total += i
print("Sumatoria de mi lista inversa : ", total)

#3.4.1.12 Listas - colecciones de datos | Listas y bucles
#Intercambiando valores de variables y de elementos de listas

mi_lista02 = [8, 4, 10, 12, 11]
#hago el intercambio sin tener que tener una variable intermedia.
#variable01, variable02 = variable02, variable01
mi_lista02[0], mi_lista02[1] = mi_lista02[1], mi_lista02[0]
mi_lista02[3], mi_lista02[4] = mi_lista02[4], mi_lista02[3]
print("Mi lista ordenada es : ", mi_lista02)


#Abajo otro ejemplo pero para intercambiar el orden de toda una lista...
mi_lista = [10, 1, 8, 3, 5]
longitud = len(mi_lista) #1 
for i in range(longitud // 2): #2 
    principio_lista = i
    final_lista = longitud - i - 1
    mi_lista[principio_lista], mi_lista[final_lista] = mi_lista[final_lista], mi_lista[principio_lista]
print(mi_lista)
"""
#1 Hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto).

#2 Hemos preparado el bucle "for" para que se ejecute su cuerpo longitud // 2 veces (esto funciona bien para listas con longitudes pares e impares, 
porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto).

Hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length-i-1) (desde el final de la lista); 
en nuestro ejemplo, for i igual a 0 a la (length-i-1) da 4; for i igual a 3, da 3: esto es exactamente lo que necesitábamos.
"""


#3.4.1.13 LABORATORIO: Lo básico de las listas - Los Beatles
# paso 1
Beatles = []
print("Paso 1:", Beatles)
# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)
# paso 3
otros_integrantes = ["Stu Sutcliffe", "Pete Best"]
otros_integrantes_longitud = len(otros_integrantes)
for i in range(otros_integrantes_longitud):
    nuevo_integrante = input("Ingrese a " + otros_integrantes[i] + " : ")
    Beatles.append(nuevo_integrante)    
print("Paso 3:", Beatles)
# paso 4
for i in range(otros_integrantes_longitud):
    del Beatles[-1]
print("Paso 4:", Beatles)
# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)
# probando la longitud de la lista
print("Los Fav", len(Beatles))

#Las listas pueden ser iteradas mediante el uso del bucle for, por ejemplo:
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
for color in my_list:
    print(color)


#3.5.1.2 Ordenando listas simples - el ordenamiento de burbuja

#mi_lista = [8, 10, 6, 2, 4]  # lista a ordenar
#mi_lista = [1, 10, 11, 12, 14]  # lista a ordenar
mi_lista = [103, 88, 90, 6, 20, 45, 11, 66, 54, 3, 8, 12, 1]
mi_lista_longitud = len(mi_lista)
cantidad_comparaciones = mi_lista_longitud - 1
cantidad_pasadas = 0
hubo_intercambio = False

print("mi_lista original: ", mi_lista)

while hubo_intercambio or cantidad_pasadas == 0:

    hubo_intercambio = False
    # necesitamos (5 - 1) comparaciones para recorrer toda la lista
    for i in range(cantidad_comparaciones):  
        elem_actual = i
        elem_siguiente = i + 1
        # compara elementos adyacentes
        if mi_lista[elem_actual] > mi_lista[elem_siguiente]:  
            # Si terminamos aquí, tenemos que intercambiar elementos y poner a hubo_intercambio en 'True'.
            mi_lista[elem_actual], mi_lista[elem_siguiente] = mi_lista[elem_siguiente], mi_lista[elem_actual] 
            hubo_intercambio = True        
    cantidad_pasadas += 1
    print("mi_lista despues de ", str(cantidad_pasadas), " pasada: ", mi_lista, hubo_intercambio)

#probando la funcion integrada sort
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#Puntos Clave del capitulo de las listas

#1. Puedes usar el método sort() para ordenar los elementos de una lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]

#2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  # salida: [4, 2, 1, 3, 5]


#3.6.1.1 Operaciones en listas

#Como python copia una lista (arreglo), cuando hacemos: 
#creamos una lista con un elemento
lista01 = [2]
#creamos una nueva lista con los elementos de la lista01???
lista02 = lista01
#cambiamos el unico elemento de la lista01
lista01[0] = 1
#mostramos las dos listas
print("lista01: ", lista01, "\nlista02: ", lista02)
#sorprendentemente cambiaron las dos listas, lo que nos muestra que python no copio los elementos de lista01 dentro de lista02 en la linea 8.
#Sino que copio la direccion de memoria de esa lista a la "nueva" lista02, que en realidad es una variable que hace referencia a la lista01

#3.6.1.2 Operaciones en listas - rebanadas
"""
permite hacer una copia nueva de una lista, o partes de una lista.
Ejemplo generico: my_list[start:end] 
si se omite el start o el end se supone que empieza desde el 1er elemento o el ultimo respectivamente.
"""
#creo un lista con 4 elementos
mi_lista01 = [0, 1, 2, 3]
#creo una lista nueva y le copio los elementos de la lista01
mi_lista02 = mi_lista01[:]
#invierto el orden de la lista01
mi_lista01.reverse()
#tambien se puede cortar parte de una lista y copiarla en otra, my_list[start:end] 
# agarra desde el elemento start hasta el elemento en el indice end-1
mi_lista03 = mi_lista02[1:4]
#muestro las tres listas, y funcionan completamente independientes.
print("mi_lista01: ", mi_lista01, "\nmi_lista02: ", mi_lista02, "\nmi_lista03: ", mi_lista03)

#usando la funcion 'del' en combinacion con [:]
del mi_lista02[:1]
print("mi_lista02 cortada: ", mi_lista02)
#Tambien puedo borrar todos los elementos de la lista, sin borrar la lista
del mi_lista01[:]
print("mi_lista01 vaciada: ", mi_lista01)

# 'in', 'not in'. Buscan si existe un valor determinado en una lista, la operacion devuelve un booleano.
tiene_un_dos = 2 in mi_lista02
if tiene_un_dos: print(mi_lista02, " --> mi_lista02 tiene un dos") 
else:  print(mi_lista02, " --> mi_lista02 NO tiene un dos") 
colores = ["rojo", "amarillo", "blanco"]
tiene_rojo = "rojo" in colores
tiene_verde = "verde" in colores
print(colores)
print("tiene rojo? ", tiene_rojo)
print("tiene verde? ", tiene_verde)


#3.6.1.7 Listas - más detalles
#Programa que busca el elemento mas grande de una lista 

mi_lista = [17, 3, 11, 5, 1, 9, 7, 45, 13]
el_mas_grande = mi_lista[0]

#Tambien podria empezar por el 2do elemento, ya que la 1er comparacion es innecesaria
# for elemento in mi_lista[1:] 
for elemento in mi_lista: 
    if elemento > el_mas_grande:
        el_mas_grande = elemento
print("el mas grande de la lista es: ", el_mas_grande)


#3.6.1.8 Listas - más detalles
#Ahora encontremos la ubicación de un elemento dado dentro de una lista:

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_buscado = 11
encontrado = False
mi_lista_longitud = len(mi_lista)

for i in range(mi_lista_longitud):
    elemento = mi_lista[i]
    encontrado = elemento == numero_buscado    
    if encontrado:
        encontrado_indice = i
        break

print("mi_lista: ", mi_lista)
if encontrado:
    print("Numero ", numero_buscado, " encontrado en la posicion ", encontrado_indice)
else:
    print("Numero ", numero_buscado, " NO encontrado")


#3.6.1.8 Listas - más detalles
#jugaste a la loteria, la pregunta es: ¿A cuántos números le has atinado?

numeros_sorteados = [5, 11, 9, 42, 3, 49]
#numeros_apostados = [3, 7, 11, 42, 34, 49]
numeros_apostados = [1, 34, 21, 5]
numeros_acertados = []
aciertos = 0

for apostado in numeros_apostados:
    if apostado in numeros_sorteados:
        aciertos += 1
        numeros_acertados.append(apostado)
print(aciertos, " aciertos.")
if aciertos > 0:
    print("Acertaste: ", numeros_acertados)


#3.6.1.9 LABORATORIO: Operando con listas - conceptos básicos
"""
Escribir un programa que elimine todas las repeticiones de números de la lista. 
El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
"""
mi_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#copio mi lista a una lista temporal
lista_temporal = mi_lista[:]
#vacio la lista, es decir elimino todos los elementos, pero no borro la lista
del mi_lista[:]
#recorro todos los elementos en la lista temporal y agrego a mi lista solo los que no fueron ya agregados
for elemento in lista_temporal:
    if elemento not in mi_lista:
        mi_lista.append(elemento)

print("La lista con elementos únicos:")
print(mi_lista)


#3.7.1.1 Listas en aplicaciones avanzadas
"""
comprensión de lista. Es la sintaxis especial utilizada por Python para completar o llenar listas masivas.
Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha durante la ejecución del programa, 
y no se describe de forma estática.
"""
#por ejemplo:
fila_dinamica = ["Naranjas" for i in range(8)]
print(fila_dinamica)

#Usando una variable
potencias_dedos = [2 ** x for x in range(7)]
print(potencias_dedos)
impares = [numero for numero in range(10) if numero % 2 != 0]
print(impares)


#3.7.1.2 Listas en aplicaciones avanzadas

#Piezas del juego
EMPTY = "XXXXXXX"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"

#Elementos del tablero
tablero = []
COLUMNAS = 8
FILAS = 8

"""
for i in range(8):
    fila = [EMPTY for j in range(8)]
    tablero.append(fila)
"""
#forma abreviada, funciona igual que el for de arriba.
tablero = [[EMPTY for i in range(FILAS)] for j in range(COLUMNAS)]

#colocamos piezas en el tablero
tablero[0][0] = ROOK
tablero[0][7] = ROOK
tablero[7][0] = ROOK
tablero[7][7] = ROOK


print(tablero)
#mostrar_tablero()

#3.7.1.4 Listas en aplicaciones avanzadas 
#matrices bidimensionales - Ejemplo de temperaturas

temperaturas = [[hora + 0.0 for hora in range(24) ] for dia in range(31)]


#sacamos un promedio mensual de la temperatura al mediodia
"""
La matriz tiene 31 filas (dias) de 24 columnas (horas)
recorremos las 31 filas y de cada una de ellas, tomamos el valor de la posicion 11 (12Hs.)
"""
hora = 12
sumatoria_temperaturas = 0
for dia in temperaturas:
    sumatoria_temperaturas += dia[hora - 1]
print("Promedio de temperaturas a las 12 hs es de: ", str(sumatoria_temperaturas / 31))

#La variable day itera en todas las filas de la matriz temps.
#La variable temp itera a través de todas las mediciones tomadas en un día.
temperatura_mas_alta = -300
for dia in temperaturas:
    for temperatura in dia:
        if temperatura > temperatura_mas_alta:
            temperatura_mas_alta = temperatura
print("La temperatura mas alta fue: ", temperatura_mas_alta)


#3.7.1.5 Listas en aplicaciones avanzadas
"""
Arreglos tridimensionales
Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. 
Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar 
y procesar información sobre las habitaciones ocupadas/libres.
"""

habitaciones = [[[False for habitacion in range(20)] for piso in range(15)] for edificio in range(3)]

#Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:

#empiezan a contar en 0
edificio = 1
piso = 9
habitacion = 13
habitaciones[edificio][piso][habitacion] = True
