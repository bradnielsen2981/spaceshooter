import pygame, os, sys
from pygame.locals import *
import random
import math

class Laser(pygame.sprite.Sprite):

    '''Initialization   --Constructor--'''  
    def __init__(self, screen_dimensions, x, y, targetx, targety, speed):

        super().__init__()  #need to call the super constructor to work with Groups

        # Sprite Image #
        self.image = pygame.image.load("laser.png")
        self.image.convert_alpha()
        self.originalimage = self.image

        # Sprite Positioning #
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.rect.centerx = x
        self.rect.centery = y
    
        self.boundary_x, self.boundary_y = screen_dimensions

        #set angle and rotation
        xdiff = targetx - self.rect.centerx
        ydiff = targety - self.rect.centery
        hypotenuse = math.hypot(xdiff,ydiff)
        self.hspeed = xdiff / hypotenuse * speed
        self.vspeed = ydiff / hypotenuse * speed
        angle = (180 / math.pi) * -math.atan2(xdiff, ydiff) - 90

        self.image, self.rect = self.rot_center(self.image, self.rect, angle)


        '''print(angle)
        self.image = pygame.transform.rotate(self.originalimage, int(angle))
        self.rect = self.image.get_rect() #now update rectangle
        self.rect.center = self.originalimage.get_rect().center'''

        #play sound
        pygame.mixer.music.load('laser.mp3')
        pygame.mixer.music.play()
        return

    #update 
    def update(self):
        self.rect.centerx += self.hspeed
        if (self.rect.centerx > self.boundary_x) or (self.rect.centerx < 0):
            self.kill()
        self.rect.centery += self.vspeed
        if (self.rect.centery > self.boundary_y) or (self.rect.centery < 0):
            self.kill()
        return

    #rotate
    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    #there is already a draw function inside the Sprite Class, its called by the SpriteGroup
    '''def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return'''
    

