
class Setting:

    def __init__(self):
        '''Initializing the game settings'''
        #Screen settings
        
        self.screen_w = 500
        self.screen_h = 500
        self.screen_bg = (0,0,0)

        #ship settings
        self.ship_speed = 1

        #bullet settings
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_color = (230,230,230)
        self.bullet_speed = 0.5
        self.bullet_allowed = 3
