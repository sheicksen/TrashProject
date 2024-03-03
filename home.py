from battling import *
from dataclasses import dataclass

@dataclass
class State:
    store_button:Button
    battle_button:Button

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 120
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Home Screen')
store_button = Button('battleImages/Tim.png',SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


run = True
while run:
    screen.blit(screen, (0, 0))
    store_button.draw_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()