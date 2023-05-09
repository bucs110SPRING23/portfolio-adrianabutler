import pygame
import time
import random

class score:
    import length
    pygame.init()
    Length_of_snake = 1
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    x1 = dis_width / 2
    y1 = dis_height / 2
    snake_block = 10
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    Your_score = Length_of_snake - 1
 
    pygame.display.update()
 
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

 
    pygame.quit()
quit()