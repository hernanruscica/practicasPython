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
    print(randrange(8))
"""


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for i in range(1, 14):
        #dibujo el tablero
        if i == 1 or i == 5 or i == 9 or i == 13:
            print("+-------+-------+-------+")
        else:
            print("|       |       |       |")
        
        #lleno el tablero con los datos del array
        if i == 3 :
            print("    ", board[0][0] , "    ", board[0][1] , "   ", board[0][2])
        
        if i == 7 :
            print("    ", board[1][0] , "    ", board[1][1] , "   ", board[1][2])
        
        if i == 10 :
            print("    ", board[2][0] , "    ", board[2][1] , "   ", board[2][2])

DisplayBoard(board)

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    print(board)

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    print(board)

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    print(board, sign)

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    print(board)