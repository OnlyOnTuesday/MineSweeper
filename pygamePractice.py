##//////////////////////////////////////////////////////////////////////////////
## Program: pygamePractice.py
##
## Author: Michael Cooney
## Date: Summer 2020
## Description: Getting familiar with the pygame library
##
##//////////////////////////////////////////////////////////////////////////////

import pygame
from pygame.locals import *

pygame.init()

disp = pygame.display.set_mode()
r = pygame.Rect(10,20,30,40)
pygame.draw.rect(disp, 102, r)
while 1:
    pygame.display.update()
