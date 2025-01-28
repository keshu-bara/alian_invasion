import sys
import pygame
from settings import Setting
from bullet import bullet
from ship import Ship
from alien import Alien


class AlianInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initailize the game, and create game resources'''
        icon = pygame.image.load('./images/logo.png')
        pygame.display.set_icon(icon)

        self.setting = Setting()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        
        self.bg_color = self.setting.screen_bg

        pygame.display.set_caption("Alian Invasion")

        self.ship = Ship(self)
        #bullet initializing
        self.bullets = pygame.sprite.Group()
        #creating alien 
        self.aliens = pygame.sprite.Group()

        self._create_fleet()



    def _create_fleet(self):
        '''Create the fleet of aliens'''
        alien = Alien(self)

        #getting screen width

        screen_w = self.screen.get_width()
        alien_w = alien.rect.width

        #to calculate number of aliens
        allowed_screen = screen_w - (2*alien_w)
        allowed_alien = allowed_screen//(2*alien_w)

        for i in range(allowed_alien):
            #create an alien and place it in a row
            alien = Alien(self)
            alien.x = alien_w + 2*alien_w*i
            alien.rect.x = alien.x
            self.aliens.add(alien)




        self.aliens.add(alien)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
            

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                                    
                  
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
                     
    def _fire_bullets(self):
        
        if len(self.bullets) <= self.setting.bullet_allowed:           
            new_bullet = self.bullet = bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = True
        if event.key == pygame.K_LEFT:
            self.ship.movement_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()


    def _check_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = False
        if event.key == pygame.K_LEFT:
            self.ship.movement_left = False
    def _update_bullets(self):
        self.bullets.update()
            # Get rid of bullets that have diappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))  
          
         
                
         
    def _update_screen(self):
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # Make the most recently drawn screen visible.
            self.aliens.draw(self.screen)

            pygame.display.flip()



if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlianInvasion()
    ai.run_game()
