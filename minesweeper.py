'''
This is a Python program that implements the game Minesweeper. It allows the 
user to specify the size of the game board and the number of mines at the 
beginning of the game. The program uses the Pygame library to display the game 
board and handle user input.

The game board is represented as a two-dimensional list, with each element 
representing a cell on the board. Mines are represented by the value -1, and 
the other cells contain a number representing the number of mines in the 
surrounding cells. The game keeps track of which cells have been revealed and 
which cells have been flagged by the player using separate two-dimensional 
lists.

The main game loop handles user input and updates the game board display. If 
the user clicks on a cell with a mine, the game ends and a message is 
displayed. If the user right-clicks on a cell, it is flagged. If the user left-
clicks on a cell, it is revealed. The game also checks for a win condition, 
which occurs when all cells that do not contain mines have been revealed. If 
the player wins, a message is displayed.
'''

__author__ = 'Andrew Malaty'
__email__ = 'andrew_malaty@hotmail.com'
__date__ = '2022/12/17'

import pygame
import random


# Get board size and number of mines from the player
board_size = int(input("Enter the size of the board (e.g. 10 for a 10x10 board): "))
mines = int(input("Enter the number of mines: "))

# Constants
CELL_SIZE = 50
BOARD_SIZE = board_size
MINES = mines

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Minesweeper")

# Load the images
mine_image = pygame.image.load("mine.png")
flag_image = pygame.image.load("flag.png")

# Initialize the board
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
flagged = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Place the mines randomly on the board
for i in range(MINES):
    x = random.randint(0, BOARD_SIZE - 1)
    y = random.randint(0, BOARD_SIZE - 1)
    board[x][y] = -1

# Calculate the number of mines in the surrounding cells for each cell
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] == -1:
            continue
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x >= 0 and x < BOARD_SIZE and y >= 0 and y < BOARD_SIZE and board[x][y] == -1:
                    board[i][j] += 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x //= CELL_SIZE
            y //= CELL_SIZE
            if event.button == 1:  # Left mouse button
                if board[x][y] == -1:
                    print("You hit a mine! Game over.")
                    running = False
                else:
                    revealed[x][y] = True
            elif event.button == 3:  # Right mouse button
                flagged[x][y] = not flagged[x][y]

    # Draw the board
    screen.fill((255, 255, 255))
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if revealed[i][j]:
                if board[i][j] == -1:
                    screen.blit(mine_image, (i * CELL_SIZE, j * CELL_SIZE))
                else:
                    text = str(board[i][j])
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(text, True, (0, 0, 0))
                    screen.blit(text_surface, (i * CELL_SIZE + 20, j * CELL_SIZE + 10))
            elif flagged[i][j]:
                screen.blit(flag_image, (i * CELL_SIZE, j * CELL_SIZE))
            else:
                pygame.draw.rect(screen, (192, 192, 192), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    pygame.display.flip()

    # Check for a win condition
    win = True
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if not revealed[i][j] and board[i][j] != -1:
                win = False
                break
        if not win:
            break
    if win:
        print("You won! Game over.")
        running = False

pygame.quit()
