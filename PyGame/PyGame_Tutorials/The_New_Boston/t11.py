import pygame, sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

color=(200,155,64)
points=[]


while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==MOUSEBUTTONDOWN:
			points.append(event.pos)
	if len(points)>1:
		#False means that if there's multiple lines, then python won't connect them)
		pygame.draw.lines(screen, color, False, points, 3)
	pygame.display.update()
	

