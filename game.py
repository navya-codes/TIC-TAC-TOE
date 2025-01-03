import pygame
import sys
import numpy as np

pygame.init()

#setting up the window size
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
LINE_COLOUR = (28, 170, 156)
CIRCLE_COLOUR = (242, 85, 96)
CROSS_COLOUR = (28,170,156) 
BACKGROUND_COLOUR= (28,170, 156)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_captiom("TIC-TAC-TOE")