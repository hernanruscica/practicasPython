"""
CADENAS EN PYTHON
"""

#2.2.1.1 Longitud de las cadenas 
##################################

# Ejemplo 1
word = 'by'
print(len(word)) #2

# Ejemplo 2
empty = ''
print(len(empty)) #0

# Ejemplo 3: No olvides que la diagonal invertida (\) empleada como un carácter de escape, no está incluida en la longitud total de la cadena.
i_am = 'I\'m'
print(len(i_am)) #3
print(i_am) #i'm


#2.2.1.2 Cadenas multilínea
##################################
"""
Una variable multilinea, se declara, poniendo el valor entre comillas triples. 
Al momento de contar hay que tener en cuenta que hay un caracter invisible que es el salto de linea \n
"""
multiline = '''Línea #1
Línea #2'''
print(len(multiline)) #17

#2.2.1.3 - Operaciones con cadenas
"""
concatenacion (+) de cadenas y replicacion (*)
"""
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#2.2.1.4 - funcion ord()  el valor del punto de código ASCII/UNICODE de un carácter específico
# # Demostración de la función ord ().

char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))

#2.2.1.5 - funcion chr() : toma un punto de código y devuelve su carácter.
print(chr(97)) #a
print(chr(945)) #αα
cuatro_string = '4'
print(chr(ord(cuatro_string)) == cuatro_string)


#2.2.1.6 indexando cadenas
the_string = "silly walks"
the_string_len = len(the_string)

#indexando la cadena
for i in range(the_string_len):
    print(the_string[i], end = ' ')
print('\n')
#iterando la cadena
for character in the_string:
    print(character, end = '-')
print('\n')

#2.2.1.7  Rebanadas extrae una porcion de cadena de texto. 
# Se debe indicar posicion inicial y posicion final, esta ultima no se incluye

alpha = "abdefg"
print(alpha[1:3]) #bd
print(alpha[3:]) #efg
print(alpha[:3]) #abd
print(alpha[3:-2]) #e 
print(alpha[-3:4]) #e
print(alpha[::2]) #adf saltea de a dos posiciones
print(alpha[1::2]) #beg

#2.2.1.8 Los operadores in y not in
"""
'in' comprueba si el argumento izquierdo (una cadena) se puede encontrar en 
cualquier lugar dentro del argumento derecho (otra cadena).
"""

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
letra = 'ñ'
existeLetraEn = letra in alfabeto
print('letra ', letra,' existe ' if existeLetraEn else ' No existe ', ' en alfabeto')

letras = 'abc'
existenLetrasEn = letras in alfabeto
print('letras ', letras,' existen ' if existenLetrasEn else ' No existen ', ' en alfabeto')

letras = 'abC'
existenLetrasEn = letras in alfabeto
print('letras ', letras,' existen ' if existenLetrasEn else ' No existen ', ' en alfabeto')

#not in es es al reves, niega el in

letras = 'caracteres que no estan en el alfabeto'
noExistenLetrasEn = letras not in alfabeto #true
print('letras ', letras,' No existen ' if noExistenLetrasEn else ' existen ', ' en alfabeto')


