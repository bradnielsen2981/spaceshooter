''' Spaceship Sprite Code '''
import pygame
import sys
import math

''' The object for the spaceship in the game '''
class Spaceship(pygame.sprite.Sprite): ##Q what does sprite class mean?

    # Constructing spaceship object #
    def __init__(self,screen, x, y):

        # Overiding Constructor #
        super().__init__() 
        
        # Sprite Image #
        self.image = pygame.image.load("spaceship.png")
        self.image.convert_alpha()
        self.originalimage = self.image

        # Sprite Movement Variables set to 0 at start #
        self.speed_x = 0
        self.speed_y = 0

        # Sprite Positioning #
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.rect.centerx = x
        self.rect.centery = y
    
        self.boundary_x = screen.get_width()
        self.boundary_y = screen.get_height()
        return
    
    # Draws the spacecraft sprite #
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) #when you blit, you have to feed the topleft corner.
        return

    ### Acceleration data gather from user input ###
    def update(self, pressed):
        limit = 601
        if self.speed_y > -limit and self.speed_y < limit:
            if pressed[pygame.K_UP] == 1:
                self.speed_y -= 1
            
            if pressed[pygame.K_DOWN] == 1:
                self.speed_y += 1

        if self.speed_x > -limit and self.speed_x < limit:
            if pressed[pygame.K_LEFT] == 1:
                self.speed_x -= 1

            if pressed[pygame.K_RIGHT] == 1:
                self.speed_x += 1

        #moderate speed_y and speed_x based on 60 frames a second
        #problem where modulas returns only a positive
        v = 0
        if self.speed_y > 0:
            v = self.speed_y%200
        else:
            v = -((-self.speed_y)%200)
        h = 0
        if self.speed_x > 0:
            h = self.speed_x%200
        else:
            h = -((-self.speed_x)%200)

        self.rect.y += v/5   #added even more slowdown by dividing by 5
        self.rect.x += h/5
        
        #check for boundary  
        if (self.rect.top < 0):
            self.rect.top = 0
            self.speed_y = 0
        if (self.rect.bottom > self.boundary_y):
            self.rect.bottom = self.boundary_y
            self.speed_y = 0
        if (self.rect.left < 0):
            self.rect.left = 0
            self.speed_x = 0
        if (self.rect.right > self.boundary_x):
            self.rect.right = self.boundary_x
            self.speed_x = 0
        return
    

    def rotate(self, mouse_x, mouse_y):
        rel_x = mouse_x - self.rect.centerx
        rel_y = mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.originalimage, int(angle))
        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        return


