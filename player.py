

class Player:

    def __init__(self, value, character):
        self.value = value
        self.character = character

    def chooseMove(self, turn, board):
        move = None
        while move is None:
            currPlayer = '1' if turn % 2 else '2'
            msg = 'Jugador ' + currPlayer
            move = input(f'{msg}, por favor introduce tu movimiento o pulsa q para salir: ').lower()

            if move == 'q':
                exit()
            try:
                move = int(move)
            except ValueError:
                print('Por favor, introduce un número válido')
                move = None

            try:
                if move < 1 or move > 9:
                    print('El número elegido no es una de las casillas. Por favor, introduce un número del 1 al 9')
                    move = None
                else:
                    if board.tableboard[move - 1] != 0:
                        print('El número elegido ya está ocupado, prueba con otro')
                        move = None
            except TypeError:
                move = None
        return move
