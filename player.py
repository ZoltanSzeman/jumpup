# Created by Zoltan Szeman
# 2020-05-27

import pygame

class Player():
    """Create a player with image and attributes."""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/0.jpg')
        self.rect = self.image.get_rect()
        
    def blitme(self):
        """Draw the player at its current location."""
        if self.rect.bottom < self.screen_rect.top:
            # Create a rectangle for when the ball is out of the screen.
            self.screenout_width = 64 - 64 * (self.rect.bottom / (-300))
            self.screenout_rect = pygame.Rect(0, 0, self.screenout_width, 5)
            self.screenout_rect.centerx = self.rect.centerx
            self.screenout_rect.top = self.screen_rect.top
            pygame.draw.rect(self.screen, (0, 255, 0), self.screenout_rect)
        else:
            # If the ball is inside the screen then draw the ball.
            self.screen.blit(self.image, self.rect)
