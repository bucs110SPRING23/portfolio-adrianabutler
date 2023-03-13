# pygame keeps track of display image and next image
import pygame
pygame.init()
screen=pygame.display.set_mode()
pygame.draw.circle(screen,'cyan',[200,150], 50)
pygame.display.flip()