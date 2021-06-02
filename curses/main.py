import os
import curses
import graphic

class Game:
    def __init__(self):
        self.breed = 'Game'
    
    def playGame(self, board, stdscr, win):
        turn = 1
        while True:
            move = 'a'
            while move not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                player = Player()
                move = player.chooseMove(turn, win)
                if board.board[move - 1] != 0:
                    win.addstr(1, 1, 'El número elegido ya esta ocupado, intentalo de nuevo')
                    move = 'a'
            board.board = self.assignTab(turn, move, board.board)
            board.displayBoard(stdscr, win)
            self.checkWin(board, win, stdscr)
            if turn == 9:
                win.clear()
                win.addstr(6, 6, 'Ha sido un empate')
                board.endCurse(stdscr)
            turn = turn + 1
        
    def assignTab(self, turn, move, board):
        if turn % 2 == 1:
            board[move - 1] = 1
        else:
            board[move - 1] = -1
        return board

    def checkWin(self,board,win,stdscr):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if board.board[a] + board.board[b] + board.board[c] == 3:
                win.addstr(6, 6, 'Gana el jugador 1')
                board.endCurse(stdscr)
            if board.board[a] + board.board[b] + board.board[c] == -3:
                win.addstr(6, 6, 'Gana el jugador 2')
                board.endCurse(stdscr)
            










class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def createCurse(self):
        os.system('MODE CON: COLS=150 LINES=60')
        stdscr = curses.initscr()
        stdscr.keypad(True)
        curses.noecho()
        curses.cbreak()
        return stdscr
    
    def endCurse(self,stdscr):
        curses.nocbreak()
        curses.echo()
        stdscr.keypad(False)
        curses.endwin
        exit()

    
    def createWindow(self):
        win = curses.newwin(32, 50, 1, 65)
        return win


    def displayBoard(self,stdscr,win):
        for i in range(0, 3):
            indx1 = (self.board[i*3])
            indx2 = (self.board[(i*3)+1])
            indx3 = (self.board[(i*3)+2])
            chain = str(indx1) + str(indx2) + str(indx3)
            cursorAt =(i*9)+i+5
            stdscr.addstr(cursorAt, 0, graphic.graphics[chain])
            if i !=2:
                 stdscr.addstr(cursorAt+9, 0, graphic.graphics["separador"])
            stdscr.refresh()  
    
        
            

    



class Player:
    def __init__(self):
        self.breed = 'Player'

    def chooseMove(self, turn, win):
        if turn % 2 == 1:
            msg = 'Jugador 1'
        else:
            msg = 'Jugador 2'
        win.clear()
        win.addstr( 3, 3,f'{msg}, por favor introduce tu movimento')
        win.addstr( 4, 3,'o pulsa q para salir: ' )
        move = win.getkey()
        move = move.lower()     
        if move == 'q':
            exit()
        return int(move)

    

b = Board()
pantalla = b.createCurse()
win = b.createWindow()
b.displayBoard(pantalla, win)
g = Game()
g.playGame(b, pantalla, win)
    