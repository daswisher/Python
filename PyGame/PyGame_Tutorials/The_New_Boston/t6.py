import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)

while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	#prevents shapes from being displayed while they're being drawn
	screen.lock()
	#Surface, rgb values, shape(location, size)
	pygame.draw.rect(screen, (140,240,100), Rect((100,100),(200,100)))
	#allows the screen to be modified after the object is drawn
	screen.unlock()
	pygame.display.update()
	
