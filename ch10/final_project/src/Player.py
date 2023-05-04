import pygame
pygame.init()
dis = pygame.display.set_mode()

blue = (0,0,225)
red = (255,0,0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, blue, [100,50,50,50])
    pygame.display.update()
pygame.quit
quit()