import pygame
pygame.init


class controls():
    dis = pygame.display.set_mode()

    game_over = False

    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        x1 += x1_change
        y1 += y1_change
        dis.fill('white')
        pygame.draw.rect(dis, 'black', [x1, y1, 10, 10])

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()