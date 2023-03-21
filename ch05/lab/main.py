import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
        count = count + 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3*n+1)
            while n == 1.0:
                return count

def threenp1range(upperlimit):
    threenplus1_dictionary = {}
    for n in range(2, upperlimit+1):
        iters = threenp1(n)
        threenplus1_dictionary = iters
        return threenplus1_dictionary

def graph(value):
    points = threenp1range(value)
    coordinates = points.items()
    print(coordinates)
    pygame.init
    screen = pygame.display.set_mode((500,500))
    pygame.draw.lines(screen, "black", False, list(coordinates))
    pygame.display.flip()
    new_screen = pygame.transform.flip(screen, False, True)
    width, height = new_screen.get_size()
    new_screen = pygame.transform.scale(new_screen, (width * 5, height * 5))
    new_screen.blit(new_screen, (0,0))
    pygame.display.flip()
    pygame.time.wait(1000)

    currentmax = 0
    for key, value in coordinates:
        if value > currentmax:
            currentmax = value
        else:
            currentmax != value
    print(currentmax)
    font = pygame.font.Font(None, 100)
    text = font.render(str(currentmax), True, "cyan")
    pos = (20,20)
    screen.blit(text, pos)
    pygame.display.flip()
    pygame.time.wait(1500)

    return coordinates

def main():
    value = 600
    print(threenp1(value))
    print(threenp1range(value))
    graph(value)

main()