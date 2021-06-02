import os

class Game:
    def __init__(self):
        self.breed = 'Game'
    
    def playGame(self, board):
        turn = 1
        while True:
            move = 'a'
            while move not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                player = Player()
                move = player.chooseMove(turn)
                if board.board[move - 1] != 0:
                    print('El número elegido ya esta ocupado, intentalo de nuevo')
                    move = 'a'
            board.board = self.assignTab(turn, move, board.board)
            board.displayBoard()
            self.checkWin(board)
            if turn == 9:
                print('Ha sido un empate')
                exit()
            turn = turn + 1
        
    def assignTab(self, turn, move, board):
        if turn % 2 == 1:
            board[move - 1] = 1
        else:
            board[move - 1] = -1
        return board

    def checkWin(self,board):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if board.board[a] + board.board[b] + board.board[c] == 3:
                print('Gana el jugador 1')
                exit()
            if board.board[a] + board.board[b] + board.board[c] == -3:
                print('Gana el jugador 2')
                exit()
            










class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    def displayBoard(self):
        os.system("cls")
        playerValues = (' ', 'X', 'O')
        gameValues = (0, 1, -1)
        for i in range(0, 3):
            print('   |   |   ')
            indx1 = gameValues.index(self.board[i*3])
            indx2 = gameValues.index(self.board[(i*3)+1])
            indx3 = gameValues.index(self.board[(i*3)+2])
            print(f' {playerValues[indx1]} | {playerValues[indx2]} | {playerValues[indx3]} ')
            if i !=2:
                print('___|___|___')
            else:
                print('   |   |   ')
            

    



class Player:
    def __init__(self):
        self.breed = 'Player'

    def chooseMove(self, turn):
        if turn % 2 == 1:
            msg = 'Jugador 1'
        else:
            msg = 'Jugador 2'
        move = input(f'{msg}, por favor introduce tu movimento o pulsa q para salir: ').lower()
        if move == 'q':
            exit()
        return int(move)

    

b = Board()
b.displayBoard()
g = Game()
g.playGame(b)
    