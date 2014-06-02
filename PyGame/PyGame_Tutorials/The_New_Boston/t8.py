import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
#circles aren't made the same way as polygons
#predefine color, origin, and radius
color=(230,160,150)
point_of_origin=(300,240)
radius=(30)
while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.lock()
	#by only having a single point, will cause pygame to draw a circle
	pygame.draw.circle(screen, color, point_of_origin, radius)
	screen.unlock()
	pygame.display.update()
	


