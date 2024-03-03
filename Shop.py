# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
clock = pygame.time.Clock()
button_1_x = 220
button_1_y = 150
button_2_x = 420
button_2_y = 150
button_3_x = 0
button_3_y = screen.get_height()/2
pygame.display.set_caption('Store')

text_font = pygame.font.SysFont(None, 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

armor_upgrade_level = 1
sword_upgrade_level = 1
current_coin_count = 100
def Main():
    global current_coin_count
    global armor_upgrade_level
    global sword_upgrade_level
    image_2 = pygame.image.load('images/brownSord.png')
    image_2 = pygame.transform.scale(image_2, (75, 75))
    image_3 = pygame.image.load('images/brownArmor.png')
    image_3 = pygame.transform.scale(image_3, (75, 75))
    screen = pygame.display.set_mode((720, 360))
    image_1 = pygame.image.load('images/Shop.png')
    image_1 = pygame.transform.scale(image_1, (400, 400))
    image_2 = pygame.image.load('images/brownSord.png')
    image_2 = pygame.transform.scale(image_2, (75, 75))
    image_3 = pygame.image.load('images/brownArmor.png')
    image_3 = pygame.transform.scale(image_3, (75, 75))
    image_4 = pygame.image.load('static/images/homeButt.png')
    image_4 = pygame.transform.scale(image_4, (75, 75))
    pygame.display.set_caption('Store')
    pygame.display.update()
    running = True
    while running:
        screen.fill("Salmon")
        screen.blit(image_1, (screen.get_width() / 4 - 20, 0))
        button1_color = "blue"
        button2_color = "blue"
        button3_color = "blue"
        draw_text("COIN AMOUNT: " + str(current_coin_count), text_font, (0, 0, 0), 0, 0)
        mouse_pos_x = pygame.mouse.get_pos()[0]
        mouse_pos_y = pygame.mouse.get_pos()[1]
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        if sword_upgrade_level == 2:
            image_2 = pygame.image.load('images/blueSord.png')
            image_2 = pygame.transform.scale(image_2, (75, 75))
        elif sword_upgrade_level == 3:
            image_2 = pygame.image.load('images/redSord.png')
            image_2 = pygame.transform.scale(image_2, (75, 75))
        elif sword_upgrade_level == 4:
            image_2 = pygame.image.load('images/SoldOut.png')
        if(armor_upgrade_level == 2):
            image_3 = pygame.image.load('images/blueArmor.png')
            image_3 = pygame.transform.scale(image_3, (75, 75))
        elif armor_upgrade_level==3:
            image_3 = pygame.image.load('images/redArmor.png')
            image_3 = pygame.transform.scale(image_3, (75, 75))
        elif armor_upgrade_level==4:
            image_3 = pygame.image.load('images/SoldOut.png')
        if (button_1_x < mouse_pos_x < button_1_x + 80) and (button_1_y < mouse_pos_y < button_1_y + 80):
            button1_color = "red"
        if (button_2_x < mouse_pos_x < button_2_x + 80) and (button_2_y < mouse_pos_y < button_2_y + 80):
            button2_color = "red"
        if (button_3_x < mouse_pos_x < button_3_x + 80) and (button_3_y < mouse_pos_y < button_3_y + 80):
            button3_color = "red"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (button_1_x < mouse_pos_x < button_1_x + 80) and (button_1_y < mouse_pos_y < button_1_y + 80):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and current_coin_count >
                        sword_upgrade_level*10 and sword_upgrade_level <=3):
                    current_coin_count += -(sword_upgrade_level * 10)
                    sword_upgrade_level += 1
                    print("Left mouse button clicked on button 1")
            if (button_2_x < mouse_pos_x < button_2_x + 80) and (button_2_y < mouse_pos_y < button_2_y + 80):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and current_coin_count >
                                                                 (armor_upgrade_level*10) and armor_upgrade_level <=3):
                    current_coin_count += -(armor_upgrade_level*10)
                    armor_upgrade_level+=1
                    print("Left mouse button clicked on button 2")
            if (button_3_x < mouse_pos_x < button_3_x + 80) and (button_3_y < mouse_pos_y < button_3_y + 80):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print("Left mouse button clicked on button 3")
                    from home import Main1
                    Main1()

        # fill the screen with a color to wipe away anything from last frame
        pygame.draw.rect(screen, button1_color, (button_1_x, button_1_y, 80, 80))
        pygame.draw.rect(screen, button2_color, (button_2_x, button_2_y, 80, 80))
        pygame.draw.rect(screen, button3_color, (button_3_x, button_3_y, 80, 80))
        screen.blit(image_2, (button_1_x,button_1_y))
        screen.blit(image_3, (button_2_x,button_2_y))
        screen.blit(image_4, (button_3_x, button_3_y))
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
    pygame.quit()

#Main()