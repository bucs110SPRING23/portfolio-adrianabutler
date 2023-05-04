import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode()

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 40)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width-snake_block)/10)*10
    foody = round(random.randrange(0, dis_height-snake_block)/10)*10

    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list)>length_of_snake:
        del snake_list[0]
    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True
    our_snake(snake_block, snake_list)
    your_score(length_of_snake-1)
    pygame.display.update()
pygame.quit()
quit()

gameLoop()