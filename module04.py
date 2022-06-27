"""
Fundamentos de Python 1
Módulo 4
Funciones, Tuplas, Diccionarios, Exceptiones y Procesamiento de Datos

En este módulo, se cubrirán los siguientes temas:

Estructuración de código y el concepto de función.
Invocación de funciones y devolución de resultados de una función.
Alcance de nombres y sombreado de variables.
Tuplas y su propósito: construcción y uso de tuplas.
Diccionarios y su propósito: construcción y uso de diccionarios;
Introducción a las excepciones en Python.
"""
#4.1.1.1 Funciones
"""
-No se debe invocar una función antes de que se haya definido.
    Recuerda: Python lee el código de arriba hacia abajo. 
    No va a adelantarse en el código para determinar si la función invocada está definida más adelante, 
    el lugar correcto para definirla es antes de ser invocada.
-Una función y una variable no pueden compartir el mismo nombre.
    El asignar un valor al nombre "message" causa que Python olvide su rol anterior. 
    La función con el nombre de message ya no estará disponible.
"""
def mi_function(parametros_opcionales):
    print("Hola ", parametros_opcionales)
mi_function("Hernan")

def pedir_datos(nombre, numero):
    print("Ingresa ", nombre, " Num.", numero)
    
pedir_datos("Telefono", 1)

"""
4.2.1.5 Cómo las funciones se comunican con su entorno
    En python ademas del paso de parametros en forma posicional,
    se pueden pasar con el nombre del parametro
"""
def presentacion(primer_nombre, apellido):
    print("Hola, mi nombre es ", primer_nombre, apellido)

presentacion(primer_nombre = "hernan", apellido = "ruscica")

#4.2.1.6 Cómo las funciones se comunican con su entorno
#parametros posicionales, mezclados con palabras claves

def sumando(a, b, c):
    print(a, " + ", b, " + ", c, " = ", a + b + c)
sumando(1, 2, 3)
sumando(1, c = 3, b = 2)

#4.2.1.7 Cómo las funciones se comunican con su entorno
#funciones con argumentos con valores predefinidos.

def presentacion(nombres, apellido = "Gonzalez"):
    print("Hola, mi nombre es ", nombres, apellido)
presentacion("Ezequiel")
presentacion("Hernan", "Ruscica")



#4.3.1.1 Regresando el resultado de una función
#Uno de los casos es usar el return sin argumento, simplemente para salir de la funcion y no devolver nada...
def paseo_con_sol(hay_sol):
    if not hay_sol:
        return
    print("Salimos a pasear")
paseo_con_sol(False)

a = 1
b = 2
c = 4
d = 3

#Devolviendo un valor
def sumar(a, b):
    return a + b
resultado_suma = sumar(a, b)
print("Resultado de la suma: ", resultado_suma)

#Devolviendo un valor
def se_puede_restar(c, d):
    if c >= d:        
        return True
    return False

if se_puede_restar(c, d) == True:
    print("El resultado de la resta es: ", c - d)
else:
    print("No se pudo restar.")

#4.3.1.2 Regresando el resultado de una función
"""
None es una palabra clave reservada.
    Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
    Cuando se compara con una variable para diagnosticar su estado interno.
"""
value = None
if value is None:
    print("Lo siento, no contienes ningún valor")

#4.3.1.3 Ahora un ejemplo de una funcion que a veces no tiene que devolver 
#entonces devuleve None

def funcion_extrania(n):
    if(n % 2 == 0):
        return True

print(funcion_extrania(2))
print(funcion_extrania(1))


#4.3.1.4 Regresando el resultado de una función, recibiendo una lista
#Una función como la siguiente:

def suma_lista(lista):
    sumador = 0    
    for elemento in lista:
        sumador += elemento    
    return sumador
#y se invoca así:
print(suma_lista([5, 4, 3]))


#4.3.1.5 Regresando una lista como resultado de una función
def lista_extrania_divertida(n):
    listra_extrania = []
    
    #inserta siempre en el indice 0
    for i in range(0, n):
        listra_extrania.insert(0, i)
    
    return listra_extrania

print(lista_extrania_divertida(5))


#4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones

def es_anio_bisiesto(year):
#devuelve la evaluacion de las condiciones de año bisiesto
#que el año sea divisible por 4, que no sea divisible por 100 y que sea divisible por 400 
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

