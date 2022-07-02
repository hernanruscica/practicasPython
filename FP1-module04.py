"""
variable = 1
mi_lista = [1, 2, 3]
def hola(lista):
    print("hola", variable)
    del lista[-1]

def fun(mi_in = 2, mi_out = 3):
    return mi_in * mi_out

hola(mi_lista)
print(mi_lista)
print(fun(3))

tup = (1, ) + (1, )
tup = tup + tup
print(len(tup))



tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)


def fun(x):
    global y
    y = x * x
    
    return  y

fun(2)
print(y)
"""
"hola" / "casa"
"""
mitupla = (1, 2)

mitupla[0] = 6


def milista(milista):
    del milista[2]
    milista[0] = 1
    return 1

milista = [1,2]

print(milista(milista))

#que imprime-------------------------------------------------
diccionario = {"one": "two", "three": "one", "two": "three"}
v = diccionario["one"]#two

#len = 3 hace 3 pasadas: 0, 1, 2
for k in range(len(diccionario)):
    v = diccionario[v] 
    #1ra pasada: three
    #2da pasada: one
    #3ra pasada: two

#se queda con el ultimo valor, two
print(v) 
#que imprime-------------------------------------------------


#que imprime-------------------------------------------------
def funcion(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(funcion(funcion(2)) + 1)
#paso a paso
#print(funcion(1) + 1)
#print(None + 1) y esto tira TypeError
#que imprime-------------------------------------------------


#que debo cambiar abajo de "k = diccionario[i]" para que la salida sea: a, b, c
# -------------------------------------------------
diccionario = {}
mi_lista = ["a", "b", "c", "d"]

#len(mi_lista) = 4 => 4 - 1 = 3 itera: 0, 1, 2 
for i in range(len(mi_lista) - 1):
    #diccionario["a"] = ("a", )
    diccionario[mi_lista[i]] = (mi_lista[i], )

#keys = a, b, c  itera 3 veces
for i in sorted(diccionario.keys()):
    #obtengo el valor de la clave que es igual a la clave
    k = diccionario[i]
    #obtengo el primer elemento de la tupla de 1 elemento.
    print(k[0])
#que debo cambiar abajo de "k = diccionario[i]" para que la salida sea: a, b, c 
# 

#cual es la salida del siguiente codigo (RECURSIVIDAD)
def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)
print(f(3))
# f(0) => return 0 
# f(1) => return 1 + f(1 - 1)
# f(2) => return 2 + f(2 - 1)
# f(3) => return 3 + f(3 - 1)
#Empieza de abajo a arriba, es una pila y suma las equis de cada iteracin

#cual es la salida del siguiente codigo 
def fun(x):
    x += 1
    return x

x = 2
x = fun(x + 1)
print(x)
#fun(3) => return 4 DEVUELVE 4
#cual es la salida del siguiente codigo 

#cual es la salida del siguiente codigo?
def fun(inp = 2, out = 3):
    return inp * out
print(fun(out = 2))
#se le pasa el argumento con nombre para out, asi que deja de ser el default y devuelve 2 * 2 = 4
#cual es la salida del siguiente codigo?


#cual es la salida del siguiente codigo?
mi_lista = ["Mary", "had", "a", "little", "lamb"]
def mi_lista(mi_lista):
    #elimino "little"
    del mi_lista[3]
    mi_lista[3] = "ram"
print(mi_lista(mi_lista))
#typeError no se puede eliminar un item de una lista
#cual es la salida del siguiente codigo?


#cual es la salida del siguiente codigo?
def func(a, b):
    return a ** a
print(func(2))
#Error: le falta un argumento
#cual es la salida del siguiente codigo?
"""