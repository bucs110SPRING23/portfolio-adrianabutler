import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode(1500,1500)
screensize = pygame.display.get_window_size()
x = screensize [0]/2
y = screensize [1]/2
screen.fill("cyan")
pygame.draw.circle(screen, "gold", [x,y], y)
pygame.display.flip
pygame.draw.line(screen, "hotpink", (x+y, y), (x-y,y), width = 5)
pygame.display.flip
pygame.draw.line(screen, "hotpink", (x, x+y), (x, y-x), width = 5)
pygame.display.flip
playerblue = []
playerred = []

score = []

done = False
hitboxes = {
    "red" : pygame.rect(0,0,50,50),
    "blue" : pygame.rect(0,0,50,50)
}

hitboxes["red"].topleft = hitboxes["blue"].topright

colors = {
    "red" : (255,105,180),
    "blue" : (34,139,34)
}

while not done:
    for c,hb in hitboxes.items():
        pygame.draw.rect(screen,colors[c],hb)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["red"].collidepoint(event.pos):
                score = "red"
            elif hitboxes["blue"].collidepoint(event.post):
                score = "blue"
    for _ in range(11):
        for i in range(2):
            dart1 = random.randrange(screensize [0])
            dart2 = random.randrange(screensize [1])
            distance_from_center = math.hypot(x-dart1,y-dart2)
            is_in_circle = distance_from_center <= x
            if i == 0:
                if is_in_circle:
                    dart = pygame.draw.circle(screen, "green", [dart1,dart2], 20)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    playerblue.append("hit")
                elif not is_in_circle:
                    dart = pygame.draw.circle(screen, "purple", [dart1,dart2], 20)
                    pygame.display.flip()
                    pygame.time.wait(1000)
            elif i == 1:
                if is_in_circle:
                    dart = pygame.draw.circle(screen, "aquamartine", [dart1,dart2], 20)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    playerred.append("hit")
                elif not is_in_circle:
                    dart = pygame.draw.circle(screen, "magenta", [dart1,dart2], 20)
                    pygame.display.flip()
                    pygame.time.wait(1000)

print(playerred)
print(playerblue)

if len(playerblue) >  len(playerred):
    if score == "blue":
        font = pygame.font.Font(None, 48)
        text = font.render("Blue player won, correct!", True, "black")
        screen.blit(text, (x,y))
        pygame.display.flip()
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("Blue player won, incorrect!", True, "black")
        screen.blit(text, (x,y))
        pygame.display.flip()

elif len(playerblue) < len(playerred):
    if score == "red":
        font = pygame.font.Font(None, 48)
        text = font.render("Red player won, correct", True, "black")
        screen.blit(text, (x,y))
        pygame.display.flip()
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("Red player won, incorrect", True, "black")
        screen.blit(text, (x,y))
        pygame.display.flip()

else:
    if score == "pint" or "green":
        font = pygame.font.Font(None, 48)
        text = font.render("Tie Game!", True, "black")
        screen.blit(text, (x,y))
        pygame.display.flip()

done = True

pygame.time.wait(1000)
