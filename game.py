import pygame
import sys

# Initialize pygame
pygame.init()

# Set the screen dimensions
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
LINE_COLOR = (28, 170, 156)
CIRCLE_COLOR = (242, 85, 96)
X_COLOR = (28, 170, 156)
BG_COLOR = (28, 170, 156)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
SPACE = 55

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Create a 3x3 grid (empty cells initially)
board = [["" for _ in range(3)] for _ in range(3)]

# Set the initial player (X)
current_player = "X"

# Function to draw lines (grid)
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

# Function to draw X or O
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, X_COLOR, (col * 100 + 25, row * 100 + 25), (col * 100 + 75, row * 100 + 75), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 100 + 25, row * 100 + 75), (col * 100 + 75, row * 100 + 25), X_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * 100 + 50, row * 100 + 50), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

# Function to reset the game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    draw_lines()

# Function to check if the board is full
def is_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

# Main game loop
def main():
    global current_player
    draw_lines()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] // 100
                mouseY = event.pos[1] // 100

                # If the cell is empty, place the player's mark
                if board[mouseY][mouseX] == "":
                    board[mouseY][mouseX] = current_player
                    if check_winner():
                        print(f"Player {current_player} wins!")
                        pygame.time.wait(500)
                        reset_game()
                    elif is_full():
                        print("It's a draw!")
                        pygame.time.wait(500)
                        reset_game()
                    else:
                        current_player = "O" if current_player == "X" else "X"

            # Redraw the figures (X or O)
            draw_figures()

        pygame.display.update()

if __name__ == "__main__":
    main()