#2.6.1.1 Errores: el pan diario del programador

import math
x = float(input("Ingresa x: ")) #Ingreso un caracter o un negativo y genera ERROR
y = math.sqrt(x)
print("La raíz cuadrada de", x, "es igual a", y)


#2.6.1.3 Errores: Division por cero
value = 1
value /= 0

#2.6.1.4 Error de indice en una lista
my_list = []
x = my_list[0]

#2.6.1.6 Usando excepciones
first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))
try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")
print("FIN.")

#2.6.1.7 probando excepciones
try:
    print("1")
    x = 1 / 0 #1 ERROR
    print("2") #2 Esto ya no lo hace!
except:
    print("Oh cielos, algo salió mal...") #3 luego del error, viene aca
print("3")

#2.6.1.9 manejando mas de una excepcion en un mismo bloque try
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")
print("FIN.")


#2.7.1.2 Anatomia de las excepciones
try:
    y = 1 / 0 #1 ERROR
#except ArithmeticError: Si pongo las dos expeciones, entraria primero en esta
except ZeroDivisionError: #segun el arbol de excepciones, tambien se podria usar 'ArithmeticError'
    print("Uuupsss...")
print("FIN.")


#2.7.1.4 pasando dos excepciones a except
"""
def bad_fun(n):
    try:
        return 1 / n
    except (ZeroDivisionError, ArithmeticError):
        print("division por cero")
    return None
bad_fun(0)
print("FIN.")
"""
#Tambien se puede atrapar el error desde fuera de la funcion
def bad_fun(n):
    return 1 / n
try:
    bad_fun(0)
except ArithmeticError:
    print("Error aritmetico")
    

#2.7.1.5  La instruccion raise, que genera una exception intencionalmente
def bad_fun(n):
    raise ZeroDivisionError    
try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")
print("FIN.")


#2.7.1.7 instruccion assert
"""
se usa con una condicion logica a la derecha, 
si dicha condicion no se cumple, genera el error.
"""
import math
x = float(input("Ingresa un número: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)


#2.8.1.4 Leer enteros de forma segura
def read_int(prompt, min, max):
    #
    # Escribe tu código aquí.
    pedir_valor = True
    while pedir_valor :
        try:
            valor = int(input(prompt))
            assert min < valor and valor < max
            pedir_valor = False
        except ValueError:
            print('Error: entrada incorrecta')
        except AssertionError:
            print('Error: el valor no está dentro del rango permitido (min..max)')
    return valor
    
v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
print("El número es:", v)
