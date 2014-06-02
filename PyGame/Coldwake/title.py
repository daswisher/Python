import sys
import pygame
from pygame.locals import *

import state
import game
import surface_manager

class Title(state.State):
    def __init__(self):
		#Establishes the initial main menu display by loading background and fonts
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/menu_background.jpg")
        self.font_manager = pygame.font.Font("data/fonts/coders_crux.ttf", 64)
        self.help_font_manager = pygame.font.Font("data/fonts/coders_crux.ttf", 28)
        self.title_font_manager = pygame.font.Font("data/fonts/coders_crux.ttf", 128)

        self.title = self.title_font_manager.render("", True, (100, 100, 100))
        self.title_rect = pygame.Rect((self.display.get_width()/2 - self.title.get_width()/2, self.display.get_height()/2 - self.title.get_height()*2),
            (self.title.get_width(), self.title.get_height()))
        self.title_color = "white"
        #Creates the start option
        self.start_game = self.font_manager.render("START", True, (244, 129, 11))
        self.start_game_rect = pygame.Rect((self.display.get_width()/2 - self.start_game.get_width()/2, self.display.get_height()/2 - self.start_game.get_height()),
            (self.start_game.get_width(), self.start_game.get_height()))
        #Creates the exit option
        self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
        self.exit_game_rect = pygame.Rect((self.display.get_width()/2 - self.exit_game.get_width()/2, self.display.get_height()/2 + self.exit_game.get_height()),
            (self.exit_game.get_width(), self.exit_game.get_height()))

        self.current_choice = 1
        
        self.show_help = False
            
        self.timer = pygame.time.Clock()

    def exit(self):
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
    #Adds key functions to the main menu
    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.current_choice == 1:
                        return game.Game()
                    elif self.current_choice == 2:
                            pygame.quit()
                            sys.exit()
                elif event.key == K_DOWN:
                    self.next_selection()
                elif event.key == K_UP:
                    self.previous_selection()

    def act(self):
        self.timer.tick(40)
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.title, self.title_rect)
        self.display.blit(self.start_game, self.start_game_rect)
        self.display.blit(self.exit_game, self.exit_game_rect)

        pygame.display.update()
    #Updates how the options are rendered when the down key is hit
    def next_selection(self):
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (244, 129, 11))
            self.current_choice = 2
        else:
            self.start_game = self.font_manager.render("START", True, (244, 129, 11))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1
    #Updates how the options are rendered when the up key is hit
    def previous_selection(self):
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (244, 129, 11))
            self.current_choice = 2
        else:
            self.start_game = self.font_manager.render("START", True, (244, 129, 11))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1

        

