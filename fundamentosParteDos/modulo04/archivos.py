#4.2.1.09 abriendo un archivo 
try:
    stream = open("file.txt", "rt")
    # El procesamiento va aquí.
    print(stream)
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


#4.2.1.11 manejo de error al abrir archivos
import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)


#4.3.1.1 Trabajando con archivos reales
# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
stream = open("tzop.txt", "rt", encoding = "utf-8")

# Se imprime el contenido del archivo:
print(stream.read()) 

#4.3.1.2 leyendo de a 1 caracter
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


#4.3.1.3 leyendo todo el archivo de texto
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


#4.3.1.4 leyendo lineas completas
from os import strerror
try:
    character_counter = line_counter = 0
    stream = open('file.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

#4.3.1.5 readlines
"""
Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo 
y devuelve una lista de cadenas, un elemento por línea del archivo.
"""
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('file.txt', 'rt')
    lines = stream.readlines(10)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
        lines = stream.readlines(10)
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

#4.3.1.6  Gracias al metodo implicito __next__ del objeto open, se puede iterar por él, y auto cerrarse al llegar al final
from os import strerror
try:
	character_counter = line_counter = 0
	for line in open('text.txt', 'rt'):
		line_counter += 1
		for char in line:
			print(char, end='')
			character_counter += 1
	print("\n\nCaracteres en el archivo: ", character_counter)
	print("Líneas en el archivo:     ", line_counter)
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))

#4.3.1.7  La funcion write()
"""
El método se llama write() y espera solo un argumento: una cadena que se transferirá 
a un archivo abierto (no lo olvides), el modo de apertura debe reflejar la forma 
en que se transfieren los datos, escribir en un archivo abierto 
en modo de lectura no tendrá éxito).
"""
from os import strerror
try:
	file = open('newtext2.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "linea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))

#4.3.1.8 en vez de escribir de a un caracter, se escribe la linea
from os import strerror

try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
