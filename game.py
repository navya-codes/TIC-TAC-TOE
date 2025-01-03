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

#game board
board = np.zeros((3, 3))  # A 3x3 matrix

# Function to draw the grid
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# Function to draw the X and O shapes
def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 50, row * 200 + 50),
                                 (col * 200 + 150, row * 200 + 150), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 150, row * 200 + 50),
                                 (col * 200 + 50, row * 200 + 150), CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * 200 + 100, row * 200 + 100),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)