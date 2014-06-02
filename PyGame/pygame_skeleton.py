"""
pygame_skeleton.py

Dana Hughes
02-Oct-2013

A skeleton for a simply Pygame program
"""

# Import this to have Python 2.7 behave like Python 3.2
from __future__ import division, absolute_import, print_function, unicode_literals

# Common modules to import
import pygame
from pygame.locals import *

# Some constants for use later 
GAME_TITLE = "My Game Title" # What's the game called?
DISPLAY_SIZE = (640,480)     # Size of the screen for the game (in pixels)
DESIRED_FPS = 30             # Want the game to run at 30 FPS

# Initialize pygame
pygame.init()

# Create a display for the game (this creates a window)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption(GAME_TITLE)

# Create a clock to try to keep the game running at however many FPS
fps_clock = pygame.time.Clock()

# Initial game variables
game_running = True          # Is the player still playing?


##########################
### The main game loop ###
##########################

while game_running:          # Keep going until the player quits

    ##########################
    ### Capture user input ###
    ##########################

    user_input = pygame.event.get()


    #############################
    ### Update the game model ###
    #############################


    #####################################
    ### Redraw the game on the screen ###
    #####################################

    pygame.display.flip()


    # Wait until this frame is finished (as per the FPS clock)
    fps_clock.tick(DESIRED_FPS)

# All done!  Cleanup time
pygame.quit()

