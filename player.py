import game
import random
from messages import messages


class Player:
    WINNERMOVES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
    SQUARES = [0, 2, 6, 8]
    NOTSQUARES = [1, 3, 5, 7]

    def __init__(self, value, character):
        self.value = value
        self.character = character

    def chooseMove(self, turn, board):
        move = None
        while move is None:
            currPlayer = '1' if turn % 2 else '2'
            msg = messages["player"] + currPlayer
            move = input(f'{msg}{messages["inputNumber"]}').lower()

            if move == 'q':
                exit()
            try:
                move = int(move)
            except ValueError:
                print(messages["validateNumber"])
                move = None

            try:
                if move < 1 or move > 9:
                    print(messages["outOfRange"])
                    move = None
                else:
                    if board.tableboard[move - 1] != 0:
                        print(messages["wrongNumber"])
                        move = None
            except TypeError:
                move = None
        return move

    def cpuMove(self, tablero, turn):
        move = 10

        if turn == 1:
            move = 4
            return move
        if turn in (2, 3):
            if tablero.tableboard[4] == 0:
                move = 4
                return move
            else:
                return self.chooseSquare(tablero, turn)
        if turn > 3:
            return self.checkMove(tablero)

    def chooseSquare(self, tablero, turn):
        fail = random.randint(0, 10)
        if turn == 2:
            if fail == 5:
                return random.choice(self.NOTSQUARES)
            return random.choice(self.SQUARES)
        if turn == 3:
            lastMove = tablero.tableboard.index(-1)
            if lastMove == 4:
                myLastMove = tablero.tableboard.index(1)
                if myLastMove == 0 or myLastMove == 8:
                    return random.choice([2, 6])
                else:
                    return random.choice([0, 8])
            if lastMove not in self.SQUARES:
                if lastMove == 1 or lastMove == 7:
                    return lastMove + 1
                else:
                    return lastMove + 3
            else:
                if lastMove == 0 or lastMove == 8:
                    return random.choice([2, 6])
                else:
                    return random.choice([0, 8])

    def checkMove(self, tablero):
        markRival = 1

        for i in range(0, 9):
            if tablero.tableboard[i] == 0:
                tablero.tableboard[i] = self.value
                victory = self.checkWin(tablero)
                tablero.tableboard[i] = 0
                if victory is True:
                    return i

        for i in range(0, 9):
            if tablero.tableboard[i] == 0:
                tablero.tableboard[i] = markRival
                victory = self.checkWin(tablero)
                tablero.tableboard[i] = 0
                if victory is True:
                    return i

        return self.notObligateMove(tablero, self.value, markRival)

    def notObligateMove(self, tablero, markPlayer, markRival):
        maximum = 0
        move = 10

        def checkTable(move, maximum):
            goodcounts = 0
            for a, b, c in self.WINNERMOVES:
                table = [tablero.tableboard[a], tablero.tableboard[b], tablero.tableboard[c]]
                if table.count(markPlayer) == 2 and markRival not in table:
                    goodcounts += 1
                if goodcounts > maximum:
                    maximum = goodcounts
                    move = i
            return [move, maximum]

        for i in range(0, 9):
            if tablero.tableboard[i] == 0:
                tablero.tableboard[i] = markPlayer
                moveAndMaximum = checkTable(move, maximum)
                move = moveAndMaximum[0]
                maximum = moveAndMaximum[1]
                tablero.tableboard[i] = 0

        if move != 10:
            return move

        for i in self.NOTSQUARES:
            if tablero.tableboard[i] == 0:
                return i

        for i in self.SQUARES:
            if tablero.tableboard[i] == 0:
                return i
        return move

    def checkWin(self, tablero):
        for a, b, c in self.WINNERMOVES:
            if tablero.tableboard[a] + tablero.tableboard[b] + tablero.tableboard[c] == 3:
                return True
            if tablero.tableboard[a] + tablero.tableboard[b] + tablero.tableboard[c] == -3:
                return True
