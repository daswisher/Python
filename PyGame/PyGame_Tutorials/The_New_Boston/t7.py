import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
#Setup a list of points for pygame to connect in order to make a shape
points=[(20,120),(140,140), (110,30)]
#predefine the object color
color=(255,255,0)
while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.lock()
	#using points instead of a shape tool automatically makes pygame connect the dots
	pygame.draw.polygon(screen, color, points)
	screen.unlock()
	pygame.display.update()
	

