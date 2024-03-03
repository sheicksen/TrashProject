# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
clock = pygame.time.Clock()
running = True
button_1_x = 220
button_1_y = 150
button_2_x = 420
button_2_y = 150
image_1 = pygame.image.load('images/Shop.png')
image_1 = pygame.transform.scale(image_1, (400, 400))
image_2 = pygame.image.load('images/red pill.png')
image_2 = pygame.transform.scale(image_2, (125, 125))
image_3 = pygame.image.load('images/blue pill.png')
image_3 = pygame.transform.scale(image_3, (100, 43))

text_font = pygame.font.SysFont(None, 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


while running:
    current_coin_count = 0
    screen.fill("Salmon")
    screen.blit(image_1, (screen.get_width() / 4 - 20, 0))
    button1_color = "blue"
    button2_color = "blue"
    button3_color = "blue"
    button4_color = "blue"
    draw_text("COIN AMOUNT: " + str(current_coin_count), text_font, (0, 0, 0), 0, 0)
    mouse_pos_x = pygame.mouse.get_pos()[0]
    mouse_pos_y = pygame.mouse.get_pos()[1]
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if (button_1_x < mouse_pos_x < button_1_x + 80) and (button_1_y < mouse_pos_y < button_1_y + 80):
        button1_color = "red"
    if (button_2_x < mouse_pos_x < button_2_x + 80) and (button_2_y < mouse_pos_y < button_2_y + 80):
        button2_color = "red"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (button_1_x < mouse_pos_x < button_1_x + 80) and (button_1_y < mouse_pos_y < button_1_y + 80):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Left mouse button clicked on button 1")
        if (button_2_x < mouse_pos_x < button_2_x + 80) and (button_2_y < mouse_pos_y < button_2_y + 80):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Left mouse button clicked on button 2")

    # fill the screen with a color to wipe away anything from last frame
    pygame.draw.rect(screen, button1_color, (button_1_x, button_1_y, 80, 80))
    pygame.draw.rect(screen, button2_color, (button_2_x, button_2_y, 80, 80))
    screen.blit(image_2, (button_1_x-25,button_1_y-25))
    screen.blit(image_3, (button_2_x-10,button_2_y+16))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit()
