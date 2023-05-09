def star_pyramid(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def rstar_pyramid(stars):
    for i in range(stars, 0, -1):
        print("*" * i)

levels = int(input("Enter the desired pyramid height: "))

star_pyramid(levels)
rstar_pyramid(levels)