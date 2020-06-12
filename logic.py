##//////////////////////////////////////////////////////////////////////////////
## Program    : logic.py
##
## Author     : Keit Vu and Michael Cooney
## Date       : Summer 2020
## Description: logic files for minesweeper game
##
##//////////////////////////////////////////////////////////////////////////////

class Empty:
    #counter variable, getNumberBombs
    def __init__(self):
        self = self
        self.var = 1

    #we never input this variable
    def printVar(self):
        print(self.var)

        
    #def countBombs(self, gameBoard = []):
        #pseudo code
        # for x in gameBoard:
        #     if type is "bomb":
        #         bombs = bombs + 1
    #var for number of surrounding bombs, var to say we're not a bomb
#class Bomb:

if __name__ == "__main__":
    x = Empty()
    x.printVar()
