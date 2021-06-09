import game
import os
import curses


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
            **                                                                                      **
            **                                      1. Jugador vs Jugador                           **
            **                                      2. Salir                                        **
            **                                                                                      **
            ******************************************************************************************
            ******************************************************************************************'''
        self.printMenu()

    def chooseOption(self):
        tableOption = ['1', '2']
        option = None
        while option is None:
            option = input('\n Por favor introduce tu opción: ')
            if option not in tableOption:
                option = None
                self.printMenu()
            elif option == tableOption[0]:
                game.Game()
            else:
                exit()

    def printMenu(self):
        os.system("cls")
        print(self.img)
        self.chooseOption()


Menu()
