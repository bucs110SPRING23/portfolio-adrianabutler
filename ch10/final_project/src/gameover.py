import pygame
pygame.init()
class over:
    red = (255, 0, 0)

dis = pygame.display.set_mode()

game_over = False

snake_block = 10

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, 400, 300)

x1 = 400
y1 = 300

if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
    game_over = True

    if game_over is True:
        message("You Lost", 'red')
pygame.display.update()   