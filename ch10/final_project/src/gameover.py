import pygame
pygame.init()
from src.Player import player
from src.food import food
from src.longerandscore import score
from src.controls import controls
class over:
    red = (255, 0, 0)

    game_over = False

    snake_block = 10

    clock = pygame.time.Clock()
    snake_speed = 30

    def message(msg, color):
        font_style = pygame.font.SysFont(None, 50)
        dis = pygame.display.set_mode()
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, 400, 300)

    x1 = 400
    y1 = 300

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    if game_over is True:
        message("You Lost", 'red')
pygame.display.update()   