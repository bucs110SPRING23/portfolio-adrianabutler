import pygame

def threenp1(n):
    while n > 1.0:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return None

def threenp1count(n):
    count = 0
    while n > 1.0:
        count = count + 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    if n == 1:
        count = count + 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for _ in range(2, upper_limit + 1):
        result = threenp1count(_)
        objs_in_sequence.update({_ : result})
    return objs_in_sequence

def main():
    result = threenp1range(20)
    print(result)
    graph_coordinates(result)

def graph_coordinates(d):
    startpoint = (0, 0)
    pygame.init()
    screen = pygame.display.set_mode()
    max_so_far = 0
    for k, v in d.items():
        pygame.draw.line(screen, "red", startpoint, (k * 20, v * 20))
        startpoint = (k * 20 , v * 20)
    for k, v in d.items():
        if v > max_so_far:
            max_so_far = v
    width, height = screen.get_size()
    newdisplay = pygame.transform.scale(screen, (width , height))
    newdisplay = pygame.transform.flip(newdisplay, False, True)
    screen.blit(newdisplay, (0, 0))
    font = pygame.font.Font(None, 48)
    message = str(max_so_far)
    msg = font.render("The max is " + message + " iterations!", True, "blue")
    screen.blit(msg, (10, 10))
    pygame.display.flip()
    pygame.time.wait(5000)
main()