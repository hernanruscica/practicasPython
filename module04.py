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



#4.5.1.8 Creando funciones: recursividad
"""
La recursividad es una técnica donde una función se invoca a si misma.
La serie de Fibonacci es un claro ejemplo de recursividad.
"""
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
for n in range(1, 10):
    print(n, "->", fib(n))


# Implementación recursiva de la función factorial.

def factorial(n):
    if n == 1:    # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4)) # 4 * 3 * 2 * 1 = 24

"""
Revisar lo de recursivida
"""


#4.6.1.1 y 4.6.1.2 Tuplas y diccionarios

"""
Tipos de secuencias y mutabilidad

Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor (o ninguno si la secuencia esta vacía), 
los cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento por elemento.

La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder 
cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.
Los datos mutables pueden ser actualizados libremente en cualquier momento, a esta operación se le denomina "in situ".

tupla. Una tupla es una secuencia inmutable.
"""
#tuplas 
tupla_1 = (1, 2, 3, 4)
tupla_2 = 4, 'b', 'c', 'd'
tupla_vacia = ()
tupla_un_elemento = (True, )

#El quitar las comas no arruinará el programa en el sentido sintáctico, pero serán dos variables, no tuplas.
tupla_un_elemento_02 = True,

#la forma de acceder a las tuplas es la misma que con las listas.
print(tupla_2[0])#El 1er elementeo
print(tupla_2[-1])#El ultimo elemento
print(tupla_2[1:])#desde el 2do hasta el final
print(tupla_2[0])#desde el comienzo hasta el ante ultimo

"""
Todas estas tiran ERROR.:
    my_tuple.append(10000)
    del my_tuple[0]
    my_tuple[1] = -10
"""
for elem in tupla_1:
    print(elem)


#4.6.1.3 Tuplas y diccionarios
"""
¿Qué más pueden hacer las tuplas?

La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
El operador + puede unir tuplas (ya se ha mostrado esto antes).
El operador * puede multiplicar las tuplas, así como las listas.
Los operadores in y not in funcionan de la misma manera que en las listas.
"""

mi_tupla = (10, 20, 30)
tupla1 = mi_tupla + (40, 50)
tupla2 = tupla1 * 3
print("tupla1: ", tupla1, "\ntupla2: ", tupla2)
numero_buscado = 20
print("El ", numero_buscado, " está en tupla2 ? ", numero_buscado in tupla2)


#4.6.1.4 Tuplas y diccionarios
"""
¿Qué es un diccionario?
El diccionario es otro tipo de estructura de datos de Python. No es una secuencia 
(pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

Esto significa que un diccionario es un conjunto de pares de claves y valores.

Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.

"""

#Diccionarios
preferencias = {"color" : "Azul", "comida" : "Pastel de papas", "hace_ejercicio" : False, "telefono" : 1132924558}

#dependiendo de la version de python el orden de la lista puede variar. 
#En Python 3.6x los diccionarios se han convertido en colecciones ordenadas de manera predeterminada. 
print(preferencias)

#Accediendo a un atributo en particular
print(preferencias["hace_ejercicio"]) #False



#4.6.1.5 Tuplas y diccionarios
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo', 'chien']
for word in words:
    #busca cada una de las word por keys de dictionary
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")



#4.6.1.6 Tuplas y diccionarios - El metodo keys()
"""
No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.
Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los 
requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el diccionario 
y una entidad secuencial temporal).
keys() = El método retorna o regresa una lista de todas las claves dentro del diccionario. 
"""
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
keys_del_diccionario = dictionary.keys()
#muestra la key y el valor de cada elemento
for key in keys_del_diccionario:
    print(key, "->", dictionary[key])    

#Ademas la funcion sorted() sirve para entregar los datos ordenados
frutas = {"uva" : "grape", "frutilla" : "strawberry", "naranja" : "orange", "manzana" : "apple"}
keys_de_frutas = frutas.keys()
for fruta in sorted(keys_de_frutas) :
    print(fruta, "->", frutas[fruta])




#4.6.1.7 Tuplas y diccionarios - Métodos

diccionario = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

"""items()"""
#variables temporales para manejar cada par de items
for espaniol, frances in diccionario.items():
    print(espaniol, "-->", frances)

"""keys()"""
#tomo el valor de las 'keys'de cada elemento
for nombre_elemento in diccionario.keys():
    print(nombre_elemento)

"""values() """
#tomo el valor de cada elemento y lo muestro
for valor_elemento in diccionario.values():
    print(valor_elemento)




#4.6.1.8 Tuplas y diccionarios
"""
¿Cómo utilizar un diccionario? Modificar, agregar y eliminar valores
"""

