#4.7.2.1 PROYECTO: TIC-TAC-TOE
"""
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
El usuario (por ejemplo, tu) jugarás utilizando las 'O's.
El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
La maquina responde con su movimiento y se verifica el estado del juego.
No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
El ejemplo del programa es el siguiente:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

Implementa las siguientes características:
-------------------------------------------

El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

board[row][column]


Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre).
La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

from random import randrange

for i in range(10):
    print(randrange(8))Implementa las siguientes características:

El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

board[row][column]


Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre).
La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

from random import randrange

for i in range(10):
    print(randrange(8))"""
    



def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    
    for i in range(1, 14):
        #dibujo el tablero
        
        if i == 1 or i == 5 or i == 9 or i == 13:
            print("+-------+-------+-------+")
        
        #lleno el tablero con los datos del array
        if i == 3 :
            print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
        
        if i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12:
            print("|       |       |       |")
        
        if i == 7 :
            print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
        
        if i == 11 :
            print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
        
    

def EnterMove(board, sign):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    movimiento_ingresado = int(input("Ingrese su movimiento.\n(1 a 9) y debe estar libre: "))
    posicion_columna_ingresada = (movimiento_ingresado - 1) % 3
    posicion_fila_ingresada = (movimiento_ingresado - 1) // 3
    posicion_tupla_ingresada = (posicion_fila_ingresada, posicion_columna_ingresada)
    
    esta_vacio = posicion_tupla_ingresada in lista_vacios
    print("movimiento ingresado: ", posicion_tupla_ingresada, esta_vacio)
    
    if esta_vacio == True :
        board[posicion_fila_ingresada][posicion_columna_ingresada] = sign
        print("ingreso la ", sign, " en [", posicion_fila_ingresada, " ][ ", posicion_columna_ingresada, " ]")
    
    DisplayBoard(board)    


def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    
    longitud_filas = 3
    longitud_columnas = 3
    for i in range(longitud_filas):
        for j in range(longitud_columnas):
            print(board[i][j], end = "")
            if board[i][j] != "O" and board[i][j] != "X":
                #print(" casilla vacia")
                lista_vacios.append((i, j))
            #else:
                #print(" casilla ocupada")
    #print(lista_vacios)
    #print(board)

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    """
    Condiciones para ser ganador:
        - Algunas de las lineas horizontales (3 lineas) tienen el mismo signo [0][0] == [0][1] == [0][2] == "X"
        - Algunas de las lineas verticales (3 lineas) tienen el mismo signo   [0][0] == [1][0] == [2][0]
        - Algunas de las lineas diagonales (2 lineas) tienen el mismo signo
    """
    es_ganador = False
    for indice_filas in range(3):
        if board[indice_filas][0] == board[indice_filas][1] == board[indice_filas][2] == sign :
            es_ganador = True
    for indice_columnas in range(3):
        if board[0][indice_columnas] == board[1][indice_columnas] == board[2][indice_columnas] == sign :
            es_ganador = True
    if board[0][0] == board[1][1] == board[2][2] == sign :
        es_ganador = True
    if board[0][2] == board[1][1] == board[2][0] == sign :
        es_ganador = True
            
    print("Tablero: ", board, "\nBusco  : ", es_ganador)

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    print(board)

lista_vacios = []
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_2 = [["X", "O", "X"], ["O", "O", "O"], ["O", "X", "X"]]        
DisplayBoard(board)
MakeListOfFreeFields(board)
EnterMove(board, "X")
VictoryFor(board, "X")
#falta DrawMove(board)





