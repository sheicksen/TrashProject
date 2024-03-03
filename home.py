import pygame
from dataclasses import dataclass

# initializing pygame
pygame.init()

# setting up the background screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Home Screen')
home_screen = pygame.image.load('battleImages/white_background.jpg')

# setting up title text
font = pygame.font.SysFont('Arial',50)
text_color = (0,0,0) # black


def draw_text(text:str,x:int,y:int):
    """
        This function places text at a specified location on the screen
        :param text: represents the text you wish to display
        :param x: represents the x-coordinate of where you wish to display the text
        :param y: represents the y-coordinate of where you wish to display the text
        """
    text_box = font.render(text,True,text_color)
    screen.blit(text_box,(x,y))


@dataclass
class Button():
    """
        This class represents a button that can be put at a specified location and be clicked with the mouse to carry out an action
        Fields:
        image = the image that will serve as the button to be clicked
        x:int = the x-coordinate of the button's location
        y:int = the y-coordinate of the button's location
        Methods:
            draw_button places the button image at the specified location
        """
    def __init__(self,image,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def draw_button(self):
        screen.blit(self.image,(self.x,self.y))


# create button instances that will be drawn in the Main function
store_button = Button('static/images/ShopButt.png',SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2 - 100)
battle_button = Button('static/images/toBattle.png',SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2 - 25)


def Main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Home Screen')
    home_screen = pygame.image.load('battleImages/white_background.jpg')
    """This function runs the entire program and allows this program to be run from battling.py and Shop.py"""
    run = True
    while run:
        mouse_position = pygame.mouse.get_pos()
        # displays what will always be present on home screen
        screen.blit(home_screen, (0, 0))
        draw_text("Trash Destroyer", int(SCREEN_WIDTH / 2 - 180), 100)
        store_button.draw_button()
        battle_button.draw_button()
        for event in pygame.event.get():
            # check if player closes the window, which causes the program to end
            if event.type == pygame.QUIT:
                run = False
            # check if player switches to the store screen using the button, which runs the store screen's program
            if event.type == pygame.MOUSEBUTTONDOWN and store_button.rect.collidepoint(mouse_position):
                from Shop import Main
                Main()
            # check if player switches to the battle screen using the button, which runs the battle screen's program
            if event.type == pygame.MOUSEBUTTONDOWN and battle_button.rect.collidepoint(mouse_position):
                from battling import Main
                Main()
        pygame.display.update()
    pygame.quit()

Main()