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
        self.bomb = False
        self.count = 0

    #we never input this variable
    def isBomb(self):
        print(self.bomb)

        
    #def countBombs(self, gameBoard = []):
        #pseudo code
        # for x in gameBoard:
        #     if type is "bomb":
        #         count += 1


#class Bomb:

if __name__ == "__main__":
    x = Empty()
    x.isBomb()
    #x.countBombs(gameboard)
