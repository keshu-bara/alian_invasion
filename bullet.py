import pygame

from pygame.sprite import Sprite

class bullet(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.color = self.settings.bullet_color

        '''Create a bullet rect at (0,0) and then set correct position'''
        self.rect = pygame.Rect(0,0,self.settings.bullet_w,self.settings.bullet_h)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as float
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)



