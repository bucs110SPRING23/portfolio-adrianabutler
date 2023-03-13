import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000,1000))
screensize = pygame.display.get_window_size()
x = screensize[0]/2
y = screensize[1]/2
screen.fill("cyan")
pygame.draw.circle(screen, "yellow", [x,y], y)
pygame.display.flip
pygame.draw.line(screen, "pink", (x+y, y), (x-y, y), width = 4)
pygame.display.flip()
pygame.draw.line(screen, "pink", (x, x+y), (x, y-x), width = 4)
pygame.display.flip()

for i in range (10):
    dart1 = random.randrange(screensize[0])
    dart2 = random.randrange(screensize[1])
    distance_from_center = math.hypot(x-dart1, y-dart2)
    is_in_circle = distance_from_center <= x

    if is_in_circle:
        dart = pygame.draw.circle(screen, "green", [dart1,dart2], 20)
        pygame.display.flip()
        pygame.time.wait(2000)
    else:
        dart = pygame.draw.circle(screen, "purple", [dart1,dart2], 20)
        pygame.display.flip()
        pygame.time.wait(2000)

pygame.time.wait(5000)