#resumen de la seccion

#imprime todos los caracteres antes del @ en una misma linea, 
# gracias a la variable 'end', porque asi no pone el '/'
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "") 


#Crea un programa con un bucle for y una sentenciacontinue. 
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        print("x", end = "")
        continue
    print(digit, end = "")