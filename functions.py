# Created by Zoltan Szeman
# 2020-05-28

import sys, time
from random import randint
import pygame
from jump_platform import JumpPlatform as JPlatform

def animate_the_ball(player, movement, image_no):
    """animate the ball rolling"""
    if movement[0]:
        image_no[0] -= 1
        if image_no[0] < 0:
            image_no[0] = 35
    if movement[1]:
        image_no[0] += 1
        if image_no[0] > 35:
            image_no[0] = 0
    player.image = pygame.image.load('images/'+str(int(image_no[0]))+'.jpg')

def check_events(player, movement):
    """Check keyboard events to interact with the game."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # key is pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement[0] = True
            if event.key == pygame.K_RIGHT:
                movement[1] = True
            if event.key == pygame.K_SPACE:
                movement[2] = True # jumping
        # key is let go.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
            if event.key == pygame.K_RIGHT:
                movement[1] = False
                
def check_quit():
    for event in pygame.event.get():
    # key is pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return False
            elif event.key == pygame.K_q:
                sys.exit()
                
def create_platform(player, screen, settings, clock, plats):
    """Create a platform if limit is not reached yet and
        get rid of platforms that have disappeared."""
    for plat in plats:
        plat.update()
        if plat.rect.top > screen.get_rect().bottom:
            plats.remove(plat)
        if (plat.rect.bottom == 150 and
                len(plats) <= settings.plat_no):
            new_plat = JPlatform(screen, settings)
            plats.add(new_plat)
            continue
    
def moving_the_ball(player, screen, settings, movement, plats,
                        velocity, delta_t, prev_pos):
    """horizontal movement of player and jump and bouncing controls."""
    # Move left and right.
    if movement[0]:
        player.rect.centerx -= velocity[0]
        if player.rect.left <= screen.get_rect().left:
            player.rect.left = screen.get_rect().left
    if movement[1]:
        player.rect.centerx += velocity[0]
        if player.rect.right >= screen.get_rect().right:
            player.rect.right = screen.get_rect().right
    if movement[2]: # jumping function
        player.rect.bottom += velocity[1] * delta_t
        velocity[1] += settings.gravity * delta_t
    for plat in plats:
        if (abs(player.rect.bottom - plat.rect.top) <= 5 and
                player.rect.centerx > plat.rect.left and
                player.rect.centerx < plat.rect.right):
            if velocity[1] > 500: # bounce back
                movement[2] = True
                time.sleep(0.025)
                velocity[1] = velocity[1] * settings.bounc_factor * (-1)
            elif velocity[1] > 0 or velocity[1] == settings.jump_speed * (-1):
                # don't bounce back
                player.rect.bottom = plat.rect.top
                velocity[1] = settings.jump_speed * (-1)
                movement[2] = False
        # when the ball is stationary let it fall
        if player.rect.bottom == prev_pos[0]:
            if velocity[1] < 0:
                velocity[1] = 0
            player.rect.bottom += velocity[1] * delta_t
            velocity[1] += settings.gravity * delta_t
    # the previous position of the ball in a variable to check movement
    prev_pos[0] = player.rect.bottom

def still_playing(player, settings):
    """Check whether the ball is still inside the window."""
    if player.rect.top > settings.size[1]:
        return False
    else:
        return True

def update_screen(still_playing,
                    screen, settings, player, play_again, plats, score):
    """Redraw screen and player each frame."""
    screen.fill(settings.color)
    player.blitme()
    # Draw each platform.
    for plat in plats.sprites():
        plat.draw_me()
    # Draw the score and highscore onto the screen
    score.blitme()
    score.blit_highscore()
    # If the game is over then write to the screen
    if still_playing == False:
        play_again.blitme()
    # Refresh the screen each frame
    pygame.display.flip()
