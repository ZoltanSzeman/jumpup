# Created by Zoltan Szeman
# 2020-05-28

import pygame

class Settings():
    """An object for the basic game settings."""
    def __init__(self):
        # screen settings
        self.size = (700, 600)
        self.color = 0, 0, 0
        # ball movement settings
        self.jump_speed = 1200.0
        self.gravity = 2000.0
        self.x_speed = 3
        self.fps = 120
        self.bounc_factor = 0.3
        
        #platform size, movement and color settings
        self.plat_w_min = 30
        self.plat_w_max = 150
        self.plat_h = 10
        self.plat_no = 10
        self.plat_vel = 1.0
        self.brown = (255, 255, 0)
