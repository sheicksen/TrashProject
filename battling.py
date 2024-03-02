import pygame
pygame.init()

SCREEN_WIDTH = 384
SCREEN_HEIGHT = 128
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Battle Time')
background = pygame.image.load('download.jpg')

class Character():
    """Returns a character whose stats correspond with what's been unlocked by the player"""
    hp:int
    cp:int
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprite = []
        pos_x:int
        pos_y:int

class Monster(pygame.sprite.Sprite):
    hp:int
    cp:int
    def __init__(self):
        super().__init__()
        self.sprite = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

