import game
import os
import curses
from messages import messages


class Menu():

    def __init__(self):
        self.img = '''
            ******************************************************************************************
            ******************************************************************************************
            **                                                                                      **
            **                                                                                      **
            **                                         TIC,                                         **
            **                                                  TAC,                                **
            **                                                           TOE                        **
            **                                                                                      **
            **                                                                                      **
            **              by Tito                                                                 **
            **                                                                                      **
            **                                                                                      **
            **                                                                                      **
            **           Elige tu opción:                                                           **
            **                                      1. Jugador vs Jugador                           **
            **                                      2. Jugador vs CPU                               **
            **                                      3. Salir                                        **
            **                                                                                      **
            ******************************************************************************************
            ******************************************************************************************'''
        self.printMenu()

    def chooseOption(self):
        tableOption = ['1', '2', '3']
        option = None
        while option is None:
            option = input(messages["introOption"])
            if option not in tableOption:
                option = None
                self.printMenu()
            elif option == tableOption[2]:
                exit()
            else:
                game.Game(option)

    def printMenu(self):
        os.system("cls")
        print(messages["menu"])
        self.chooseOption()


Menu()
