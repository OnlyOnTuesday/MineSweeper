##//////////////////////////////////////////////////////////////////////////////
## Program: pygamePractice.py
##
## Author: Michael Cooney
## Date: Summer 2020
## Description: Getting familiar with the pygame library
##
##//////////////////////////////////////////////////////////////////////////////

# #the second line is optional but adds some constants and functions that wouldn't
# #be in the script otherwise (not sure what though yet)
# import pygame
# from pygame.locals import *

# #prepare all modules to be used.  Each can be inited individually too
# pygame.init()

# #create the surface that will be seen on the screen
# #this function should have a parameter that determines the window size
# disp = pygame.display.set_mode()

# #create a rectangle
# #I need to figure out what the first two variable do. Are they coordinates?
# r = pygame.Rect(10,20,30,40)
# pygame.draw.rect(disp, 102, r)

# #display the rectangle until the user stops python
# while 1:
#     pygame.display.update()

import pygame
from pygame.locals import *
import sys

pygame.init()


#screen resolution
res = (720,720)

screen = pygame.display.set_mode(res)

#white color
color = (255, 255, 255)

#light shade of button
colorLight = (170, 170, 170)

#dark shade of button
colorDark = (100, 100, 100)

#store the width of the screen into a var
width = screen.get_width()
#store the height of the screen into a var
height = screen.get_height()

#define a font
smallfont = pygame.font.SysFont("Corbel", 35)

#render text in the button
text = smallfont.render("quit", True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        #check if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    #fills the screen with a color
    screen.fill((60, 25, 60))

    #stores the (x,y) coordinates as a tuple
    mouse = pygame.mouse.get_pos()

    #if mouse is hovered on button it changes to lighter shade
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, colorLight, [width/2, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, colorDark, [width/2, height/2, 140, 40])

    #superimposing text onto our button
    screen.blit(text, (width/2+50, height/2))

    #update the frames of the game
    pygame.display.update()
