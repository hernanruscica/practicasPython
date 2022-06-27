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
#4.6.1.1 Tuplas y diccionarios
