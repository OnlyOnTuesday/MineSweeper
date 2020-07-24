import random
import sys
import pygame
from pygame.locals import *

class Button:

    def __init__(self, textColor, colorLight, colorDark, font, text, xPos, yPos, sideLength):
        self.textColor = textColor
        self.colorLight = colorLight
        self.colorDark = colorDark
        self.font = pygame.font.SysFont(font, 25)
        self.text = self.font.render(text, True, textColor)
        self.xPos = xPos
        self.yPos = yPos
        self.sideLength = sideLength

    def setText(self, newText):
        self.text = self.font.render(newText, True, textColor)

    def drawLight(self, surface, pos):
        pygame.draw.rect(surface, self.colorLight, pos)
        pos[0] += 6
        pos[1] += 16
        surface.blit(self.text, pos)

    def drawDark(self, surface, pos):
        pygame.draw.rect(surface, self.colorDark, pos)
        pos[0] += 6
        pos[1] += 16
        surface.blit(self.text, pos)

    def getXPos(self):
        return self.xPos

    def getYpos(self):
        return self.yPos

    def getSideLength(self):
        return self.sideLength


class Bomb(Button):
    def getType(self):
        return "bomb"

class Empty(Button):
    def getType(self):
        return "empty"

pygame.init()

res = (720, 720)
screen = pygame.display.set_mode(res)

#white
textColor = (255, 255, 255)

#light shade of button
colorLightButton = (170, 170, 170)

#dark shade of button
colorDarkButton = (100, 100, 100)

# width = screen.get_width()
# height = screen.get_height()
xStart = 0
yStart = 0
side = 50

#but = Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit")
#but2 = Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Start")
#OBJS = [Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit", xStart)
#        and xStart += 60 for i in range(10)]

def clickedButton(mousePos):
    for i in OBJS:
        if i.getXPos() <= mouse[0] <= i.getXPos() + i.getSideLength()\
           and i.getYpos() <= mouse[1] <= i.getYpos() + i.getSideLength():
            return i

    return None


OBJS = []
for i in range(10):
    #OBJS.append(Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit", xStart, yStart, side))
    x = random.randrange(2)
    if x > 0:
        OBJS.append(Bomb(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit", xStart, yStart, side))
    else:
        OBJS.append(Empty(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit", xStart, yStart, side))
    xStart += 60

while True:

    screen.fill((60,25,60))
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            button = clickedButton(mouse);
            if button is not None:
                print(button.getType())
        # if ev.type == pygame.MOUSEBUTTONDOWN:
        #     if width/2 <= mouse[0] <= width/2+50 and height/2 <= mouse[1] <= height/2+50:
        #         pygame.quit()



    

    for i in OBJS:
        if i.getXPos() <= mouse[0] <= i.getXPos() + i.getSideLength()\
           and i.getYpos() <= mouse[1] <= i.getYpos() + i.getSideLength():
            i.drawDark(screen, [xStart, yStart, side, side])
           #  # for ev in pygame.event.get():
           #  #     # if ev.type == pygame.MOUSEBUTTONDOWN \
           #  #     #    and i.getType() == "bomb":
           #  #     #     print("BOOM")
           #  #     #     i.setText("BOOM")
           #  #     if ev.type == pygame.MOUSEBUTTONDOWN:
           #  #         print(i.getType())
            

        else:
            
            i.drawLight(screen, [xStart, yStart, side, side])
        xStart += 60
    xStart = 0
    #dis()

    pygame.display.update()
    


##
# How to check if hitting button
# Write a function that checks if mouseclick is over button, and then return a
# button if true. return null if otherwise
#
# check that the button is not null and perform an action on the returned object
##
