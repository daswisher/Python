"""
bug_game.py

Dana Hughes
02-Oct-2013

A simple bug / flower game using pygame.  

Images are from opengameart.org
"""

# Import this to have Python 2.7 behave like Python 3.2
from __future__ import division, absolute_import, print_function, unicode_literals

# Common modules to import
import pygame
from pygame.locals import *

import random

# Some constants for use later 
GAME_TITLE = "My Awesome Bug & Flower Game"
DISPLAY_SIZE = (640,480)     # Size of the screen for the game (in pixels)
DESIRED_FPS = 30             # We want our game to run at 30 Frames per second

# Initialize pygame
pygame.init()

# Create a display for the game (this creates a window)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption(GAME_TITLE)

# Create a clock to try to keep the game running at however many FPS
fps_clock = pygame.time.Clock()

# Initial game variables
game_running = True          # Is the player still playing?

bug_x = 300                  # The bug's starting position
bug_y = 240

flower_x = 100               # The flower's starting position
flower_y = 100

score = 0                    # How many flowers did the player get

bug_color = "red"            # What color is the bug?

# Load the images
background = pygame.image.load("images/background.png")
red_bug = pygame.image.load("images/red_bug.png")
blue_bug = pygame.image.load("images/blue_bug.png")
flower = pygame.image.load("images/flower.png")

bug = red_bug                # The bug image is currently the red one

# The main game loop

while game_running:          # Keep going until the player quits

    ##########################
    ### Capture user input ###
    ##########################

    user_input = pygame.event.get()

    pressed_keys = pygame.key.get_pressed()    # Which keys are down?

    # Debugging stuff, delete if you don't like this printing out
#    print("===================")
#    if pressed_keys[K_q]:
#        print("The 'q' key is pressed.")
#    if pressed_keys[K_UP]:
#        print("The up arrow key is pressed.")
#    if pressed_keys[K_DOWN]:
#        print("The down arrow key is pressed.")
#    if pressed_keys[K_LEFT]:
#        print("The left arrow key is pressed.")
#    if pressed_keys[K_RIGHT]:
#        print("The right arrow key is pressed.")
    # End debugging stuff

    mouse_position = pygame.mouse.get_pos()    # Where's the mouse?

    # More debugging stuff
#    print("The mouse is at position", mouse_position)
#    print("The x position is", mouse_position[0])
#    print("The y position is", mouse_position[1])
    # End debugging stuff

    mouse_buttons = pygame.mouse.get_pressed() # Which buttons are clicked?    

    # More debugging stuff
#    print("The mouse buttons are", mouse_buttons)
#    if mouse_buttons[0]:
#        print("The left button is pressed.")
#    if mouse_buttons[1]:
#        print("The center button is pressed.")
#    if mouse_buttons[2]:
#        print("The right button is pressed.")
    # End debugging stuff

    #############################
    ### Update the game model ###
    #############################

    # Does the user want to quit?
    if pressed_keys[K_q]:
        game_running = False

    # Should we move the bug?
    if pressed_keys[K_UP]:
        bug_y = bug_y - 1
    if pressed_keys[K_DOWN]:
        bug_y = bug_y + 1
    if pressed_keys[K_LEFT]:
        bug_x = bug_x - 1
    if pressed_keys[K_RIGHT]:
        bug_x = bug_x + 1

    # Is the bug and flower touching?
    bug_box = Rect( (bug_x, bug_y), red_bug.get_size())
    flower_box = Rect( (flower_x, flower_y), flower.get_size())

    if bug_box.colliderect(flower_box):        # The two are touching
        score = score + 1
        print ("Current Score is", score)

        flower_x = random.randint(0, DISPLAY_SIZE[0] - flower.get_width())
        flower_y = random.randint(0, DISPLAY_SIZE[1] - flower.get_height())

    # Did the user click on the bug?
    if mouse_buttons[0]:                          # Did the user click?
        if bug_box.collidepoint(mouse_position):  # On the bug?
            # Then swap to the other color (either red or blue)
            if bug_color == "red":
                bug = blue_bug
                bug_color = "blue"
            else:
                bug = red_bug
                bug_color = "red"


    #####################################
    ### Redraw the game on the screen ###
    #####################################

    screen.blit(background, (0,0))             # Draw the background
    screen.blit(flower, (flower_x, flower_y))  # Then the flower
    screen.blit(bug, (bug_x, bug_y))       # And the bug

    pygame.display.flip()                      # All done drawing! 

    # Wait until this frame is finished (as per the FPS clock)
    fps_clock.tick(DESIRED_FPS)

# Finished the game?  Need to clean up!

pygame.quit()
print("The final score is:", score)
