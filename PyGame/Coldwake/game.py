import sys
import time
import pygame
from pygame.locals import *

#Imports the various components that constitute the game
import state
import level
import player
import title
import hud
import highscores
import surface_manager

class Game(state.State):
	#Initialize the score values by starting them at 0
    score = 0
    streak_counter = 0
    combo_timer = time.clock()
    player
    def __init__(self):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.level_manager = state.StateMachine(self, level.Level())
        self.player = player.Player()
        Game.player = self.player
        self.hud_manager = state.StateMachine(self, hud.Hud(self, self.player, self.timer))
        #Loads the background image
        self.background = pygame.image.load("data/images/menu_background.jpg").convert()
        #Adds the player's character to the game window
        surface_manager.add(self.player)
        pygame.display.update

    def exit(self):
        Game.score = 0
        Game.streak_counter = 0

    def reason(self):
		#Sets up the in-game exit ability
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.level_manager.current_state.exit()
            return title.Title()
        if self.player.pos_y > self.display.get_height():
            if Game.streak_counter > 1:
                Game.score += 5 * (Game.streak_counter*2)
            self.level_manager.current_state.exit()
            return highscores.HighScores(Game.score)
    #These are the user actions
    def act(self):
        self.timer.tick(60)
        surface_manager.clear(self.display, self.background)
        #Sets up the key-press functions
        keys = pygame.key.get_pressed()
        #Jump
        if keys[K_SPACE]:
            self.player.jump()
        else:
            self.player.stop_jumping()
        #Shoot
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_f:
                    self.player.shoot()
        
        check_for_combo()
        self.level_manager.update()
        surface_manager.update()
        dirty_rects = surface_manager.draw(self.display)
        pygame.display.update(dirty_rects)
#Updates the score
def update_score():
	#Adds 5 points for everytime an orb is shot
    Game.score += 5
    Game.combo_timer = time.clock()
    #Adds to the streak counter to be used in combo points
    Game.streak_counter += 1
#Sets up the combo score values and the streak counter
def check_for_combo():
    if Game.streak_counter > 1 and time.clock() > Game.combo_timer + 1:
        Game.score += 5 * (Game.streak_counter*2)
        hud.show_combo(5 * (Game.streak_counter*2))
        Game.streak_counter = 0
