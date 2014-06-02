import pygame, sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

color=(200,155,64)
position_1=(20,20)
position_2=(150,143)
while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.lock()
	#the 5th parameter is the width of the line
	pygame.draw.line(screen,color,position_1,position_2, 8)
	screen.unlock()
	pygame.display.update()
	
