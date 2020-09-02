# Created by Zoltan Szeman
# 2020-05-27

import os, sys, time, pygame
from pygame.sprite import Group
from settings import Settings
from player import Player
from jump_platform import JumpPlatform as JPlatform
from score import Score
from game_over import GameOver
import functions as f

# Center the gaming window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize the pygame instance
pygame.init()

def game():
    # Instantiate objects 1
    settings = Settings()
    # GUI display
    screen = pygame.display.set_mode(settings.size)
    pygame.display.set_caption("JumpUp!")
    # Instantiate objects 2
    player = Player(screen)
    plats = Group()
    score = Score(screen, settings)
    play_again = GameOver(screen, settings)
    clock = pygame.time.Clock()
    # create the first instance of a platform
    new_plat = JPlatform(screen, settings)
    plats.add(new_plat)
    new_plat.update()
    new_plat.draw_me()
    # update screen
    pygame.display.flip()
    # draw player on the top of the first platform.
    player.rect.centerx = new_plat.rect.centerx
    player.rect.bottom = new_plat.rect.top
    
    # [0] - x and [1] - y velocity
    velocity = [settings.x_speed, settings.jump_speed * (-1)]
    # [0] - negative x, [1] - positive x [2] - jumping
    movement = [False, False, False]
    # first image for animation
    image_no = [1]
    # create initial previous position
    #for not getting an error on the first frame
    prev_pos = [-30]

    while True:
        # check if the ball is still in game
        if f.still_playing(player, settings) == True:
            score.update_time() # update score by the second
            score.check_highscore() # check whether we beat the highscore
            delta_t = clock.tick(settings.fps)/1000
            f.create_platform(player, screen, settings, clock, plats)
            f.check_events(player, movement)
            f.moving_the_ball(player, screen, settings, movement, plats,
                                velocity, delta_t, prev_pos)
            f.animate_the_ball(player, movement, image_no)
            f.update_screen(f.still_playing(player, settings),
                            screen, settings, player, play_again, plats, score)
        else:
            f.update_screen(f.still_playing(player, settings),
                            screen, settings, player, play_again, plats, score)
            score.save_highscore() # save the current highscore
            if f.check_quit() == False:
                game()
         
game()
