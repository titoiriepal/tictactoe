import os


class Board:

    def __init__(self, character1, character2):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tableboard = self.createTable(self.board)
        self.playerCharacter = (' ', character1, character2)

    def createTable(self, board):
        return [j for i in board for j in i]

    def assignValue(self, turn, move, value):
        self.tableboard[move - 1] = value
        self.displayBoard()

    def fillBoard(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = self.tableboard[(i*3)+j]

    def displayBoard(self):
        os.system("cls")
        self.fillBoard()
        count = 0
        for [a, b, c] in self.board:
            print('     |     |')
            print(f'  {self.playerCharacter[a]}  |  {self.playerCharacter[b]}  |  {self.playerCharacter[c]}')
            if count != 2:
                print('_____|_____|_____')
            else:
                print('     |     |\n \n')
            count += 1
        self.printFreeMoves()

    def printFreeMoves(self):

        def getFill(displacement=0):
            table = []
            for i in range(0, 3):
                position = (displacement * 3) + i
                if self.tableboard[position] != 0:
                    character = " "
                else:
                    character = str(position + 1)
                table.append(character)
            return table

        for i in range(0, 3):
            freeMoves = getFill(i)
            if i != 2:
                print(f'                ' + "\033[4;37m" + f'{freeMoves[0]}|{freeMoves[1]}|{freeMoves[2]}' + '\033[0;37m')
            else:
                print(f'                {freeMoves[0]}|{freeMoves[1]}|{freeMoves[2]}')
