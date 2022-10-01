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


#2.2.1.9 Si bien las cadenas de caracteres son similares a las listas, algunos metodos no funcionan
alphabet = "abcdefghijklmnopqrstuvwxyz"
"""
Con cadenas No se puede usar del, si se usa se borra toda la cadena
del alphabet[0] borra todo la cadena
el metodo append() y insert() tambien son ilegales
"""
# Escribe el código de prueba aquí.
print(alphabet)


#2.2.1.10 Que hacer para agregar caracteres a una cadena, se usa el +
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)


#2.2.1.11 Demonstrando min() - Ejemplo 1:
caracter_minimo_valor_ascii = min("aAbByYzZ")
print('el minimo caracter es: ', caracter_minimo_valor_ascii)
print('Porque, el codigo ASCII de "', caracter_minimo_valor_ascii, '" es :', str(ord(caracter_minimo_valor_ascii)))
# Demonstrando min() - Ejemplo 2 y 3: el minimo es el espacio. Se ponen los corchetes para que se vea el espacio.
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2] #tambien sirve para numeros
print(min(t))

#2.2.1.12 Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))
# Demostración de max() - Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))


#2.2.1.13 Demonstrando el método index(): busca un caracter dentro de una cadena y devuelve el indice de la primera ocurrencia
cadena_prueba = "aAbByYzZaA"
letra_b = 'b'
letra_Z = 'Z'
letra_A = 'A'
indice_letra_b = cadena_prueba.index(letra_b)
indice_letra_Z = cadena_prueba.index(letra_Z)
indice_letra_A = cadena_prueba.index(letra_A)
print(indice_letra_b)
print(indice_letra_Z)
print(indice_letra_A)


#2.2.1.14 Demostración de la función list():
"""
list convierte no solo cadenas de caracteres, sino tambien otras entidades 
como tuplas, y diccionarios
"""
cadena_prueba_2 = "abcabc"
lista_prueba_2 = list(cadena_prueba_2)
print(lista_prueba_2)
# Demostración de la función list():
print(cadena_prueba_2.count("b"))
print(cadena_prueba_2.count("d"))
#prueba de la lista recientemente creada con la funcion list
lista_prueba_2.append("X")
#cadana_prueba_2.append("Y") Tira un error, porque no es un metodo de cadenas de caracteres.
print(lista_prueba_2)


#2.3.1.1 Demostración del método capitalize():
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize()) #el primer caracter es un espacio en blanco
print('123'.capitalize()) #no hay letras
print("αβγδ".capitalize()) 

#2.3.1.2 Demostración del método center():
cadena_prueba_3 = "alpha"
espacios_alrededor = 20
caracter_separacion = " "
#los parentesis se usan para ver el centrado
print('[' + cadena_prueba_3.center(espacios_alrededor, caracter_separacion) + ']') 

#2.3.1.3  Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
t = "zeta"
print(t.endswith("4"))

#2.3.1.4 Demostración del método find():
# busca una cadena dentro de otra cadena, si no la encuentra devuelve -1
print("Eta".find("ta"))
print("Eta".find("mma"))

#Existe una variante de find() con dos parametros, el segundo indica desde donde buscar.
cadena_prueba_4 = "kappa"
cadena_buscada = "a"
desde_el_indice = 2
indice_encontrada = cadena_prueba_4.find(cadena_buscada, desde_el_indice)
print('cadena encontrada en el indice: ', indice_encontrada)

#Tambien se puede usar find()para mostrar todos los indices de las ocurrencias
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
cadena_buscada = "the"
encontrado = the_text.find(cadena_buscada)
while encontrado != -1:
    print(encontrado)
    encontrado = the_text.find(cadena_buscada, encontrado + 1)    
    
#Tambien se puede usar con tres parametros
cadena_buscada = 'p'
desde_el_indice = 1
hasta_el_indice = 4
encontrado = cadena_prueba_4.find(cadena_buscada, desde_el_indice, hasta_el_indice)
print(encontrado)

#2.3.1.5  Demostración del método the isalnum():
print('lambda30'.isalnum()) #True
print('lambda'.isalnum()) #True
print('30'.isalnum()) #True
print('@'.isalnum()) #False
print('lambda_30'.isalnum()) #False
print(''.isalnum()) #False

#2.3.1.6  saber si una cadena tiene solo digitos o solo letras

# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())
# Ejemplo 2: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())


#2.3.1.7 letras minusculas, espacios en blanco, y mayusculas