#creo un diccionario para las pruebas
dictionary = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

#Reemplazamos un valor en la clave o key 'gato'
dictionary['gato'] = 'minou'
print("cambie el valor de 'gato'\n", dictionary)

#Agregando nuevas claves, a diferencia de una lista, en los diccionarios se pueden agregar nuevas claves
dictionary['cisne'] = "cigne"
print("agregue una nueva clave, declarandola directamente\n", dictionary)

#Tambien se puede usar el metodo update() para ingresar una nueva clave
dictionary.update({"pato": "canard"})
print("agregue la clave canard con update\n", dictionary)

"""
Ademas Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem()
En versiones anteriores de Python, por ejemplo, antes de la 3.6.7, el método popitem() 
elimina un elemento al azar del diccionario.
"""
dictionary.popitem()
print("Elimine el ultimo par 'clave-valor' con el metodo popitem()\n", dictionary)



#4.6.1.9 Tuplas y diccionarios trabajando juntos
"""
Imaginemos el siguiente problema:

-Necesitas un programa para calcular los promedios de tus alumnos.
-El programa pide el nombre del alumno seguido de su calificación.
-Los nombres son ingresados en cualquier orden.
-El ingresar un nombre vacío finaliza el ingreso de los datos 
    (nota 1: ingresar una puntuación vacía generará la excepción ValueError, 
    pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el 
    segundo parte de la serie del curso).
-Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
"""
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
        
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

"""
Los resumenes de las secciones (a partir de esta) los guardo en ISPC\Programador - TSDWAD - 2022\Python
"""

#4.7.1.2 Excepciones
#Saber el tipo de datos de una variable
value = 1
es_entero = type(value) is int
print(es_entero)

value = 1.0
es_entero = type(value) is int
print(es_entero)

#4.7.1.3 Excepciones
"""
La palabra clave reservada try marca el lugar donde intentas hacer algo sin permiso.
La palabra clave reservada except comienza un lugar donde puedes mostrar tu 
talento para disculparte o pedir perdón.
"""
try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
    23 / 0
except:
	# Es un espacio dedicado 
    # exclusivamente para pedir perdón.
    print("hubo un error")

#4.7.1.5 Excepciones
"""
Cómo lidiar con más de una excepción?
Se ponen los nombres de las excesiones a manejar.
En esta variante, cada una de las excepciones esperadas tiene su propia 
forma de manejar el error, pero se debe enfatizarse en que solo una de 
todas puede interceptar el control; si se ejecuta una, todas las demás 
permanecen inactivas. 

"""
try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')  

#4.7.1.6 La excepción por defecto y cómo usarla
"""
Hemos agregado un tercer except, pero esta vez no tiene un nombre de excepción 
específico; podemos decir que es anónimo o (lo que está más cerca de su función real) 
es el por defecto.
"""
try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')


#4.7.1.7 Excepciones
"""
Analicemos con más detalle algunas excepciones útiles (o más bien, las más comunes) 
que puedes llegar a experimentar.
"""

#ZeroDivisionError
try:
    #ZeroDivisionError 1 / 0
    # NameError 2 + d 
    #TypeError print("cadena" + 2)
    #AttributeError "rebanada".slice(0, 10)    
    """
    ValueError
    lista = []
    lista.remove(7)
    """
    # print(("trato de escribir print, pero no puedo")
except ZeroDivisionError:
    print("ZeroDivisionError: No se puede dividir por cero")
except NameError:
    print("NameError: ocurre cuando el intérprete CPython no reconoce un nombre de objeto local o global que se haya proporcionado en el código fuente de Python.")
except ValueError:
    print("ValueError: Error en los tipos de datos pasados a una funcion")
except TypeError:
    print("TypeError: Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual")
except AttributeError:
    print("AttributeError: Esta excepción llega, entre otras ocasiones, cuando intentas activar un método que no existe en un elemento con el que se está tratando.")
except SyntaxError:
    print("SintaxError: Errores en la sintaxis de nuestro codigo. Es una mala idea manejar este tipo de excepciones en tus programas. Deberías producir código sin errores de sintaxis, en lugar de enmascarar las fallas que has causado.")


#4.7.1.9 Excepciones
"""
Cuando Python cierra sus ojos... puede haber errores de sintaxis que python no reconoce porque estan en una linea de varias lineas de ejecucion.
Abajo un ejemplo:
"""
temperature = float(input('Ingresa la temperatura actual:'))
if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    prin("Por debajo de cero")
else:
    print("Cero")
#¿Entiendes ahora por qué el pasar por todos los caminos de ejecución es tan vital e inevitable?
