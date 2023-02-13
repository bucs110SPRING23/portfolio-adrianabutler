import pygame
pygame.init()
screen=pygame.display.set_mode()
screen_size=screen.get_size()
dimensions=[screen_size[0]/2, screen_size[1]/2,250,250]
pygame.draw.rect(screen,"black", dimensions)