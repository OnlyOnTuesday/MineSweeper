import sys
import pygame
from pygame.locals import *

class Button:

    def __init__(self, textColor, colorLight, colorDark, font, text):
        self.textColor = textColor
        self.colorLight = colorLight
        self.colorDark = colorDark
        self.font = pygame.font.SysFont(font, 25)
        self.text = self.font.render(text, True, textColor)

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

pygame.init()

res = (720, 720)
screen = pygame.display.set_mode(res)

#white
textColor = (255, 255, 255)

#light shade of button
colorLightButton = (170, 170, 170)

#dark shade of button
colorDarkButton = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()
# xStart = 0
# yStart = 0
# side = 50

but = Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Quit")
but2 = Button(textColor, colorLightButton, colorDarkButton, "Corbel", "Start")
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+50 and height/2 <= mouse[1] <= height/2+50:
                pygame.quit()

    screen.fill((60,25,60))
    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+50 and height/2 <= mouse[1] <= height/2+50:
        but.drawLight(screen, [width/2, height/2, 50, 50])
    else:
        but.drawDark(screen, [width/2, height/2, 50, 50])

    # if width/3 < mouse[0] <= width/3+50 and height/2 <= mouse[1] <= height/2+50:
    #     but2.drawLight(screen, [width/3, height/2, 50, 50])
    # else:
    #     but2.drawDark(screen, [width/3, height/2, 50, 50])
        

    # for i in range(10):
    #     for j in range(10):
    #         #make separate objects
    #         but.drawDark(screen, [xStart, yStart, side, side])
    #         xStart += 60
    #     yStart += 60

    pygame.display.update()
                      