# Ejemplo 1: Demostración del método islower(): Busca si todas las letras estan en minusculas
print("Moooo".islower()) #False
print('moooo'.islower()) #True
# Ejemplo 2: Demostración del método isspace(): Busca si todos son espacios en blanco
print(' \n '.isspace()) #True
print(" ".isspace()) #True
print("mooo mooo mooo".isspace()) #False
# Ejemplo 3: Demostración del método isupper():  Busca si todas las letras estan en Mayusculas
print("Moooo".isupper())#False
print('moooo'.isupper()) #False
print('MOOOO'.isupper()) #True


# 2.3.1.8 Demonstrating the join() method:
# El metodo se invoca desde la cadena que servira de separador, luego de ser unida.

lista_nombres_frutas = ["Naranja", "Banana", "Manzana", "Pera", "Frutilla", "Sandia", "Mandarina", "Uvas"]
cadena_separadora = " y "
cadena_nombres_frutas = cadena_separadora.join(lista_nombres_frutas)
print(cadena_nombres_frutas)

#2.3.1.9 Demostración del método lower():
cadena_prueba_5 = "SiGmA=60"
nueva_cadena_minusculas = cadena_prueba_5.lower()
print(nueva_cadena_minusculas)

#2.3.1.10 Demostración del método the lstrip():
"""
devuelve una cadena recién creada formada a partir de la original 
eliminando todos los espacios en blanco iniciales.
"""
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pppppythoninstitute.org".lstrip("py"))



#2.3.1.11 Demostración del método replace():
"""
reemplaza una cadena por otra, o la elimina si el segundo argumento está vacio, admite hasta tres argumentos
"""
cadena_original = "hola hernan? que tal?"
cadena_buscada = "hernan"
cadena_remplazo = "cesar"
#Version con dos argumentos NO vacios
nueva_cadena = cadena_original.replace(cadena_buscada, cadena_remplazo)
print(nueva_cadena)
#Elimina una cadena
cadena_a_borrar = "que tal?"
nueva_cadena = cadena_original.replace(cadena_a_borrar, "")
print(nueva_cadena)
#busca la letra "a" y la reemplaza por una "e", en solo dos indices
cadena_a_borrar = "a"
nueva_cadena = cadena_original.replace(cadena_a_borrar, "e", 2)
print(nueva_cadena)


#2.3.1.12  Demostración del método rfind():
"""
comienzan sus búsquedas desde el final de la cadena, no el principio (de ahí el prefijo r, de reversa).
"""
print("tau tau tau".rfind("ta")) #8
print("tau tau tau".rfind("ta", 9)) #-1
print("tau tau tau".rfind("ta", 3, 9)) #4


#2.3.1.13 Demostración del método rstrip():
#Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


#2.3.1.14 Demostración del método split():
contenido_multilinea = """El método asume que las subcadenas están delimitadas por espacios en blanco.  
los espacios no participan en la operación y no se copian en la lista resultante."""

lista_palabras = contenido_multilinea.split()
cantidad_palabras =  len(lista_palabras)
print('Cantidad palabras: ',cantidad_palabras,'\n', lista_palabras)


#2.3.1.15 Demostración del método startswith():
"""
El método startswith() es un espejo del método endswith() - 
comprueba si una cadena dada comienza con la subcadena especificada.
"""
print("omega".startswith("meg")) #False
print("omega".startswith("om")) #True
print()
"""
El método strip() combina los efectos causados por rstrip() y lstrip() - 
crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
"""
# Demostración del método strip():
print("[" + "   aleph   ".strip() + "]")


#2.3.1.16  swapcase() title() upper()

# Demostración del método swapcase():
"""
crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original
"""
print("Yo sé que no sé nada.".swapcase()) #yO SÉ QUE NO SÉ NADA.
# Demostración del método title():
"""
cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
"""
print("Yo sé que no sé nada. Part 1.".title()) #Yo Sé Que No Sé Nada. Parte 1.
"""
hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas,
"""
# Demostración del método upper():
print("Yo sé que no sé nada. Part 2.".upper()) #YO SÉ QUE NO SÉ NADA. PARTE 2.


#2.3.1.18 Tu propio split
def mysplit(cadena):    
    separador = " "
    lista_palabras = []    
    if cadena == "": 
        return lista_palabras
    else :
        cadena_longitud = len(cadena)    
    indice_comenzar = 0
    indice_encontrado = cadena.find(separador)
    while indice_encontrado != -1 :        
        palabra = cadena[indice_comenzar : indice_encontrado].strip()        
        if palabra != "" :
            lista_palabras.append(palabra)        
        indice_comenzar = indice_encontrado
        indice_encontrado = cadena.find(separador, indice_encontrado + 1)        
        if indice_encontrado == -1 and indice_comenzar < cadena_longitud :
            palabra = cadena[indice_comenzar : cadena_longitud].strip()
            if palabra != "" :
                lista_palabras.append(palabra)     
    return lista_palabras

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

