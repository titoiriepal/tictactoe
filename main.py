import os


class Game:

    WINNERMOVES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]  # Definimos todas las opciones de victoria de una lista de 9 posiciones

    def __init__(self):
        self.board = Board()  # Cuando empezamos el juego creamos el tablero
        self.board.displayBoard()  # Cuando empezamos el juego imprimimos el tablero vacío
        self.playGame(self.board)  # Llamamos a la función principal.

    def playGame(self, board):
        turn = 1  # Inicializamos los turnos
        while True:  # Bucle principal del programa
            move = 'a'  # Definimos un movimiento no válido para sanitizar el input del movimiento
            player = Player(turn)  # inicializo el jugador, para que en cada turno asigne un valor
            # de carácter para jugar. No lo veo muy necesario en este juego de jugador contra jugador
            board.printFreeMoves()  # Imprime una pequeña tabla con los números libres para jugar
            while move not in (1, 2, 3, 4, 5, 6, 7, 8, 9):  # Bucle para pedir el movimiento y comprobar que sea válildo
                move = player.chooseMove(turn)  # Función para introducir el movimiento

                if move < 1 or move > 9:  # Comprueba que sea un número válido y vuelve arriba si no lo es
                    print('El número elegido no está en rango, por favor elige un número de la tabla superior')
                    move = 'a'
                else:
                    if board.board[move - 1] != 0:  # Comprueba que el número no está ya  seleccionado
                        print('El número elegido ya esta ocupado, intentalo de nuevo')
                        move = 'a'

            board = self.assignTab(turn, move, board)  # Introduce el valor válido en la lista del tablero
            board.displayBoard()  # Imprimimos la tabla con el último movimiento efectuado
            self.checkWin(board)  # Comprobamos si hemos ganado. Saldrá de la partida si lo hemos hecho
            if turn == 9:  # Comprobamos que, si no hay victoria, hayamos completado todos los turnos
                print('Ha sido un empate')
                exit()
            turn = turn + 1

    def assignTab(self, turn, move, board):  # Rellena la tabla con el valor correspondiente según sea el turno
        if turn % 2 == 1:
            board.board[move - 1] = 1
        else:
            board.board[move - 1] = -1
        return board

    def checkWin(self, board):  # Comprobamos las condiciones de victoria en la constante de arriba
        for a, b, c in self.WINNERMOVES:
            if board.board[a] + board.board[b] + board.board[c] == 3:
                print('Gana el jugador 1')
                exit()
            if board.board[a] + board.board[b] + board.board[c] == -3:
                print('Gana el jugador 2')
                exit()


class Board:

    PLAYERVALUES = (' ', 'X', 'O')  # Inicializamos esta constante con los valores a imprimir que, curiosamente
    # sus inidices corresponden a sus valores en la tabla [0, 1, -1]. El -1 siempre
    # es el último índice
    # GAMEVALUES = (0, 1, -1)

    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # inicializamos el tablero con una lista de tres listas
        self.board = self.rellenaTabla()  # Creo una tabla, que será la que actualice y luego envíe al tablero
        # la función rellenaTabla se encargará de ello

    def rellenaTabla(self):
        # https://blog.teamtreehouse.com/python-single-line-loops
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return [j for i in self.tablero for j in i]  # Esta instrucción devuelve un valor j por cada lista (i)
        # que hay por cada una de las listas j en a lista grande (i)

    def displayBoard(self):  # Dibujamos el tablero
        os.system("cls")  # Limpiamos pantalla
        self.fillTablero()  # rellenamos el tablero de tres listas según la tabla de 9 posiciones
        cont = 0  # Un contador para poder imprimir las líneas de separación
        for [a, b, c] in self.tablero:  # Literal: por cada lista que haya en el tablero...
            print('     |     |     ')  # ...imprime la primera línea de cada casilla...
            print(f'  {self.PLAYERVALUES[a]}  |  {self.PLAYERVALUES[b]}  |  {self.PLAYERVALUES[c]}')  # ... imprime la
            # segunda línea de cada casilla con sus valores ya cambiados. Aquí el indice de la lista PLAYERVALUES
            if cont != 2: # Si no es la última casilla de las tres imprime el separador de casillas
                print('_____|_____|_____')
            else:
                print('     |     |   ')
            cont += 1  # actualizo el contador para saber que casilla estoy imprimiendo
        # Alternativa más complicada para imprimir la tabla. Funciona pero no es nada clara. Básicamente recorre la
        #  tabla de 9 posiciones sumando uno, dos, y tres al indice i multiplicado por tres para imprimir cada posición
        '''for i in range(0, 3):
            print('   |   |   ')
            indx1 = self.GAMEVALUES.index(self.board[i*3])
            indx2 = self.GAMEVALUES.index(self.board[(i*3)+1])
            indx3 = self.GAMEVALUES.index(self.board[(i*3)+2])
            print(f' {self.PLAYERVALUES[indx1]} | {self.PLAYERVALUES[indx2]} | {self.PLAYERVALUES[indx3]} ')
            if i != 2:
                print('___|___|___')
            else:
                print('   |   |   ')'''

    def printFreeMoves(self):  # Imprime los movimientos libres

        def getFill(displacement=0):  # Creamos una lista de tres posiciones con los valores que estan sin cojer, en la
            # lista son 0 y con espacios en blanco si los números están cogidos. Lo hacemos tres veces.
            #  FUNCIÓN A REVISAR. 
            table = []
            for i in range(0, 3):
                pos = (displacement * 3) + i
                if self.board[pos] != 0:
                    character = " "
                else:
                    character = str(pos + 1)
                table.append(character)
            return table

        for i in range(0, 3):  # Bucle para imprimir la tabla de movimientos vacíos 
            freeMovesTable = getFill(i)
            if i != 2:
                print(f'                   ' + "\033[4;37m" + f'{freeMovesTable[0]}|{freeMovesTable[1]}|{freeMovesTable[2]}' + '\033[0;37m')
            else:
                print(f'                   {freeMovesTable[0]}|{freeMovesTable[1]}|{freeMovesTable[2]}')

    def fillTablero(self):  # Actualizo el tablero según la tabla de 9 posiciones con la que realmente jugamos
        for i in range(0, 3):
            for j in range(0, 3):
                self.tablero[i][j] = self.board[(i*3)+j]


class Player:  # La clase player en el jugador vs jugador no la veo demasiado necesaria, aún así la invoco para pedir
    # el movimiento. Puede ser más útil cuando el juego sea jugador vs cpu ó cpu vs cpu

    CHARACTERA = 'X'
    CHARACTERB = '0'

    def __init__(self, turn):
        if turn % 2 != 0:
            self.mark = self.CHARACTERA
        else:
            self.mark = self.CHARACTERB

    def chooseMove(self, turn):  # función para elegir movimiento del jugador humano
        currPlayer = '1' if turn % 2 else '2'
        msg = 'Jugador ' + currPlayer
        move = None
        while move is None:
            move = input(f'{msg}, por favor introduce tu movimento o pulsa q para salir: ').lower()
            if move == 'q':
                exit()
            try:  # Comprobamos que nos pasan un número entero, y, si no, pedimos otro
                move = int(move)
            except ValueError:
                print('Por favor, introduce un número de la tabla superior')
                move = None

        return move


Game()
