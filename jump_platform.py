# Created by Zoltan Szeman
# 2020-06-15

import pygame
from pygame.sprite import Sprite
from random import randint

class JumpPlatform(Sprite):
    """A class to manage randomly appearing platforms."""
    def __init__(self, screen, settings):
        super().__init__()
        """Initialize platform and it's starting position."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        
        # Create a platform rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0,
            randint(self.settings.plat_w_min, self.settings.plat_w_max),
            self.settings.plat_h)
        self.rect.left = randint(self.screen_rect.left,
                                    self.screen_rect.right - 100)
        self.rect.top = self.screen_rect.top
        
        # initialize color as brown RGB
        self.color = self.settings.brown
        self.bottom = 0
    
    def update(self):
        """Move the platform down the screen."""
        # Update the rect position.
        self.bottom += self.settings.plat_vel
        self.rect.bottom = int(self.bottom)
        
    def draw_me(self):
        """Draw the platform to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
