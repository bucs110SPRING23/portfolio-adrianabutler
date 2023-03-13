import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()
hitbox_width = width/2
hitbox_height = height/2

hitboxes = {
    "red" : pygame.rect(0, 0, hitbox_width, hitbox_height),
    "blue" : pygame.rect(0, 0, hitbox_width, hitbox_height)
}

hitboxes["blue"].topleft = hitboxes["red"].topright
main_colors = {
    "red" : (200, 200, 0),
    "blue" : (0, 200, 0)
}
hightlight_colors = {
    "red" : (255, 255, 0),
    "blue" : (0, 255, 0)
}
font = pygame.font.Font(None, 48)
text = font.render("Who will win?: Red or Blue?", True, "Black")
text = font.render("Click a box", True, "black")
screen.blit(text, (0, 0))
screen = pygame.display.set_mode((1500, 1500))
pygame.display.get_window_size()
screensize = 1500
screen.fill("aquamarine")
pygame.draw.circle(screen, "black", (850,850), 850)
pygame.draw.circle(screen, "purple", (850, 850), 850)
pygame.draw.line(screen, "black", (850, 0), (850, 1500))
pygame.draw.line(screen, "black", (0, 850), (1500, 850))
playerblue_score = 0
playerred_score = 0
for i in range (11):
    x1 = 850
    y1 = 850
    x2 = random.randrange(0, screensize)
    y2 = random.randrange(0, screensize)
    playerblue = (x2, y2)
    distance_from_center = math.hypot(x1 - x2, y1 - y2)
    is_in_circle = distance_from_center <= 850
    if is_in_circle:
        pygame.draw.circle(screen, "blue", (x2, y2), 10)
        playerblue_score += 1
    else:
        pygame.draw.circle(screen, "orange", (x2, y2), 10)
    x3 = random.randrange(0, screensize)
    y3 = random.randrange(0, screensize)
    playerred = (x3, y3)
    distance_from_center = math.hypot(x1 - x3, y1 - y3)
    is_in_circle = distance_from_center <= 850
    if is_in_circle:
        pygame.draw.circle(screen, "red", (x3, y3), 10)
        playerred_score += 1
    else:
        pygame.draw.circle(screen, "orange", (x3, y3), 10)
if playerblue_score > playerred_score:
    font = pygame.font.Font(None, 48)
    msg = ("Player Blue won and they scored" + str(playerblue_score) + "points!")
    text = font.render(msg, True, "White")
    screen.blit(text, (0,0))
elif playerblue_score < playerred_score:
    font = pygame.font.Font(None, 48)
    msg = ("Player Red won and they scored", + str(playerred_score) + "points!")
    text = font.render(msg, True, "white")
    screen.blit(text, (0,0))
elif playerblue_score == playerred_score:
    font = pygame.font.Font(None, 48)
    msg = ("It's a tie! They both scored" + str(playerblue_score) + "ponts!")
    text = font.render (msg, True, "white")
    screen.blit(text, (0,0))

pygame.display.flip()
pygame.time.wait(1000)