##//////////////////////////////////////////////////////////////////////////////
## Program    : logic.py
##
## Author     : Keit Vu and Michael Cooney
## Date       : Summer 2020
## Description: logic files for minesweeper game
##
##//////////////////////////////////////////////////////////////////////////////

#What does this program need to do

#needs to load a gameboard where random pieces are bombs and the rest tell how
#many bombs are surrounding that piece

#needs to be able to put a flag down (so the player can mark where they think a bomb is)




class Empty:
    #What needs to be in this class?:
    #variable to determine whether this space has been clicked yet or not
    #variable to keep track of how many bombs surround this space
    #a way to count those bombs (helper function)
    #a way to display that number (getter function)
    
    #counter variable, getNumberBombs
    def __init__(self):
        self.bomb = False
        self.count = 0

    def isBomb(self):
        print(self.bomb)

        
    #def countBombs(self, gameBoard = []):
        #pseudo code
        # for x in gameBoard:
        #     if type is "bomb":
        #         count += 1


#class Bomb:
    #What needs to be in this class?:
    #variable to determine whether this space has been clicked yet or not
    

if __name__ == "__main__":
    x = Empty()
    x.isBomb()
    #x.countBombs(gameboard)
