
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
horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

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