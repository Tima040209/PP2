import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
color = RED
x = 100
y = 100
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Getting all pressed buttons
    pressed = pygame.key.get_pressed()

        

    if pressed[pygame.K_UP]:
        y -= 20
    if pressed[pygame.K_DOWN]:
        y += 20
    if pressed[pygame.K_LEFT]:
        x -= 20
    if pressed[pygame.K_RIGHT]:
        x += 20

    if x + 25 >= 500:
        x = 26
    if x - 25 <= 0:
        x = 475
    if y - 25 >= 500:
        y = 26
    if y - 25 <= 0:
        y = 475
    screen.fill(WHITE)
        
    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(10)
