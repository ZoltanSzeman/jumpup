# Created by Zoltan Szeman
# 2020-06-18

import pygame

class Score():
    """Create score attributes and image"""
    def __init__(self, screen, settings):
        """A class to report scores."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.timer = 0
        
        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)
        # Read in the current highscore settings
        self.highscore_file = open('highscore.txt', 'r+')
        self.highscore = self.highscore_file.read()
        
    def check_highscore(self):
        if int(self.timer) > int(self.highscore):
            self.highscore = str(self.time_sec)
        self.highscore_image = self.font.render('Highscore: '+self.highscore,
            True, self.text_color, self.settings.color)
        # Display the highscore at the top left of the screen.
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.left = self.screen_rect.left + 10
        self.highscore_rect.top = 10
    
    def update_time(self):
        self.timer += 1/120
        self.time_sec = int(self.timer)
        """Turn the time/score into a rendered image."""
        self.time_sec = str(self.time_sec)
        self.score_image = self.font.render('Score: '+self.time_sec, True,
            self.text_color, self.settings.color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
    
    def save_highscore(self):
        """Save the current highscore to file."""
        try:
            self.highscore_file.truncate(0) # delete previous data
            self.highscore_file.seek(0) # go to the beginning of the file
            self.highscore_file.write(self.highscore)
            self.highscore_file.close()
        except:
            pass
        
    def blit_highscore(self):
        """Draw the highscore to the screen."""
        self.screen.blit(self.highscore_image, self.highscore_rect)
        
    def blitme(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
