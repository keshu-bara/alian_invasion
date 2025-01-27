import pygame

from settings import Setting

class Ship:
    '''A claas to manage the ship'''

    def __init__(self,ai_game):
        #initializing the ship and starting its initial position in the screen
       
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading the image and getting its rect
        self.ship = pygame.image.load('./images/ship.png')
        self.rect = self.ship.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement
        self.movement_right = False
        self.movement_left = False

        self.Setting = Setting()
        self.x = self.rect.x



    def update(self):
        if self.movement_right and self.rect.x <= (self.screen_rect.right - self.rect.width):
            self.x += self.Setting.ship_speed
            self.rect.x =int(self.x)
            print(self.rect.x)
        if self.movement_left and self.rect.x >= 0:
            self.x -= self.Setting.ship_speed
            self.rect.x = int(self.x)
           

    def blitme(self):
        '''Draw the ship to its current loc'''
        self.screen.blit(self.ship,self.rect)



