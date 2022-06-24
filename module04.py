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
resultado = dia_del_anio(1980, 11, 32)
print(resultado)
resultado = dia_del_anio(1900, 2, 29)
print(resultado)


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
