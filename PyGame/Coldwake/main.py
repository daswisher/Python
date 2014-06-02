import pygame, sys, pygame.mixer

import state
import title
import game

pygame.init()
#Sets the dimensions of the game window
display = pygame.display.set_mode((1000,600))
#Changes the title bar on the program window
pygame.display.set_caption("Coldwake Orange {Alpha}")
sound = pygame.mixer.Sound("data/audio/dissolving_time.wav")
sound.play()
#pygame.mixer.music.load("data/audio/dissolving_time.mp3")
#pygame.mixer.music.play("data/audio/dissolving_time.mp3")
class coldwake():
	#Initializes the game state
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = coldwake()
    game.start()

