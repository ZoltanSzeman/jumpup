# Created by Zoltan Szeman
# 2020-06-19

import pygame

class GameOver():
    """Create score attributes and image"""
    def __init__(self, screen, settings):
        """A class to report scores."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.msg = 'Game Over! Press Enter to play again or "q" to quit!'
        
        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)
    
        #Turn the message into a rendered image.
        self.msg_image = self.font.render(self.msg, True,
            self.text_color, self.settings.color)
        # Display the score at the center of the screen.
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center
        
    def blitme(self):
        # Draw message to the screen.
        self.screen.blit(self.msg_image, self.msg_rect)
