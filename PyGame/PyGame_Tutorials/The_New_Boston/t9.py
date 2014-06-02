import pygame, sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

#an ellipse requires a rectangle in order to draw
color=(0,255,255)
#rectangles take 4 parameters (xy coordinates, and the width and height)
rectangle=(40, 80,150,90)

while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.lock()
	pygame.draw.ellipse(screen, color, rectangle)
	screen.unlock()
	pygame.display.update()
	


