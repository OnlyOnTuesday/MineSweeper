##//////////////////////////////////////////////////////////////////////////////
## Program: pygamePractice.py
##
## Author: Michael Cooney
## Date: Summer 2020
## Description: Getting familiar with the pygame library
##
##//////////////////////////////////////////////////////////////////////////////

#the second line is optional but adds some constants and functions that wouldn't
#be in the script otherwise (not sure what though yet)
import pygame
from pygame.locals import *

#prepare all modules to be used.  Each can be inited individually too
pygame.init()

#create the surface that will be seen on the screen
#this function should have a parameter that determines the window size
disp = pygame.display.set_mode()

#create a rectangle
#I need to figure out what the first two variable do. Are they coordinates?
r = pygame.Rect(10,20,30,40)
pygame.draw.rect(disp, 102, r)

#display the rectangle until the user stops python
while 1:
    pygame.display.update()
