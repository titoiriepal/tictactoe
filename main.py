import os


class Game:

    WINNERMOVES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]

    def __init__(self):
        self.board = Board()
        self.board.displayBoard()
        self.playGame(self.board)

    def playGame(self, board):
        turn = 1
        while True:
            move = 'a'
            player = Player(turn)
            board.printFreeMoves()
            while move not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                move = player.chooseMove(turn)
                
                if move < 1 or move > 9:
                    print('El número elegido no está en rango, por favor elige un número de la tabla superior')
                    move = 'a'
                else:
                    if board.board[move - 1] != 0:
                        print('El número elegido ya esta ocupado, intentalo de nuevo')
                        move = 'a'

            board = self.assignTab(turn, move, board)
            board.displayBoard()
            self.checkWin(board)
            if turn == 9:
                print('Ha sido un empate')
                exit()
            turn = turn + 1

    def assignTab(self, turn, move, board):
        if turn % 2 == 1:
            board.board[move - 1] = 1
        else:
            board.board[move - 1] = -1
        return board

    def checkWin(self, board):
        for a, b, c in self.WINNERMOVES:
            if board.board[a] + board.board[b] + board.board[c] == 3:
                print('Gana el jugador 1')
                exit()
            if board.board[a] + board.board[b] + board.board[c] == -3:
                print('Gana el jugador 2')
                exit()


class Board:

    PLAYERVALUES = (' ', 'X', 'O')
    GAMEVALUES = (0, 1, -1)

    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.board = self.rellenaTabla()

    def rellenaTabla(self):
        # https://blog.teamtreehouse.com/python-single-line-loops
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return [j for i in self.tablero for j in i]

    def displayBoard(self):
        os.system("cls")
        self.fillTablero()
        for i in range(0, 3):
            print('   |   |   ')
            indx1 = self.GAMEVALUES.index(self.board[i*3])
            indx2 = self.GAMEVALUES.index(self.board[(i*3)+1])
            indx3 = self.GAMEVALUES.index(self.board[(i*3)+2])
            print(f' {self.PLAYERVALUES[indx1]} | {self.PLAYERVALUES[indx2]} | {self.PLAYERVALUES[indx3]} ')
            if i != 2:
                print('___|___|___')
            else:
                print('   |   |   ')

    def printFreeMoves(self):

        def getFill(displacement=0):
            table = []
            for i in range(0, 3):
                pos = (displacement * 3) + i
                if self.board[pos] != 0:
                    character = " "
                else:
                    character = str(pos + 1)
                table.append(character)
            return table

        for i in range(0, 3):
            a = getFill(i)
            if i != 2:
                print(f'          ' + "\033[4;37m" + f'{a[0]}|{a[1]}|{a[2]}' + '\033[0;37m')
            else:
                print(f'          {a[0]}|{a[1]}|{a[2]}')

    def fillTablero(self):
        for i in range(0, 3):
            self.tablero[i][0] = self.board[i*3]
            self.tablero[i][1] = self.board[(i*3)+1]
            self.tablero[i][2] = self.board[(i*3)+2]


class Player:

    CHARACTERA = 'X'
    CHARACTERB = '0'

    def __init__(self, turn):
        if turn % 2 != 0:
            self.mark = self.CHARACTERA
        else:
            self.mark = self.CHARACTERB

    def chooseMove(self, turn):
        currPlayer = '1' if turn % 2 else '2'
        msg = 'Jugador ' + currPlayer
        move = None
        while move is None:
            move = input(f'{msg}, por favor introduce tu movimento o pulsa q para salir: ').lower()
            if move == 'q':
                exit()
            try:
                move = int(move)
            except ValueError:
                print('Por favor, introduce un número de la tabla superior')
                move = None

        return move


Game()
