import pygame
class character(pygame.sprite.Sprite):
    """Returns a character whose stats correspond with what's been unlocked by the player"""
    hp:int
    cp:int
    def __init__(self):
        super().__init__()
        self.sprites = []

class monster(pygame.sprite.Sprite):
    hp:int
    cp:int
    def __init__(self):
        super()
