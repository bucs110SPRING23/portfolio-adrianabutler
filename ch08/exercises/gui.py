class Mysterybox:
    def __init__(self,x,y):
        """
        initialise the myster box object
        args: mbnum(int), the amount of boxes that will appear on screen
        """
        self.coords = self.x,self.y
        self.click = True #player must click on the box to get it
        self.grows = False #the box always stays the same size
class Tube:
    def __init__(self,x,y):
        """
        initialize the greentube object
        args: gtnum(int), how many will appear on the GUI
        """
        self.appear = (self.x,self.y)
        self.accept_player = False #this is when the player stands on top to enter at begining of game
        self.gets_difficult = int #it becomes harder to enter as you play the game, but starts off easy

class Coin:
    def __init__(self,x,y):
        """
        initializes the coin objects
        args: cnum(int), how many coins will appear on screen
        """
        self.coord = (self.x,self.y)
        self.is_hit = False #the player must touch it to get the coin and make it True.
        self.is_mobile = False #coin remains in one place
    
