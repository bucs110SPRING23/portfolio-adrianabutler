import pygame
import random
import time

pygame.init()
class food():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    dis_width = 800
    dis_heigth = 600

    dis = pygame.display.set_mode()
    clock = pygame.time.Clock
    snake_block = 10
    snake_speed = 30

    font_style = pygame.font.SysFont(None, 30)


    def gameLoop():
        game_over = False
        game_close = False
        dis_width = 800
        dis_heigth = 600
        x1 = dis_width/2
        y1 = dis_heigth/3

        x1_change = 0
        y1_change = 0

        foodx = round(random.randrange(0, dis_width-snake_block)/10.0)*10
        foody = round(random.randrange(0, dis_width-snake_block)/10.0)*10

        while not game_over:
            def message(msg, color):
                font_style = pygame.font.SysFont(None, 30)
                dis_width = 800
                dis_heigth = 600
                dis = pygame.display.set_mode()
                mesg = font_style.render(msg, True, color)
                dis.blit(mesg, [dis_width/3, dis_heigth/3])
            message("You Lost! Press Q-Quit or C-Play Again", 'red')
            pygame.display.update()

            for event in pygame.event.get():
                def gameLoop():
                    game_over = False
                    game_close = False
                    dis_width = 800
                    dis_heigth = 600
                    x1 = dis_width/2
                    y1 = dis_heigth/3

                    x1_change = 0
                    y1_change = 0

                    foodx = round(random.randrange(0, dis_width-snake_block)/10.0)*10
                    foody = round(random.randrange(0, dis_width-snake_block)/10.0)*10

                snake_block = 10
                snake_speed = 30
                if event.type == pygame.KEYDOWN:
                   if event.type == pygame.K_q:
                       game_over = True
                game_close = False
                if event.type == pygame.K_c: 
                    gameLoop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    dis_width = 800
    dis_heigth = 600
    x1 = dis_width/2
    y1 = dis_heigth/3
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width-snake_block)/10.0)*10
    foody = round(random.randrange(0, dis_width-snake_block)/10.0)*10
    pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()
pygame.quit()
quit()
gameLoop()