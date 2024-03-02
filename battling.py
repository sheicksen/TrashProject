import pygame

class Character(pygame.sprite.Sprite):
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


