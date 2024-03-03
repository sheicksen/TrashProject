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
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def draw_button(self):
        screen.blit(self.image,(self.x,self.y))

attack_button = Button('battleImages/Fight.png', SCREEN_WIDTH-800,250)
run_button = Button('battleImages/Run.png',SCREEN_WIDTH-800,300)

run = True
battle = True
ran_away = False
attacked = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    player.draw_player()
    monster.draw_monster()
    if battle:
        draw_text("HP: " + str(player.hp), 200, SCREEN_HEIGHT - 370)
        draw_text("HP: " + str(monster.hp), SCREEN_WIDTH - 250, SCREEN_HEIGHT - 370)
        draw_text("Oh no, there's a monster! Would you like to attack it or try to run away?",SCREEN_WIDTH-1000,100)
        attack_button.draw_button()
        run_button.draw_button()
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN and attack_button.rect.collidepoint(mouse_position)
                    and monster.hp > 0 and player.hp > 0):
                monster.hp = monster.hp - player.cp
                attacked = True
                player.hp = player.hp - monster.cp
                if attacked:
                    draw_text("You attacked the monster and did " + str(player.cp) + " damage.", SCREEN_WIDTH - 1000, 125)
                    draw_text("The monster attacked you and did " + str(monster.cp) + " damage.", (SCREEN_WIDTH - 1000), 150)
                    pygame.display.update()
                    pygame.time.wait(2250)
                    attacked = False

            if (event.type == pygame.MOUSEBUTTONDOWN and run_button.rect.collidepoint(mouse_position)
                    and monster.hp > 0 and player.hp >0):
                ran_away = True
                battle = False
            if monster.hp <= 0 or player.hp <= 0:
                battle = False
    if not battle:
        if ran_away:
            draw_text("You ran away from the monster. Pick up more trash to get stronger.",SCREEN_WIDTH-1000,200)
        if monster.hp <= 0:
            draw_text("Good Job! You defeated the monster!",SCREEN_WIDTH-900,200)
        if player.hp <= 0:
            draw_text("Good Job! PSYCH! The monster beat you.",SCREEN_WIDTH-1000,200)
    pygame.display.update()
pygame.quit()

