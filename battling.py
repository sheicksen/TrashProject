import pygame
from Shop import sword_upgrade_level, armor_upgrade_level
from dataclasses import dataclass

# initializing pygame
pygame.init()

# setting up the background screen
SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bought_sword = ""
@dataclass
class Player:
    """
    This class represents the player
    Fields:
        hp = health points
        cp = combat points (how much damage they do)
        player_image = their 'sprite' or png image to represent the character
    Methods:
        draw_player places the player on the left side of the screen
    """
    def __init__(self,hp,cp):
        self.hp = hp + armor_upgrade_level
        self.cp = cp + sword_upgrade_level
        player_image = pygame.image.load('battleImages/Tim.png')
        self.image = pygame.transform.scale(player_image,(300,300))
    def draw_player(self):
        screen.blit(self.image,(100,SCREEN_HEIGHT-350))

player = Player(10,5)

@dataclass
class Monster():
    """
        This class represents the monster
        Fields:
            hp:int = health points
            cp:int = combat points (how much damage they do)
            monster_image = monster's 'sprite' or png image to represent the monster
        Methods:
            draw_monster places the monster on the right side of the screen
    """
    def __init__(self,hp,cp):
        self.hp = hp
        self.cp = cp
        monster_image = pygame.image.load('battleImages/Enemy.png')
        self.image = pygame.transform.scale(monster_image,(300,300))
    def draw_monster(self):
        screen.blit(self.image,(SCREEN_WIDTH-350,SCREEN_HEIGHT-350))

monster = Monster(6,3)

#setting up text boxes
font = pygame.font.SysFont('Arial',20)
text_color = (255,255,255) #white
background_color = (0,0,0) #black
def draw_text(text:str,x:int,y:int):
    """
    This function places text at a specified location on the screen
    :param text: represents the text you wish to display
    :param x: represents the x-coordinate of where you wish to display the text
    :param y: represents the y-coordinate of where you wish to display the text
    """
    text_box = font.render(text,True,text_color,background_color)
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
        # creates an imaginary rectangle where the button image is, when using the collision function to check if the
        # mouse is colliding with the button, it will actually be checking if it is colliding with this rectangle
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def draw_button(self):
        screen.blit(self.image,(self.x,self.y))


# create button instances that will be drawn in the Main function
attack_button = Button('battleImages/Fight.png', SCREEN_WIDTH-800,250)
run_button = Button('battleImages/Run.png',SCREEN_WIDTH-800,300)
home_button = Button('static/images/homeButt.png',SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2)

def Main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battle Time')
    background = pygame.image.load('battleImages/Background.png')
    pygame.display.update()
    """This function runs the entire program and allows this program to be run from home.py"""
    run = True
    battle = True
    ran_away = False
    while run:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():

            # check if player closes the window, which causes the program to end
            if event.type == pygame.QUIT:
                run = False

            # check if player switches to the home screen, which runs the home screen's program
            if event.type == pygame.MOUSEBUTTONDOWN and home_button.rect.collidepoint(mouse_position):
                from home import Main
                Main()

        # draw what will always be present on battling screen
        screen.blit(background, (0, 0))
        player.draw_player()
        #player.change_stats()
        monster.draw_monster()

        if battle:
            # displays the amount of health the player and monster have
            draw_text("HP: " + str(player.hp), 200, SCREEN_HEIGHT - 370)
            draw_text("HP: " + str(monster.hp), SCREEN_WIDTH - 250, SCREEN_HEIGHT - 370)

            # displays combat options and text
            draw_text("Oh no, there's a monster! Would you like to attack it or try to run away?", SCREEN_WIDTH - 1000,
                      100)
            attack_button.draw_button()
            run_button.draw_button()
            for event in pygame.event.get():

                # checks if player clicked the attack button and reduces healths accordingly
                if (event.type == pygame.MOUSEBUTTONDOWN and attack_button.rect.collidepoint(mouse_position)
                        and monster.hp > 0 and player.hp > 0):
                    monster.hp = monster.hp - player.cp
                    attacked = True
                    player.hp = player.hp - monster.cp

                    # displays text showing how much damage was dealt to and by the player
                    if attacked:
                        draw_text("You attacked the monster and did " + str(player.cp) + " damage.",
                                  SCREEN_WIDTH - 1000, 125)
                        draw_text("The monster attacked you and did " + str(monster.cp) + " damage.",
                                  (SCREEN_WIDTH - 1000), 150)
                        pygame.display.update()
                        pygame.time.wait(2250)
                        attacked = False

                # checks if player clicked the run away button
                if (event.type == pygame.MOUSEBUTTONDOWN and run_button.rect.collidepoint(mouse_position)
                        and monster.hp > 0 and player.hp > 0):
                    ran_away = True
                    battle = False

                # ends the battle scene when either the player or monster has been defeated
                if monster.hp <= 0 or player.hp <= 0:
                    battle = False
        if not battle:
            # displays a message depending on the outcome of the battle and displays a button to return to home screen
            if ran_away:
                draw_text("You ran away from the monster. Pick up more trash to get stronger.", SCREEN_WIDTH - 1000,200)
                home_button.draw_button()
            if monster.hp <= 0:
                draw_text("Good Job! You defeated the monster!", SCREEN_WIDTH - 900, 200)
                home_button.draw_button()
            if player.hp <= 0:
                draw_text("Good Job! PSYCH! The monster beat you.", SCREEN_WIDTH - 1000, 200)
                home_button.draw_button()
        pygame.display.update()
    pygame.quit()

Main()
