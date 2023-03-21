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
        count = threenp1(n)
        threenplus1_dictionary = count
        return threenplus1_dictionary

def graph_coordinates(threeplus1_iters_dict):
    pygame.init
    while 1:
        pygame.event.pump()
        display = pygame.display.set_mode()
        pygame.draw.lines(display, "black", False, list(threeplus1_iters_dict.items()))
        dictionary = list(threeplus1_iters_dict.items())
        max_so_far = 0
        for i in range(len(dictionary)):
            if (dictionary[i][1] > max_so_far):
                max_so_far = dictionary[i][1]
        new_display = pygame.transform.flip(display, False, False)
        display.blit(new_display, (0, 0))
        font = pygame.font.Font(None, 48)
        msg = font.render(("Max so far is:" + str(max_so_far)), False, "aquamarine")
        display.blit(msg, (1200, 10))
        pygame.display.flip()
        break
    pygame.time.wait(1000)

def main():
    print(threenp1range(20))
    graph_coordinates(threenp1range(20))

main()