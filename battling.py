import pygame
from dataclasses import dataclass
pygame.init()

SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Battle Time')
background = pygame.image.load('battleImages/Background.png')
@dataclass
class Player:
    """Returns a character whose stats correspond with what's been unlocked by the player"""
    def __init__(self,hp,cp):
        self.hp = hp
        self.cp = cp
        player_image = pygame.image.load('battleImages/Tim.png')
        self.image = pygame.transform.scale(player_image,(300,300))
    def draw_player(self):
        screen.blit(self.image,(100,SCREEN_HEIGHT-350))

player = Player(10,5)

@dataclass
class Monster():
    def __init__(self,hp,cp):
        self.hp = hp
        self.cp = cp
        monster_image = pygame.image.load('battleImages/Enemy.png')
        self.image = pygame.transform.scale(monster_image,(300,300))
    def draw_monster(self):
        screen.blit(self.image,(SCREEN_WIDTH-350,SCREEN_HEIGHT-350))

monster = Monster(6,3)

font = pygame.font.SysFont('Arial',20)
text_color = (255,255,255) #white
background_color = (0,0,0) #black
def draw_text(text:str,x:int,y:int):
    text_box = font.render(text,True,text_color,background_color)
    screen.blit(text_box,(x,y))
@dataclass
class Button():
    def __init__(self,image,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
    def draw_button(self):
        screen.blit(self.image,(self.x,self.y))

attack_button = Button('battleImages/Tim.png', SCREEN_WIDTH-800,225)
run_button = Button('battleImages/Tim.png',SCREEN_WIDTH-800,300)

run = True
while run:
    screen.blit(background,(0,0))
    player.draw_player()
    monster.draw_monster()
    if monster.cp > 0 and player.cp > 0:
        draw_text("Oh no, there's a monster! Would you like to attack it or try to run away?",SCREEN_WIDTH-1000,200)
        attack_button.draw_button()
        run_button.draw_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

