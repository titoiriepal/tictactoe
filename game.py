from board import Board
from player import Player


class Game:

    WINNERMOVES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]

    def __init__(self):
        self.turn = 1
        self.player1 = Player(1, 'X')
        self.player2 = Player(-1, 'O')
        self.board = Board(self.player1.character, self.player2.character)
        self.board.displayBoard()
        self.playGame()

    def playGame(self):
        while True:
            if self.turn % 2 == 1:
                move = self.player1.chooseMove(self.turn, self.board)
                self.board.assignValue(self.turn, move, self.player1.value)
                self.board.displayBoard()
                victory = self.checkWin(self.board)

                if victory is True:
                    print('¡¡¡Enhorabuena, jugador 1. Has ganado la partida!!!')
                    exit()

            else:
                move = self.player2.chooseMove(self.turn, self.board)
                self.board.assignValue(self.turn, move, self.player2.value)
                self.board.displayBoard()
                victory = self.checkWin(self.board)

                if victory is True:
                    print('¡¡¡Enhorabuena, jugador 2. Has ganado la partida!!!')
                    exit()

            if self.turn == 9:
                print(' Ha sido un empate')
                exit()
            self.turn += 1

    def checkWin(self, board):
        for a, b, c in self.WINNERMOVES:
            if board.tableboard[a] + board.tableboard[b] + board.tableboard[c] == 3:
                return True
            if board.tableboard[a] + board.tableboard[b] + board.tableboard[c] == -3:
                return True
