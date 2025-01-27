#creating a game window that have the blue sky
import sys
import pygame


class blue_sky:
    '''Initializing the game'''
    def __init__(self,bg_color = (230,230,230)):
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((500,500)) 
        pygame.display.set_caption("BlueSky")

    def run_game(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

b_game = blue_sky((100,100,200))
b_game.run_game()
