import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet.'''
    def __init__(self, ai_game):
        '''Initialize the alien and set its starting position'''
        super().__init__()
        self.screen = ai_game.screen

        #load the alien image and set its rect attribute.
        self.image = pygame.image.load('./images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