#esta parte prueba los resultados de la funcion con los resultados esperados segun los datos de prueba.
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = es_anio_bisiesto(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")



#4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones

#funcion del ejercicio anterior
def es_anio_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def dias_en_mes(anio, mes):
    #cantidad de dias por mes. Indice 0 = enero
    cantidad_dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    #si el numero de mes no tiene sentido, en el anio pienso que se puede poner negativos y positivos sin un limite.
    if mes <= 0 or mes > 12:
        return None    
    if mes == 2 and es_anio_bisiesto(anio) == True:
        return 29
    return cantidad_dias_mes[mes - 1]


#pruebas
test_years = [1900, 2000, 2016, 1987, 2000, 1933]
test_months = [2, 2, 1, 12, 13, 0]
test_results = [28, 29, 31, 31, None, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = dias_en_mes(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")




#4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones
#funciones de los ejercicios anteriores
from datetime import datetime

def es_anio_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def dias_en_mes(anio, mes):
    #cantidad de dias por mes. Indice 0 = enero
    cantidad_dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    #si el numero de mes no tiene sentido, en el anio pienso que se puede poner negativos y positivos sin un limite.
    if mes <= 0 or mes > 12:
        return None    
    if mes == 2 and es_anio_bisiesto(anio) == True:
        return 29
    return cantidad_dias_mes[mes - 1]


def dia_del_anio(anio, mes, dia):
    """
    if mes < 1 or mes > 12 :
        return None
    """    
    nombres_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    cantidad_dias_mes_actual = dias_en_mes(anio, mes)
    if cantidad_dias_mes_actual == None :
        return None
    
    if dia < 1 or dia > cantidad_dias_mes_actual :
        return None
    
    #si llega hasta aca, es que los datos estan bien
    contador_dias = 0
    mes_actual = 1
    #sumo los meses completos
    while mes_actual < mes :
        print(mes_actual)
        contador_dias += dias_en_mes(anio, mes_actual)
        mes_actual += 1
    #sumo los dias del mes actual
    contador_dias += dia
    
    #muestro el nombre del dia de la semana
    #faltaria armar el string por si estan fuera del formato aaaa/mm/dd
    fecha = str(dia) + '/' + str(mes) + '/' +  str(anio)
    fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
    numero_dia_semana = fecha_dt.weekday()
    nombre_del_dia = nombres_dias[numero_dia_semana]
    
    return [contador_dias, nombre_del_dia]

#anio mes dia
resultado = dia_del_anio(2022, 7, 10)
print(resultado)
"""
Habria que adaptarlas pruebas para los dos valores que retorna.

#pruebas 
test_years = [2000]
test_months = [12]
test_results = [31]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = dia_del_anio(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
"""


#4.3.1.9 LABORATORIO: Números primos: ¿Cómo encontrarlos?
def es_primo(numero):

# Escribe tu código aquí.
    if numero == 2 : return False
    inicio = 2
    final = numero - 1
    for elemento in range(inicio, final) :
        es_divisible = numero % elemento == 0 
        if es_divisible == True :
            return False
        
    return True
#Escribe tu código aquí.


for i in range(1, 20):
	if es_primo(i + 1):
			print(i + 1, end=" ")
print()


"""
Los Alcances de las variables - SCOPEs
"""

#4.4.1.1 Una variable declarada dentro de una funcion y la llamo fuera...ERROR
def scope_test():
    #Esta x existe, porque se declaro dentro de la funcion y se llama dentro tambien
    x = 123
    print(x)
scope_test()
#Esta x no existe en este ambito
#print(x)


#4.4.1.2 Una variable declarada fuera de una funcion y llamada dentro
def my_function():
    print("¿Conozco a la variable?", var)
var = 1
my_function()
print(var)

#Hacemos un pequenio cambio en la funcion. Las dos variables se llaman igual, pero son distintas.
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
var = 1
my_function()
print(var)


#4.4.1.3 Las variables declaradas con la palabra clave "GLOBAL"
"""
1. Se declara "var = 1"
2. llama a la funcion, dentro de la funcion declara "global var = 2"
3. Sale de la funcion e imprimi "var" de nuevo, pero esta vez modificada
"""
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)
var = 1
my_function()
print(var)


#Otro ejemplo, definiendo mi variable global desde afuera de la funcion

#1. defino la variable como global, le asigno un valor y la muestro
global mi_variable_global
mi_variable_global = 22
print(mi_variable_global)

#3. Dentro de la funcion, cambio el valor de la variale global
#para hacer referencia a ella tengo que volver a poner la palabra reservada "global"
def my_function():        
    global mi_variable_global
    mi_variable_global = 33

#2. llamo a una funcion
my_function()
print(mi_variable_global)



#4.4.1.4 Los Alcances en Python y como interactua con los argumentos

#3. Dentro la funcion modifica el argumento
def my_function(n):
    print("Yo recibí", n, " (Dentro de la funcion) ")
    n += 1
    print("Ahora tengo", n, " (Dentro de la funcion) ")

#1. defino una variable
var = 1
#2. la paso como argumento a un funcion
my_function(var)
#4. a pesar de cambiar el argumento dentro de la funcion, la variable sigue siendo la misma.
print("var = ", var , " (Fuera de la funcion) ")


"""
Si bien, el resultado del ejemplo anterior podria resultar obvio. 
Vale la pena revisar cómo funciona esto con las listas 
(¿Recuerdas las peculiaridades de asignar rebanadas de listas en lugar de asignar la lista entera?)

"""
#2. dentro de la funcion borro el primer elemento del argumento lista pasado
def mi_funcion(mi_lista_argumento):
    del mi_lista_argumento[0]
    print(mi_lista_argumento, " mi lista argumento dentro de la funcion")

#1. mi lista con dos elementos
mi_lista_2 = [1, 2]
print(mi_lista_2, " mi lista 2 ANTES y fuera de la funcion")

mi_funcion(mi_lista_2)

#3. el cambio dentro de la funcion, afecta a la lista original...
print(mi_lista_2, " mi lista 2 fuera de la funcion")




#4.5.1.2 Creando funciones con dos parámetros

#dos funciones para las conversiones
def pies_pulgadas_a_metros(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def libras_a_kilos(lb):
    return lb * 0.45359237

#calcula el indice de masa corporal. valores en kilos y metros
def imc(peso, altura):
    #condiciones con la \ hago que la linea continue en el reglon de abajo
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    return peso / altura ** 2

def pedir_datos(sistema_medida):
    datos = []    
    if sistema_de_medida == 1 :        
        datos.append(float(input("Ingrese su peso en Kilogramos: ")))
        datos.append(float(input("Ingrese su altura en metros: ")))
    if sistema_de_medida == 2 :
        peso_libras = float(input("Ingrese su peso en Libras: "))
        altura_pies = float(input("Ingrese su altura en pies y pulgadas\n1ro, los pies: "))
        altura_pulgadas = float(input("Ingrese su altura en pies y pulgadas\n2do, las pulgadas: "))
        datos.append(libras_a_kilos(peso_libras))
        datos.append(pies_pulgadas_a_metros(altura_pies, altura_pulgadas))
    return datos
    

#ingreso de datos y pregunta si los datos estan en sistema ingles o sistema metrico?
sistema_de_medida = int(input("Los datos estan en: \n 1. Sistema metrico.\n2. Sistema ingles.\n"))
#llamo a la funcion que pide datos
datos_sistema_metrico = pedir_datos(sistema_de_medida)
peso = datos_sistema_metrico[0]
altura = datos_sistema_metrico[1]
mi_imc = imc(peso, altura)
print("Su I.M.C. es : ", mi_imc)



#4.5.1.3 Creando funciones con tres parámetros
"""
Teniendo tres medidas de lados, la funcion nos dice si es o no un triangulo
Sabiendo que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.
"""
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


#4.5.1.4 Creando funciones: probando triángulos

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

#revisa si tres lados forman un triangulo rectangulo
def is_a_right_triangle(a, b, c):
    #si No es un triangulo
    if not is_a_triangle(a, b, c):
        return False
    #busca cual es el lado mas largo
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))
if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
    es_rectangulo = is_a_right_triangle(a, b, c)
    if es_rectangulo : print("\nAdemas es Rectangulo")
else:
    print('No, no puede ser un triángulo.')



#4.5.1.5 Sacando el area de un triangulo con la formula de Heron

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

#Calculo el area de un triangulo rectangulo
lado01 = 1.
lado02 = 1.
hipotenusa = (lado01 ** 2  + lado02 ** 2 ) ** .5
print(area_of_triangle(lado01,lado02, hipotenusa))


#4.5.1.6 Creando funciones: factoriales

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):  # probando
    print(n, factorial_function(n))



#4.5.1.7 Creando funciones: Fibonacci

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # probando
    print(n, "->", fib(n))