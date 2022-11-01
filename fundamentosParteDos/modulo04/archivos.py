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
