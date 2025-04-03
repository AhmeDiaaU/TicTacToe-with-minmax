import sys
import numpy as np
import pygame
import pygame.draw_py  

white = (255,255,255)# defult
orange = (255, 165, 0) # tie
red = (255,0,0) #lose
green = (0,255,0)#win
black = (0,0,0) #background

# proportions and sizes 

width = 300 
height = 300 
line_width = 5 
board_rows = 3
board_cols = 3 
square_size = width // board_cols
circle_radius = square_size // 3 
width_circle = 15
cross_width = 25

screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("Tic Tac Toe AI")
screen.fill(black)


board = np.zeros((board_rows , board_cols)) # zero means filed is unused

def draw_line(color = white):
    for i in range(1 , board_rows):
        pygame.draw.line(screen , color , ( 0, square_size * i) , (width , square_size * i) , line_width)
        pygame.draw.line(screen , color , ( square_size * i , 0 ) , (square_size * i , height ) , line_width)


def draw_figures (color = white):
    """Draw the game pieces (circles and crosses) on the board.
    
    This function iterates through the game board and draws:
    - Circles (O) for player 1
    - Crosses (X) for player 2
    
    Args:
        color (tuple): RGB color tuple for drawing the figures. 
                      Defaults to white (255,255,255).
    
    Note:
        - Player 1's pieces are circles
        - Player 2's pieces are crosses
        - Board positions with 0 are left empty
    """

    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                centerX = col * square_size + square_size//2
                centerY = row * square_size + square_size//2
                pygame.draw.circle(screen, color, (centerX, centerY), circle_radius, width_circle)
            elif board[row][col] == 2:
                start_x = col * square_size + square_size//4
                start_y = row * square_size + square_size//4
                end_x = col * square_size + 3*square_size//4
                end_y = row * square_size + 3*square_size//4
                pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), cross_width)
                pygame.draw.line(screen, color, (start_x, end_y), (end_x, start_y), cross_width)

def restart_game():
    """Restarts the game by clearing the screen and resetting the board state.
    
    Fills the screen with black, redraws the grid lines, and sets all
    board positions to 0.
    """
    
    screen.fill(black)
    draw_line()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0 