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

#Ahora un ejemplo de una funcion que a veces no tiene que devolver 
#entonces devuleve None

def funcion_extrania(n):
    if(n % 2 == 0):
        return True

print(funcion_extrania(2))
print(funcion_extrania(1))