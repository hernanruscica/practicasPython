"""
1.2.1.1 Módulos Útiles
Trabajando con modulos estandar.
La función dir, devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:
dir(module)
"""

import math
from re import X
from turtle import clear
#muestra una lista de entidades de un modulo, se le pasa un string
def mostrar_entidades_modulo(nombre_modulo) :
    lista_nombres_entidades = dir(nombre_modulo)
    for name in lista_nombres_entidades :
        print(name)
        
mostrar_entidades_modulo("math")

"""
1er grupo de funciones del modulo math: 
sin(), cos(), tan(), asin(), acos(), atan(), pi(), radians(), degrees()
"""

def demo_trigonometria_math(angulo_en_decimal) :
    angulo_en_radianes = math.radians(angulo_en_decimal)
    angulo_en_grados = math.degrees(angulo_en_radianes)
    
    print(angulo_en_decimal, " en decimal.")
    print(angulo_en_radianes, " en radianes.")
    print(angulo_en_grados, " en grados.")
    print("el numero PI es :", math.pi, "\n")
    print("Seno:", math.sin(angulo_en_decimal), "\n")
    print("Coseno:", math.cos(angulo_en_decimal), "\n")
    print("Tangente:", math.tan(angulo_en_decimal), "\n")
    
demo_trigonometria_math(89.5)

from math import e, exp, floor, log;
"""
2do grupo de funciones del modulo math:
"""
print("2 al cuadrado es cubo es: ",pow(2,3));
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


"""
El último grupo consta de algunas funciones de propósito general como
ceil(x) → devuelve el entero más pequeño mayor o igual que x.
trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) 
(lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
"""
from math import *;
import os;
x = 1.4;
y = 2.6;
os.system ("cls");
print("x = ", x, "\ny = ", y);
print("El entero más grande menor o igual que x es :", floor(x));
print("El entero más pequeño mayor o igual que y es :", ceil(y));
print("El valor de x truncado a un entero: ", trunc(x));
print("La hipotenusa que forman los catetos X e Y es = ", hypot(x, y));

"""
Las funciones ramdon y seed. seed no devuelve nada, pero genera aleatoriedad para la funcion randon. Aunque si se usa siempre la misma semilla, se obtiene siempre el mismo random
"""
from random import random, seed
seed();
for i in range (3):
    print(random());

"""
randrange(fin)
randrange(inico, fin)
randrange(inicio, fin, incremento)
randint(izquierda, derecha)
"""

from random import randrange, randint

print(randrange(1), end=' ');
print(randrange(0, 1), end=' ');
print(randrange(0, 1, 1), end=' ');
print(randint(0, 10));

"""
Funciones choice y sample
"""
from random import choice, sample;

numero_azar = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);
print("el numero al azar es : ", numero_azar);

colores = ["rojo", "azul", "verde", "amarillo", "naranja", "celeste", "violeta", "blanco", "negro"];
cantidad_colores_elegidos = 5;
orden_colores_aleatorios = sample(colores, cantidad_colores_elegidos);
print(orden_colores_aleatorios);


"""
Platform : brinda informacion sobre la plataforma donde se esta ejecutando python
"""
from platform import platform, machine, processor, system, version;
platform(aliased = False, terse = False);
print(machine());
print(processor());
print(system());
print(version());

#indice de modulos de python  https://docs.python.org/3/py-modindex.html

