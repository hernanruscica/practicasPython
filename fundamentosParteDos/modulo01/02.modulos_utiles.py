"""
1.2.1.1 Módulos Útiles
Trabajando con modulos estandar.
La función dir, devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:
dir(module)
"""

import math
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


