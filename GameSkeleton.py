''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys
import random

'''-----------------------Initialisation-----------------------'''
### Game Startup ###
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
screenDimensions = (1024, 600) # Setting the displays dimensions as a tuple / list
pygame.display.set_mode((screenDimensions))
pygame.display.set_caption('Space Game') # Setting bar title of game window #
clock = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
#pygame.font.init()
#myfont = pygame.font.SysFont()

# Getting the drawing surface & background #
screen = pygame.display.get_surface() # Where graphics/visual output displayed #
#screen.blit(image) will output any image file to screen

# Keeping tack of which keys pressed #
pressed = None

# Construct Spaceship Object #
spaceship = Spaceship(screen, 500, 300)
bulletgroup = pygame.sprite.Group()
background = pygame.image.load("background2.jpg")

Exit = False
canshoot = True

'''--------------------------GameLoop--------------------------'''
### Loop which runs until exit=True, forms basis of what happens in game ###

while not Exit:

    # Control the rate at which game run --> framerate set to 60fps #
    clock.tick(60)

    ### Process Main Events and Logic ###
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True
        elif event.type == USEREVENT + 1:
            canshoot = True
            pygame.time.set_timer(USEREVENT + 1, 0)

    # Player input put into "pressed" and transfered into spaceship object where object movement controlled #
    pressed = pygame.key.get_pressed()
    spaceship.update(pressed)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    spaceship.rotate(mouse_x, mouse_y)
    
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if canshoot:
            b = Bullet(screenDimensions, spaceship.rect.centerx, spaceship.rect.centery, mouse_x, mouse_y, 5)
            bulletgroup.add(b)
            canshoot = False
            pygame.time.set_timer(USEREVENT + 1, 500)
    

    #DRAWING CODE---------------------------------
    # Refreshing screen every time loop run #
    #screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    spaceship.draw(screen)
    bulletgroup.draw(screen)
    bulletgroup.update()
    pygame.display.flip()
    
'''Exits the game'''
print("Exiting")
pygame.quit()
sys.exit(0)


