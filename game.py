from board import Board
from player import Player
from messages import messages


class Game:

    WINNERMOVES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]

    def __init__(self, option):
        self.option = option
        self.turn = 1
        self.player1 = Player(1, 'X')
        self.player2 = Player(-1, 'O')
        self.board = Board(self.player1.character, self.player2.character)
        self.board.displayBoard()
        self.playGame()

    def playGame(self):
        while True:

            self.manageInput(self.turn, self.board, self.player1.value, 'Jugador1')
            if int(self.option) == 1:
                self.manageInput(self.turn, self.board, self.player2.value, 'Jugador2')
            else:
                self.manageInput(self.turn, self.board, self.player2.value, 'CPU')

    def manageInput(self, turn, board, playerValue, namePlayer):
        if namePlayer == 'CPU':
            move = self.player2.cpuMove(board, turn) + 1
        else:
            move = self.player1.chooseMove(turn, board)
        self.board.assignValue(turn, move, playerValue)
        victory = self.checkWin(board)
        if victory is True:
            print(f'{messages["congratulations"]} {namePlayer}{messages["win"]}')
            exit()
        self.turn += 1
        if self.turn == 10:
            regame = ' '
            while regame not in ('y', 'n'):
                regame = input(messages["draw"])
                regame = regame.lower()
                election = regame.startswith('y')
                if election:
                    Game(self.option)
            exit()

    def checkWin(self, board):
        for a, b, c in self.WINNERMOVES:
            if board.tableboard[a] + board.tableboard[b] + board.tableboard[c] == 3:
                return True
            if board.tableboard[a] + board.tableboard[b] + board.tableboard[c] == -3:
                return True
