import pygame
from dataclasses import dataclass

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Home Screen')
home_screen = pygame.image.load('battleImages/white_background.jpg')

font = pygame.font.SysFont('Arial',50)
text_color = (0,0,0) #black
def draw_text(text:str,x:int,y:int):
    text_box = font.render(text,True,text_color)
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

store_button = Button ('static/images/ShopButt.png',SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2 - 100)
battle_button = Button ('static/images/toBattle.png',SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2 - 25)

run = True
while run:
    mouse_position = pygame.mouse.get_pos()
    screen.blit(home_screen, (0, 0))
    draw_text("Game Title",int(SCREEN_WIDTH/2 - 125), 100)
    store_button.draw_button()
    battle_button.draw_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and store_button.rect.collidepoint(mouse_position):
            from Shop import Main
            Main()

        if event.type == pygame.MOUSEBUTTONDOWN and battle_button.rect.collidepoint(mouse_position):
            from battling import Main
            Main()
    pygame.display.update()
pygame.quit()