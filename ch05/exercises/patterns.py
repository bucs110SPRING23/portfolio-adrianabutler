def star_pyramid(p):
    for _ in range(p+1):
        print("*" * _ )

star_pyramid(int(input("Enter a number to determine the amount of layers in your pyramid: ")))

def rstar_pyramid(p):
    for _ in range(p+1):
        print("*" * p)
        p -=1

rstar_pyramid(int(input("Enter a number to determine the amount of layers in your pyramid: ")))