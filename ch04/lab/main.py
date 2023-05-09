import pygame
from pygame.event import get as event_getter
import random
import math

pygame.init()
pygame.display.set_caption("Dartboard")
screen_width=1000
screen_height=1000
screen=pygame.display.set_mode([screen_width, screen_height])
screen.fill((153, 184, 152))
pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)


pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
pygame.display.update()
message = """
        There are two players, Red vs Blue.
        Red player's darts that hit the target are red.
        Blue player's darts that hit the target are blue.
        Darts that miss the target are white, regardless of which player threw them.
        Press enter to continue.
        """
response = input(message)
pygame.display.flip()

print("Which player will win? To pick the Red Player left click the red box. To pick the blue player left click the blue box.")
red_area = pygame.Rect(80, 300, 400, 400)
blue_area = pygame.Rect((520, 300, 400, 400))

Red_points = []
Blue_points = []
Miss_points = []

run = True
while True:
    pygame.display.flip()
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(80, 300, 400, 400), width = 0)
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(520, 300, 400, 400), width = 0)
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if red_area.collidepoint(event.pos):
                    print("Red Player chosen.")
                    screen.fill((153, 184, 152))
                    pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)
                    pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
                    pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
                    pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
                    pygame.display.update()
                    for darts in range(5):
                        x1 = random.randrange(0,1000)
                        x2 = random.randrange(0,1000)
                        y1 = random.randrange(0,1000)
                        y2 = random.randrange(0,1000)
                        distance_from_center1 = math.hypot(x1-500, y1-500)
                        distance_from_center2 = math.hypot(x2-500, y2-500)
                        is_in_circle1 = distance_from_center1 <= screen_width/2
                        is_in_circle2 = distance_from_center2 <= screen_width/2
                        print(distance_from_center1, screen_width/2)
                        print(is_in_circle1)
                        print(distance_from_center2, screen_width/2)
                        print(is_in_circle2)
                        if is_in_circle1:
                            pygame.draw.circle(screen, (255,0,0), [x1,y1], 10)
                            Red_points.append((x1,y1))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                        else:
                            pygame.draw.circle(screen, (255, 255, 255), [x1,y1], 10)
                            Miss_points.append((x1,y1))
                            pygame.display.flip()
                            pygame.time.wait(1000) 
                        if is_in_circle2:
                            pygame.draw.circle(screen, (0, 0, 255), [x2,y2], 10)
                            Blue_points.append((x2,y2))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                        else: 
                            pygame.draw.circle(screen, (255, 255, 255), [x2,y2], 10)
                            Red_points.append((x2,y2))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                elif blue_area.collidepoint(event.pos):
                    print("Blue Player chosen.")
                    screen.fill((153, 184, 152))
                    pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)
                    pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
                    pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
                    pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
                    pygame.display.update()
                    for darts in range(5):
                        x1 = random.randrange(0,1000)
                        x2 = random.randrange(0,1000)
                        y1 = random.randrange(0,1000)
                        y2 = random.randrange(0,1000)
                        distance_from_center1 = math.hypot(x1-500, y1-500)
                        distance_from_center2 = math.hypot(x2-500, y2-500)
                        is_in_circle1 = distance_from_center1 <= screen_width/2
                        is_in_circle2 = distance_from_center2 <= screen_width/2
                        print(distance_from_center1, screen_width/2)
                        print(is_in_circle1)
                        print(distance_from_center2, screen_width/2)
                        print(is_in_circle2)
                        if is_in_circle1:
                            pygame.draw.circle(screen, (255,0,0), [x1,y1], 10)
                            Red_points.append((x1,y1))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                        else:
                            pygame.draw.circle(screen, (255, 255, 255), [x1,y1], 10)
                            Miss_points.append((x1,y1))
                            pygame.display.flip()
                            pygame.time.wait(1000) 
                        if is_in_circle2:
                            pygame.draw.circle(screen, (0, 0, 255), [x2,y2], 10)
                            Blue_points.append((x2,y2))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                        else: 
                            pygame.draw.circle(screen, (255, 255, 255), [x2,y2], 10)
                            Miss_points.append((x2,y2))
                            pygame.display.flip()
                            pygame.time.wait(1000)
            print("Red Player won", len(Red_points), "points.")
            print("Blue Player won", len(Blue_points), "points.")
            print(len(Miss_points), "darts missed the target.")
            if len(Red_points) > len(Blue_points):
                print("Red Player won!")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if red_area.collidepoint(event.pos):
                            print("You chose the winning player!")
                        else:
                            print("You chose the losing player.")
            elif len(Red_points) < len(Blue_points):
                print("Blue Player won!")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if blue_area.collidepoint(event.pos):
                            print("You chose the winning player!")
                        else:
                            print("You chose the losing player.")
            else:
                print("It is a tie!")
screen.fill((153, 184, 152))
pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)
pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
pygame.display.update()