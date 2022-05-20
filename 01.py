
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
    return tieneFiebre == False

estadoIngreso = puedeIngresar(temperatura)

if (estadoIngreso == True):
    mensajeIngreso = "Usted puede ingresar"
else:
    mensajeIngreso = "Usted No puede ingresar"

print(mensajeIngreso)





