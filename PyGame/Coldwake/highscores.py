import pygame
from pygame.locals import *

import state
import surface_manager
import title

class HighScores(state.State):
    #Creates an open list of the player scores
    high_scores = []
    #Creates the high score display screen
    def __init__(self, score):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/menu_background_clean.jpg")
        #Adds the score to the high scores list if the user actually had a score
        if score > 0:
            HighScores.high_scores.append(score)
        #This makes the scores list display the scores from highest to lowest values
        HighScores.high_scores.sort(reverse=True)
        #This limits the number of scores within high scores list
        if len(HighScores.high_scores) > 10:
			#Deletes scores that are not within the top ten list
            del HighScores.high_scores[10:]

        self.header_manager = pygame.font.Font("data/fonts/coders_crux.ttf", 84)
        self.header = self.header_manager.render("HIGH SCORES:", True, (244, 129, 11))
        self.header_rect = pygame.Rect((self.display.get_width()/2 -self.header.get_width()/2, 0), (self.header.get_width(), self.header.get_height()))
        self.font_manager = pygame.font.Font("data/fonts/coders_crux.ttf", 28)

	#Causes the program to return the the title screen if the enter key is hit
    def reason(self):
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            return title.Title()

    def act(self):
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.header, self.header_rect)

        for y, score in enumerate(HighScores.high_scores):
            self.display.blit(self.font_manager.render("%d    %d" % (y+1, score), True, (244, 129, 11)), (self.display.get_width()/2 - 64, (self.header_rect.top + self.header.get_height()) + (32*(y+1))))

        pygame.display.update()
        pygame.event.clear()
