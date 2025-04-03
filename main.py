from gui import *
from logic import *
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
FPS = 60

draw_line()
player = 1 
game_over = False

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0] // square_size
            mousey = event.pos[1] // square_size
            if availabe_squares(mousey , mousex):
                mark_square(mousey , mousex , player)
                if check_win(player):
                    game_over = True
                player = player % 2 +1
                if not game_over :
                    if bestmove():
                        if check_win(2):
                            game_over = True
                        player = player % 2 + 1 

                        if not game_over :
                            if if_board_isfull():
                                game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
                player = 1 
    # Inside the game loop (main.py)
    if not game_over:
      draw_figures()
    else:
      if check_win(1):
        draw_line(green)
        draw_figures(green)
      elif check_win(2):
        draw_line(red)
        draw_figures(red)
    pygame.display.update()