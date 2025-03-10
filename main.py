# Owen Perez
# 3/7/2025
# shapes-using-dictionaries

import pygame
import random
import sys
from config import init_game, handle_events, draw_mountain, draw_tree, draw_sky, draw_text, COLORS

# Initialize game
screen = init_game()
clock = pygame.time.Clock()

# Define font properties
font_name1 = "FreeMono.ttf"
font_name2 = "DejaVuSans.ttf"
font_size1 = 36
font_size2 = 48
font_size3 = 30

# Define text positions
text_position1 = (50, 50)
text_position2 = (225, 135)
text_position3 = (220, 370)
text_position4 = (100, 500)
text_position5 = (300, 250)

running = True
while running:
    screen.fill(COLORS["WHITE"])  # Fill screen before drawing
    draw_sky(screen)
    
    # Draw mountains
    mountains = [
        (100, 300, 300, 200, "DARK_GRAY"),
        (400, 320, 350, 220, "GRAY"),
        (250, 350, 400, 250, "DARK_GRAY")
    ]
    for m in mountains:
        draw_mountain(screen, *m)
    
    # Draw trees
    for _ in range(10):
        draw_tree(screen, random.randint(50, 750), random.randint(400, 500))
    
    # Draw text with different fonts and styles
    draw_text(screen, "Welcome to Pygame!", font_size1, font_name1, COLORS["RED"], text_position1, italic=True)
    draw_text(screen, "Game Over!", font_size2, font_name2, COLORS["PURPLE"], text_position2, bold=True)
    draw_text(screen, "You Won!", font_size3, font_name1, COLORS["ORANGE"], text_position3, italic=True, bold=True)
    draw_text(screen, "Press R to Restart", font_size1, font_name2, COLORS["BLUE"], text_position4)
    draw_text(screen, "Enjoy the Game!", font_size3, font_name1, COLORS["DARK_BLUE"], text_position5)
    
    running = handle_events()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
