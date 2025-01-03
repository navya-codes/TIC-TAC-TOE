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
pygame.display.set_caption("TIC-TAC-TOE")

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
                                   

def player_clicks():
    pos = pygame.mouse.get_pos()
    row = pos[1] // 200
    col = pos[0] // 200

    if board[row][col] == 0:
        board[row][col] = 1  # 1 is for 'X', 2 would be for 'O'

def check_winner():
    # Check horizontal and vertical lines
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return True

    # Check diagonal lines
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return True

    return False

def check_winner():
    # Check horizontal and vertical lines
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return True

    # Check diagonal lines
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return True

    return False
